from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product
from .serializers import ProductSerializer
from django.utils import timezone

PRODUCTS_URL = reverse('product-list')

class ProductTests(TestCase):
    """Test the products API"""

    def setUp(self):
        self.client = APIClient()

    def test_create_product(self):
        """Test creating a product"""
        payload = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 10.00,
            'quantity': 1,
        }
        res = self.client.post(PRODUCTS_URL, payload)
        print(res)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        product = Product.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(product, key))
    
    def test_create_product_invalid(self):
        """Test creating a product with invalid payload"""
        payload = {
            'name': '',
            'description': '',
            'price': 0.00,
            'quantity': 0,
        }
        res = self.client.post(PRODUCTS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_get_all_products(self):
        """Test getting all products"""
        Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            quantity=1,
        )
        Product.objects.create(
            name='Test Product 2',
            description='Test Description 2',
            price=20.00,
            quantity=2,
        )
        res = self.client.get(PRODUCTS_URL)

        products = Product.objects.all().order_by('id')
        serializer = ProductSerializer(products, many=True)
        print(f'\n\n{res.data}\n\n')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_product(self):
        """Test getting a single product"""
        product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            quantity=1,
        )
        url = reverse('product-list', args=[product.id])
        res = self.client.get(url)

        serializer = ProductSerializer(product)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
    
    def test_update_product(self):
        """Test updating a product"""
        product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            quantity=1,
        )
        payload = {
            'name': 'Test Product 2',
            'description': 'Test Description 2',
            'price': 20.00,
            'quantity': 2,
        }
        url = reverse('product-list', args=[product.id])
        res = self.client.put(url, payload)

        product.refresh_from_db()
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(product, key))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_update_product_invalid(self):
        """Test updating a product with invalid payload"""
        product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            quantity=1,
        )
        payload = {
            'name': '',
            'description': '',
            'price': 0.00,
            'quantity': 0,
        }
        url = reverse('product-list', args=[product.id])
        res = self.client.put(url, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_delete_product(self):
        """Test deleting a product"""
        product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            quantity=1,
        )
        url = reverse('product-list', args=[product.id])
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.filter(id=product.id).exists(), False)

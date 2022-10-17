from fastapi import FastAPI
from .models import Product
from .database import products_db


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/products")
async def get_products():
    return {"products": products_db}


@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return products_db[product_id - 1]


@app.post("/products")
async def create_product(product: Product):
    products_db.append(product.dict())
    return product


@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    products_db[product_id - 1] = product.dict()
    return product


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    products_db.pop(product_id - 1)
    return {"task": "delete successful"}

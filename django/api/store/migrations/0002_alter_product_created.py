# Generated by Django 3.2.8 on 2022-10-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

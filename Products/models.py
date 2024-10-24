from django.db import models
from base.models import BaseModel
# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=256)
    category_image = models.ImageField(upload_to="Category")


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    description = models.TextField()


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product")


from django.db import models

# Create your models here.
from .managers import ProductManager

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    objects = ProductManager()

    def __str__(self):
        return self.name

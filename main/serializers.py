from rest_framework.serializers import ModelSerializer
from rest_framework.fields import IntegerField

from .models import Product, Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')


class ProductSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = ('id','name','price','stock','category', 'category_id')

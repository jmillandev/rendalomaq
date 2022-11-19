from rest_framework.serializers import ModelSerializer

from .models import Product, Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')


class ProductSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id','name','price','stock','category')

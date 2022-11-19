from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from main.models import Product
from main.serializers import ProductSerializer

class ProductViewSet(GenericViewSet, ListModelMixin):
    queryset = Product.objects
    serializer_class = ProductSerializer

    # TODO List and filter products
    # def get(self, request, *args, **kwargs):
    #     return Response([])

    # TODO Create Products
    # def post(self, request, *args, **kwargs):
    #     pass

    # TODO: Create Endpoint
    # def prices_avg(self, request, *args, **kwargs):
    #     pass

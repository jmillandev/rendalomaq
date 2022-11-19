from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework import status
from rest_framework.response import Response

from main.models import Product
from main.serializers import ProductSerializer

class ProductViewSet(GenericViewSet, ListModelMixin):
    queryset = Product.objects
    serializer_class = ProductSerializer
    # TODO List and filter products

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "success"}, status=status.HTTP_201_CREATED)

    # TODO: Create Endpoint
    # def prices_avg(self, request, *args, **kwargs):
    #     pass

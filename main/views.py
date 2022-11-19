from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request

from main.models import Product
from main.serializers import ProductSerializer
from .filters import ProductFilter
from rendalo.mixins import ListFilterModelMixin


class ProductViewSet(ListFilterModelMixin, GenericViewSet):
    queryset = Product.objects
    serializer_class = ProductSerializer
    filter_class = ProductFilter

    def create(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "success"}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_name='price-avg')
    def price_avg(self, _: Request) -> Response:
        return Response({"price_avg": self.queryset.get_price_avg()}, status=status.HTTP_200_OK)

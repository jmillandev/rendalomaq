from typing import Union, List
from django.db.models import QuerySet
from .models import Product

ProductQuerySet = Union[QuerySet, List[Product]]

class ProductFilter:
    def __init__(self, queryset: ProductQuerySet = None) -> None:
        if not isinstance(queryset, QuerySet):
            queryset = Product.objects.all()
        self.queryset = queryset

    def by_category_id(self, category_id: int)-> ProductQuerySet:
        self.queryset = self.queryset.filter(category_id=category_id)
        return self

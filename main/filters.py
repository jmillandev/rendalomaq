from typing import Union, List
from django.db.models import QuerySet
from .models import Product
from rendalo.filters import Filter

ProductQuerySet = Union[QuerySet, List[Product]]

class ProductFilter(Filter):
    
    def __init__(self, queryset: ProductQuerySet = None) -> None:
        if not isinstance(queryset, QuerySet):
            queryset = Product.objects.all()
        super().__init__(queryset)

    def by_category_id(self, category_id: int)-> ProductQuerySet:
        self._queryset = self._queryset.filter(category_id=category_id)
        return self

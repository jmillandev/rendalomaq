import pytest

from main.filters import ProductFilter

from .recipes import generic_category, generic_product

@pytest.mark.django_db
def test_get_products_filtered_by_category():
    cat1 = generic_category.make()
    cat2 = generic_category.make()
    prod1 = generic_product.make(price=10, category=cat1)
    prod2 = generic_product.make(price=20, category=cat1)
    generic_product.make(price=30, category=cat2)

    # I thinks that intention to create this service is to use it as filter API 
    filter = ProductFilter().by_category_id(cat1.id)

    assert list(filter.queryset) == [prod1, prod2]

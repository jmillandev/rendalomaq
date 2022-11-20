import pytest

from main.models import Product

from .recipes import generic_product

@pytest.mark.django_db
def test_get_average_product_price():
    generic_product.make(price=10)
    generic_product.make(price=20)
    generic_product.make(price=30)
    # I thinks that is better use services to business logic. If you need do read operation in the DB, use a 'manager'
    assert Product.objects.get_price_avg() == 20.0

import pytest
from django.urls import reverse
from rest_framework import status

from main.models import Product

from .factories import generic_product, generic_category


@pytest.mark.django_db
def test_product_list_view(client):
    prod1 = generic_product.make(
        name="prod1",
        price=10,
        stock=2,
        category=generic_category.make(name="cat1"),
    )
    path = reverse('products-list')
    response = client.get(path)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "id": prod1.id,
            "name": "prod1",
            "price": 10,
            "stock": 2,
            "category": {
                "id": prod1.category.id,
                "name": "cat1",
            }
        }
    ]


@pytest.mark.django_db
def test_product_list_view_filter_by_category(client):
    cat1 = generic_category.make()
    cat2 = generic_category.make()
    prod1 = generic_product.make(price=10, category=cat1)
    prod2 = generic_product.make(price=20, category=cat1)
    generic_product.make(price=30, category=cat2)
    path = reverse('products-list')
    response = client.get(path, {'category_id': cat1.id, 'name': 24})

    assert response.status_code == status.HTTP_200_OK
    assert list(map(lambda x: x["id"], response.json())) == [
        prod1.id, prod2.id]


@pytest.mark.django_db
def test_product_create_view(client):
    category = generic_category.make(name="cat1")
    path = reverse('products-list')
    response = client.post(
        path,
        {
            "name": "prod1",
            "price": 10,
            "stock": 2,
            "category_id": category.id
        },
        content_type="application/json"
    )

    assert response.status_code == status.HTTP_201_CREATED, response.data
    assert response.json() == {"message": "success"}
    assert Product.objects.count() == 1


@pytest.mark.django_db
def test_average_price_view(client):
    generic_product.make(price=10)
    generic_product.make(price=20)
    generic_product.make(price=30)
    path = reverse('products-price-avg')
    response = client.get(path)

    assert response.status_code == status.HTTP_200_OK, response.data
    assert response.json() == {"price_avg": 20.0}

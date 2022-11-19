import pytest
from django.urls import reverse
from model_bakery.recipe import Recipe
from rest_framework import status
from .models import Product
from .filters import ProductFilter

generic_product = Recipe(
    "main.Product",
)

generic_category = Recipe(
    "main.Category",
)


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


@pytest.mark.django_db
def test_get_average_product_price():
    generic_product.make(price=10)
    generic_product.make(price=20)
    generic_product.make(price=30)
    # I thinks that is better use services to business logic. If you need do read operation in the DB, use a 'manager'
    assert Product.objects.get_price_avg() == 20.0


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
    response = client.get(path, {'category_id': cat1.id})

    assert response.status_code == status.HTTP_200_OK
    assert list(map(lambda x: x["id"], response.json())) == [prod1.id, prod2.id]

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

    assert response.json() == { "message": "success" }
    assert Product.objects.count() == 1 

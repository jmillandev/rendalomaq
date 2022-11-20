from django.urls import reverse, resolve
from django.test import TestCase


class AffiliateUrlTests(TestCase):

    def test_list(self):
        view_name = 'products-list'
        # TODO: '/v1/products/' It's Better
        path = '/v1/main/products/'

        self.assertEqual(reverse(view_name), path)
        self.assertEqual(resolve(path).view_name, view_name)

    def test_price_avg(self):
        view_name = 'products-price-avg'
        # TODO: '/v1/products/price-avg/' It's Better
        path = '/v1/main/products/price-avg/'

        self.assertEqual(reverse(view_name), path)
        self.assertEqual(resolve(path).view_name, view_name)

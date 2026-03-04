from django.test import TestCase
from django.urls import reverse

from .models import Category, Product


class ModelSmokeTests(TestCase):
    def test_category_str(self):
        cat = Category.objects.create(name='foo')
        self.assertEqual(str(cat), 'foo')

    def test_product_str(self):
        cat = Category.objects.create(name='bar')
        prod = Product.objects.create(
            name='baz', description='d', price='1.00', category=cat
        )
        self.assertEqual(str(prod), 'baz')


class ViewSmokeTests(TestCase):
    def test_home_status(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_products_list(self):
        resp = self.client.get(reverse('products'))
        self.assertEqual(resp.status_code, 200)

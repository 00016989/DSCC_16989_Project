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

from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category


class AdditionalTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_user_creation(self):
        user = User.objects.create_user(
            username='testuser2',
            password='testpass123'
        )
        self.assertEqual(User.objects.count(), 1)

    def test_category_string_representation(self):
        category = Category.objects.create(name="Electronics")
        self.assertEqual(str(category), "Electronics")
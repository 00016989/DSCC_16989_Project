from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Category, Product


class ModelSmokeTests(TestCase):

    def test_category_str(self):
        category = Category.objects.create(name="Electronics")
        self.assertEqual(str(category), "Electronics")

    def test_product_str(self):
        category = Category.objects.create(name="Electronics")
        product = Product.objects.create(
            name="Laptop",
            category=category,
            price=1000
        )
        self.assertEqual(str(product), "Laptop")


class ViewSmokeTests(TestCase):

    def test_home_status(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_products_list(self):
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)


class AdditionalTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_user_creation(self):
        User.objects.create_user(
            username="testuser2",
            password="testpass123"
        )
        self.assertEqual(User.objects.count(), 1)

    def test_category_string_representation(self):
        category = Category.objects.create(name="Books")
        self.assertEqual(str(category), "Books")

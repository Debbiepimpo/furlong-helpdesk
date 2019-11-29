from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")

    def test_get_cart_page(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")

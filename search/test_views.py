from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestViews(TestCase):

    def test_get_search_page(self):
        page = self.client.get("/search/?q=")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "search.html")

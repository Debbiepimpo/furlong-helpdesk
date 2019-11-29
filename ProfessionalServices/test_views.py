from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import PServices, PServices_Bought
from django.shortcuts import get_object_or_404


class TestViews(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        ProfService = PServices.objects.create(
            name="test", description="testing", author_id=user.id)

    def test_get_ProfService_page(self):
        page = self.client.get("/ProfessionalServices/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "ProfessionalServices.html")

    def test_get_completed_ProfService_page(self):
        page = self.client.get("/ProfessionalServices/completed_ProfessionalServices")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "completed_ProfessionalServices.html")

    def test_get_ProfService_details_page(self):
        user = User.objects.get(username="test")
        ProfService = PServices(
            name="Test title",
            description="Test description",
            author_id=user.id)
        ProfService.save()
        response = self.client.get('/ProfessionalServices/{}'.format(ProfService.id))
        self.assertEqual(response.status_code, 301)

    def test_get_add_ProfService_page(self):
        page = self.client.get("/ProfessionalServices/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_ProfService.html")

    def test_get_edit_ProfService_page(self):
        user = User.objects.get(username="test")
        ProfService = PServices(
            name="Create a Test",
            description="description",
            author_id=user.id)
        ProfService.save()

        page = self.client.get("/ProfessionalServices/{0}/edit/".format(ProfService.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_ProfService.html")

    def test_get_edit_page_for_ProfService_that_does_not_exist(self):
        page = self.client.get("/ProfessionalServices/100/edit/")
        self.assertEqual(page.status_code, 404)

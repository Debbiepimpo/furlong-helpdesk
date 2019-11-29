from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Hour, HourComment
from django.shortcuts import get_object_or_404


class TestViews(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        hour = Hour.objects.create(
            name="test",
            description="testing",
            author_id=user.id)

    def test_get_hours_page(self):
        page = self.client.get("/view_hours/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "hours.html")

    def test_get_hours_complete_page(self):
        page = self.client.get("/view_hours/complete_hours")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "completed_hours.html")

    def test_get_hour_details_page(self):
        user = User.objects.get(username="test")
        hour = Hour(
            name="Test title",
            description="Test description",
            author_id=user.id)
        hour.save()
        response = self.client.get('/view_hours/{0}/'.format(hour.id))
        self.assertEqual(response.status_code, 200)

    def test_get_add_hour_page(self):
        page = self.client.get("/view_hours/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_hour.html")

    def test_get_edit_hour_page(self):
        user = User.objects.get(username="test")
        hour = Hour(name="Create a Test", description="description", author_id=user.id)
        hour.save()

        page = self.client.get("/view_hours/{0}/edit/".format(hour.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_hour.html")

    def test_get_edit_page_for_hour_that_does_not_exist(self):
        page = self.client.get("/view_hours/100/edit/")
        self.assertEqual(page.status_code, 404)

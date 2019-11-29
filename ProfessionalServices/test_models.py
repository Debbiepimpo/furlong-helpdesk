from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import PServices, PServices_Bought


class TestPServicesModel(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        ProfService = PServices.objects.create(
            name="test", description="testing", author_id=user.id)

    def test_desc_defaults_to_False(self):
        user = User.objects.get(username="test")
        ProfService = PServices(name="Create a Test", author_id=user.id)
        ProfService.save()
        self.assertEqual(ProfService.name, "Create a Test")
        self.assertFalse(ProfService.description)

    def test_can_create_a_ProfService_with_a_name_and_desc(self):
        user = User.objects.get(username="test")
        ProfService = PServices(name="Create a Test", description=True, author_id=user.id)
        ProfService.save()
        self.assertEqual(ProfService.name, "Create a Test")
        self.assertTrue(ProfService.description)

    def test_name_str(self):
        test_name = PServices(name="A test Professional Service")
        self.assertEqual(str(test_name), "A test Professional Service")


class TestPServicesCommentModel(TestCase):

    def test_comment_str(self):
        test_comment = PServices_Bought(comment="A test comment")
        self.assertEqual(str(test_comment), "A test comment")

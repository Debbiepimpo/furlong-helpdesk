from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Hour, HourComment


class TestHourModel(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        hour = Hour.objects.create(
            name="test",
            description="testing",
            author_id=user.id)

    def test_desc_defaults_to_False(self):
        user = User.objects.get(username="test")
        hour = Hour(name="Create a Test", author_id=user.id)
        hour.save()
        self.assertEqual(hour.name, "Create a Test")
        self.assertFalse(hour.description)

    def test_can_create_a_hour_with_a_name_and_desc(self):
        user = User.objects.get(username="test")
        hour = Hour(name="Create a Test", description=True, author_id=user.id)
        hour.save()
        self.assertEqual(hour.name, "Create a Test")
        self.assertTrue(hour.description)

    def test_name_str(self):
        test_name = Hour(name="A test hour")
        self.assertEqual(str(test_name), "A test hour")


class TestHourCommentModel(TestCase):

    def test_comment_str(self):
        test_comment = HourComment(comment="A test description")
        self.assertEqual(str(test_comment), "A test description")

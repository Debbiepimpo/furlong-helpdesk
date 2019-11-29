from django.test import TestCase
from .forms import CreateHourForm, HourCommentForm



class TestHourForm(TestCase):

    def test_can_create_a_hour_with_name_and_description(self):
        form = CreateHourForm({'name': 'Tests', 'description': "create a test"})
        self.assertTrue(form.is_valid())

    def test_cannot_create_a_hour_without_required_values(self):
        form = CreateHourForm({'name': 'Test'})
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = CreateHourForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])

    def test_correct_message_for_missing_desc(self):
        form = CreateHourForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])


class TestHourCommentForm(TestCase):

    def test_can_create_a_comment_with_required_values(self):
        form = HourCommentForm({'comment': "comment"})
        self.assertTrue(form.is_valid())

    def test_cannot_post_blank_comment(self):
        form = HourCommentForm({'comment': ''})
        self.assertFalse(form.is_valid())

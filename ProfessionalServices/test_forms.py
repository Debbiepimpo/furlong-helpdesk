from django.test import TestCase
from .forms import CreatePServicesForm, PServicesCommentForm

# Create your tests here.


class TestPServicesForm(TestCase):

    def test_can_create_a_ProfService_with_name_and_description(self):
        form = CreatePServicesForm({'name': 'Tests', 'description': "create a test"})
        self.assertTrue(form.is_valid())

    def test_cannot_create_a_ProfService_without_required_values(self):
        form = CreatePServicesForm({'name': 'Test'})
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = CreatePServicesForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])

    def test_correct_message_for_missing_desc(self):
        form = CreatePServicesForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])


class TestPServicesCommentForm(TestCase):

    def test_can_create_a_comment_with_required_values(self):
        form = PServicesCommentForm({'comment': "comment"})
        self.assertTrue(form.is_valid())

    def test_cannot_post_blank_comment(self):
        form = PServicesCommentForm({'comment': ''})
        self.assertFalse(form.is_valid())

from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm


# Create your tests here.
class TestUserLoginForm(TestCase):

    def test_can_create_a_user_with_username_and_password(self):
        form = UserLoginForm({'username': 'Tests',
                              'password': "create a test"})
        self.assertTrue(form.is_valid())

    def test_cannot_create_a_user_without_required_values(self):
        form = UserLoginForm({'username': 'Test'})
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_correct_message_for_missing_password(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])


class TestUserRegistrationForm(TestCase):

    def test_can_create_a_user_with_required_values(self):
        form = UserRegistrationForm({'username': 'test',
                                     'email': 'test@admin.com',
                                     'password1': 'testpassword',
                                     'password2': 'testpassword'})
        self.assertTrue(form.is_valid())

    def test_cannot_create_a_user_without_matching_passwords(self):
        form = UserRegistrationForm({'username': 'test',
                                     'email': 'test@admin.com',
                                     'password1': 'testpassword',
                                     'password2': 'testpasswor'})
        self.assertFalse(form.is_valid())

    def test_cannot_register_a_user_without_required_values(self):
        form = UserLoginForm({'username': 'Test'})
        self.assertFalse(form.is_valid())

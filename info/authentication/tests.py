from django.test import TestCase
from .form import LoginForm,UserRegisterForm


class AccountTestCase(TestCase):
    def test_login_form(self):
        form = LoginForm(data={
            'username': 'tester',
            'password': 'cevaparola1'
        })
        self.assertTrue(form.is_valid())

    def test_user_registration_invalid_form(self):
        form = UserRegisterForm(data={
            'username': 'cevaaa',
            'password': 'cevaparola1',
            'retypepassword': 'cevaparola',
            'email': 'email@email.com',
            'first_name': 'temian',
            'last_name': 'pisica'
        })
        self.assertFalse(form.is_valid())
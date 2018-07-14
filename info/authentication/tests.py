from django.test import TestCase
from .models import Account, Account2
from django.contrib.auth.models import User
from .form import LoginForm,UserRegisterForm,AccRegisterForm,AccRegisterForm2
# Create your tests here.
class AccountTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="tester",
                            email="tester@tester.com",
                            password='cevaparola1')

    def test_login_form(self):
        form_data = {'username': 'tester', 'password': 'cevaparola1'}
        formular = LoginForm(data=form_data)
        self.assertTrue(formular.is_valid())

    def test_userreg_invalid_form(self):
        form_data = {'username':'cevaaa', 'password':'cevaparola1',
                     'retypepassword':'cevaparola', 'email':'email@email.com',
                     'first_name':'temian', 'last_name':'pisica'}
        formular = UserRegisterForm(data=form_data)
        self.assertFalse(formular.is_valid())
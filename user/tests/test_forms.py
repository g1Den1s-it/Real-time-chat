from django.test import TestCase, Client
from django.urls import reverse

from user.forms import LoginForm, RegisterForm

class TestRegisterForm(TestCase):

    def test_form_valid_data(self):
        form = RegisterForm(data={
            'username': 'den',
            'tag': '@den',
            'email': 'den.test@gmail.com',
            'password1': 'Q1w2e3r4t5y6_',
            'password2': 'Q1w2e3r4t5y6_'
        })

        self.assertTrue(form.is_valid())

    def test_form_not_valid_data(self):
        form = RegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)


class TestLoginForm(TestCase):

    def test_form_valid_data(self):
        form = LoginForm(data={
            'tag': '@den',
            'password': 'Q1w2e3r4t5y6_'
        })

        self.assertTrue(form.is_valid())

    def test_form_not_valid_data(self):
        form = LoginForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
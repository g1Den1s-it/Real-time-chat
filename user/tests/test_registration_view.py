from django.test import TestCase, Client
from django.urls import reverse

from user.forms import RegisterForm
# Create your tests here.

class TestRegistrationView(TestCase):

    def setUp(self):
        self.client = Client()
        self.sign_up_url = reverse("sign-up")

    def test_GET(self):
        response = self.client.get(self.sign_up_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "login/sign-up.html")

    def test_POST(self):
        form = RegisterForm(data={
            'username': 'den',
            'tag': 'den',
            'email': 'den.test@gmail.com',
            'password1': 'Q1w2e3r4t5y6_',
            'password2': 'Q1w2e3r4t5y6_'
        })

        response = self.client.post(self.sign_up_url, data=form.data)
        
        self.assertTrue(form.is_valid())
        self.assertEquals(response.status_code, 302)
        
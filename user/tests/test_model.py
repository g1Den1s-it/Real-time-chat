from django.test import TestCase, Client
from django.urls import reverse

from user.models import User


class TestUserModel(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(
            username = 'Den1s',
            tag = 'Den1s',
            password = 'Q1w2e3r4t5y6_'
        )
    
    def test_user_is_add_symbol(self):
        self.assertEquals(self.new_user.tag, '@Den1s')
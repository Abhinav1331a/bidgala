from django.test import TestCase, Client
from django.urls import reverse

from accounts.views import register, login
from accounts.models import UserInfo


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.register_url = reverse('register')

	def test_register_GET(self):
		response = self.client.get(self.register_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'accounts/register.html')
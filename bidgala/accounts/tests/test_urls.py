from django.test import SimpleTestCase
from django.urls import resolve, reverse


from accounts.views import register, login

class TestUrls(SimpleTestCase):

	def test_register_url_is_resolved(self):
		url = reverse('register')
		self.assertEquals(resolve(url).func, register)
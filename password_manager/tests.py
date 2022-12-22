from django.test import TestCase

# Create your tests here.
from django.urls import reverse, resolve

from password_manager.views import home_page


class HomeTests(TestCase):

    def home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response, 200)

    def home_page_resolves_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home_page)


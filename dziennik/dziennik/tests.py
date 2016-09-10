from django.test import TestCase
from django.test import Client


class TemplateViewTest(TestCase):

    def __init__():
        self.client = Client()

class TemplateViewTest(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "index.html")
        self.assertView('index')

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

#from superlists.lists.views import home_page

class SampleTest(TestCase):
    pass
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)
    #
    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     self.assertTrue(response.content.startswith(b'<html>'))
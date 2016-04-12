from django.test import TestCase
from django.core.urlresolvers import resolve
from inventory.views import inventory_index_page
# Create your tests here.
class HomePageTest(TestCase):

	def test_root_url_resolves_to_index_page(self):
		found =resolve('/inventory/')
		self.assertEqual(found.func, inventory_index_page)
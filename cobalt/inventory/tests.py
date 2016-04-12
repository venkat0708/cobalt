from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from inventory.views import inventory_index_page
# Create your tests here.
class InventoryTest(TestCase):

	def test_inventory_index_url_resolves_to_inventory_index_page(self):
		found =resolve('/inventory/')
		self.assertEqual(found.func, inventory_index_page)
		
	def test_inventory_index_page_returns_correct_html(self):
		request = HttpRequest()
		response = inventory_index_page(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>Inventory list</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))
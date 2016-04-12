from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from inventory.views import inventory_index_page, inventory_add_new_product
# Create your tests here.
class InventoryIndexTest(TestCase):

	def test_inventory_index_url_resolves_to_inventory_index_page(self):
		found =resolve('/inventory/')
		self.assertEqual(found.func, inventory_index_page)
		
	def test_inventory_index_page_returns_correct_html(self):
		request = HttpRequest()
		response = inventory_index_page(request)
		expected_html = render_to_string('inventory/inventory_index.html')
		self.assertEqual(response.content.decode(), expected_html)
		
class InventoryNewProductTest(TestCase):
	
	def test_inventory_new_url_resolves_to_inventory_add_new_product(self):
		found = resolve('/inventory/new/')
		self.assertEqual(found.func, inventory_add_new_product)
		
	def test_inventory_add_new_product_returns_correct_html(self):
		request = HttpRequest()
		response = inventory_add_new_product(request)
		expected_html = render_to_string('inventory/add_product.html')
		self.assertEqual(response.content.decode(), expected_html)
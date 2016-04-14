from django.test import TestCase
from django.shortcuts import render
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string, get_template

from inventory.views import (inventory_index_page, 
								inventory_add_new_product,
								inventory_add_units)
from inventory.forms import NewProductForm
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
		template = get_template('inventory/add_product.html')
		product_form = NewProductForm()
		expected_html = template.render({'product_form': product_form}, request)
		self.assertEqual(response.content.decode(), expected_html)
		
class InventoryExistingProductTest(TestCase):

	def test_inventory_add_units_to_product_resolves_to_inventory_add_units(self):
		found = resolve('/inventory/add/')
		self.assertEqual(found.func, inventory_add_units)
		
	def test_inventory_add_units_to_product_returns_correct_html(self):
		request = HttpRequest()
		response = inventory_add_units(request)
		template = get_template('inventory/add_units.html')
		change_form = ChangeUnitsForm()
		expected_html = template.render({'change_form': change_form}, request)
		self.assertEqual(response.content.decode(), expected_html)
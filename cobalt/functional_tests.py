from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	def tearDown(self):
		self.browser.implicitly_wait(3)
		self.browser.quit()
		
	def test_can_visit_home_page(self):
		
		self.browser.get('http://localhost:8000/inventory/')
		
		self.assertIn('list of products', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('List of products', header_text)
		#self.fail('finish the test')
	
	def test_adding_new_product(self):
		self.browser.get('http://localhost:8000/inventory/new')
		self.assertIn('Adding new product', self.browser.title)
		
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Add a new product', header_text)
		
		name = self.browser.find_element_by_id('id_name')
		company = self.browser.find_element_by_id('id_company')
		price = self.browser.find_element_by_id('id_price')
		total = self.browser.find_element_by_id('id_total_units')
		consumed = self.browser.find_element_by_id('id_consumed_units')
		minimum = self.browser.find_element_by_id('id_minimum_units_to_be_maintained')
		
		name.send_keys('DVD')
		company.send_keys('Sony')
		price.send_keys(40)
		total.send_keys(100)
		consumed.send_keys(50)
		minimum.send_keys(30)
		minimum.send_keys(Keys.ENTER)
		
		self.browser.implicitly_wait(20)
		self.browser.get('http://localhost:8000/inventory/')
		
		table = self.browser.find_element_by_id('list')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('DVD Sony 40.0000 100 50 30',[row.text for row in rows])
		
		
		
if __name__=='__main__':
	unittest.main()

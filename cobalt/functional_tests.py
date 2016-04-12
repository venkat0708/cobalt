from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	def tearDown(self):
		self.browser.implicitly_wait(3)
		self.browser.quit()
		
	def test_can_visit_home_page(self):
		
		self.browser.get('http://localhost:8000/inventory/')
		
		self.assertIn('Inventory list', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('List of products', header_text)
		#self.fail('finish the test')
	
if __name__=='__main__':
	unittest.main()

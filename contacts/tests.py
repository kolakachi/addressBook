from django.test import TestCase, Client

from .models import contact


class contactTestCase(TestCase):

	def test_home_page_status_code(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_list_page_status_code(self):
		client = Client()
		response = client.get('/list')
		self.assertEqual(response.status_code, 200)

	def test_add_page_status_code(self):
		client = Client()
		response = client.get('/add')
		self.assertEqual(response.status_code, 200)

	def test_addanewcontact_status_code(self):
		client = Client()
		response = client.post('/addanewcontact',{'Name' :'Contact','Email':'Contact@gmail.com'})
		self.assertEqual(response.status_code, 302)

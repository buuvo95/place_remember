from unittest import skip
from django.http import response, HttpResponse

from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from .models import Memory
from .views import home_view

class TestViewResponse(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('username','username@email.com', 'userpassword')
        self.memory_1 = Memory.objects.create(
            name = 'TestName',
            address = 'TestAddress',
            comment = 'TestComment',
            user = self.user
        )
        self.memory_2 = Memory.objects.create(
            name = 'TestName_2',
            address = 'TestAddress_2',
            comment = 'TestComment_2',
            user = self.user
        )
    
    def test_create_func(self):
        """
        Test create function
        """
        memory = Memory.objects.get(id=1)
        self.assertEqual(memory.name, 'TestName')
        memory_2 = Memory.objects.get(id=2)
        self.assertEqual(memory_2.name, 'TestName_2')

    # def test_url_allowed_hosts(self):
    #     """
    #     Test allowed hosts
    #     """
    #     response = self.c.get('/')
    #     self.assertEqual(response.status_code,200)
       
    def test_homepage_html_notauth(self):
        """
        Test homepage without login
        """
        response = self.c.get('/app/')
        request = response.wsgi_request
        response = home_view(request)
        html = response.content.decode('utf8')
        
        self.assertIn('<title>Place Remember</title>', html)
        self.assertIn('Login', html)
        self.assertEqual(response.status_code,200)
    
    def test_homepage_html_auth(self):
        """
        Test homepage with authentication
        """
        response = self.c.get('/app/')
        request = response.wsgi_request
        request.user = self.user
        response = home_view(request)
        html = response.content.decode('utf8')
       
        self.assertIn('username', html)
        self.assertIn('TestName', html)
        self.assertEqual(response.status_code,200)
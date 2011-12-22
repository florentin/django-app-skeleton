import sys
from random import choice
from pprint import pprint
from django.utils import unittest
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.utils import simplejson

class MyTests(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_unauthenticated_requests(self):
        c = Client()
        self.assertEqual(1, 2)

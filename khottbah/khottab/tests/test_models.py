
"""
Testing List:
 - Imam Model:
    - first_name max_length []
    - middel_name max_length []
    - last_name max_length []
    - nationality max_length []
    - __str__ []
    - get_abolute_url []
    
 - Khottbah Model:
    - title max_length []
    - mosque max_length []
    - resources max_length []
    - language max_length []
    - language help_text [] ---> 'The kottbah Language'
    - language is one of laguages [] ---> ['arb', 'eng', 'ord']
    - language default is arb []
    - __str__ []
    - get_absolute_url []
"""
from django.test import TestCase
from khottab.models import Imam, Khottbah

class TestImam(TestCase):
    @classmethod
    def setUpTestData(cls):
        imam = Imam.objects.create(first_name = 'mohammed', middel_name = 'Saleh', last_name = 'Al-ghanmi', nationality = 'Saudi Arabian')
    
    
    # Check if the name length is within the range
    def name_within_the_range(self,name_length, range):
            if name_length > range:
                return False
            return True
         
         
    def test_first_name_max_length(self):
        imam = Imam.objects.get(id = 1)
        max_length = imam._meta.get_field('first_name').max_length
        
        # Check if the input name is within the range
        self.assertTrue(self.name_within_the_range(max_length, 15))    
        
        # Check if the max_length is working as it should be.      
        self.assertEqual(max_length, 15)

    def test_middel_name_max_length(self):
        imam = Imam.objects.get(id = 1)
        max_length = imam._meta.get_field('middel_name').max_length
        
        # Check if the input name is within the range
        self.assertTrue(self.name_within_the_range(max_length, 15))    
        
        # Check if the max_length is working as it should be.      
        self.assertEqual(max_length, 15)
    
    def test_last_name_max_length(self):
        imam = Imam.objects.get(id = 1)
        max_length = imam._meta.get_field('last_name').max_length
        
        # Check if the input name is within the range
        self.assertTrue(self.name_within_the_range(max_length, 15))    
        
        # Check if the max_length is working as it should be.      
        self.assertEqual(max_length, 15)
        
    def test_nationalty_max_length(self):
        imam = Imam.objects.get(id = 1)
        max_length = imam._meta.get_field('nationality').max_length
        
        # Check if the input name is within the range
        self.assertTrue(self.name_within_the_range(max_length, 15))    
        
        # Check if the max_length is working as it should be.      
        self.assertEqual(max_length, 15)   
        
class TestKhottbah(TestCase):
    @classmethod
    def setUpTestData(cls):
        khottbah = Khottbah.objects.create()
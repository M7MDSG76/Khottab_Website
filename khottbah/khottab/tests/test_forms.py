from django.forms import ValidationError
from django.test import SimpleTestCase
from khottab.forms import (KhottbahEditeModelForm, check_bad_words,
                           check_sympols, split_word)

"""
Testing List:

 - Metods
    - split_word() [Ok]
    - check_bad_words() [Ok]
    - check_sympols() [Ok]
    
 - Forms
    - title max_length [Ok]
    - title label [Ok]
    - title help_text [Ok]
    - content max_length [Ok]
    - content label [Ok]
    - content help_text [Ok]
"""

# Methods
class TestKhottbahFormMethods(SimpleTestCase):
    
    bad_words = bad_words = ['bad', 'faminest']
    sentance = 'This sentance is for testing'
    def test_split_word(self):
        sentance = 'This sentance is for testing'
        splited_sentance = ['This', 'sentance', 'is', 'for', 'testing']
        
        # Check if the first input is equal to the seconde input.
        self.assertEqual(split_word(sentance), splited_sentance)
    
    def test_check_bad_words(self):
        
        sentance = 'there is allot of faminest there'
        
        # check if ValidationError accure.
        with self.assertRaises(ValidationError):
            check_bad_words(sentance)
            
    def test_check_sympols(self):
        sentance = 'this sentance to _test") if check& symp$ls working'
        
        with self.assertRaises(ValidationError):
            check_sympols(sentance)
  
  
    
class TestKhottbahForm(SimpleTestCase):
    
    def test_title_max_length(self):
        title = 'this title is equal to 50 characters bla blaa blaa'
        form = KhottbahEditeModelForm(data = {'title': title})
        self.assertTrue(form.is_valid)
    
    def test_title_label(self):       
        form = KhottbahEditeModelForm()
        title_label = form.fields['title'].label
        self.assertEqual(title_label, 'Khottbah Title')
        
    def test_title_help_text(self):
        form = KhottbahEditeModelForm()
        help_text = form.fields['title'].help_text
        
        self.assertEqual(help_text, 'Write the Title of the khottbah' )
    
    
    def test_content_max_length(self):
        content = 'this title is equal to 30 char'
        form = KhottbahEditeModelForm(data= {'content': content})
        self.assertTrue(form.is_valid)
    
    def test_content_label(self):
        form = KhottbahEditeModelForm()
        content_label = form.fields['content'].label
        self.assertEqual(content_label, 'Khottbah') 
        
    def test_content_help_text(self):
        form = KhottbahEditeModelForm()
        content_help_text = form.fields['content'].help_text
        self.assertEqual(content_help_text, 'Write the Khottbah Here')
           
    
        
    
            
    
        


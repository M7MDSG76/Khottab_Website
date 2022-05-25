from asyncio.windows_events import NULL
from dataclasses import fields
from posixpath import split

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import *


def split_word(string):
    """
    just normal spliting but insted of declaring string and then split it you just use split_word().
    """
    temp_str = string.split(' ')
    
    return temp_str


def check_bad_words(input):
    """
    Filtering content is very important,
    
    this method check if there are any bad words. 
    """
    
    bad_words = ['bad', 'faminest']
    words_list = split_word(input)
    for word in words_list:
        for bad_word in bad_words:
            if word == bad_word:
                
                raise ValidationError(_(f'{word} is a bad word change it with a good one!'))
            
            
def check_sympols(input):
    """ 
    Some fields cannot contain symplos, This method check if the input contain any sympols.
    """
    
    sympols = ['~','`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '<',
               '>', ',', '.', '?', '/', '\\', '|', '[', ']', '{', '}', ';', "'", '"', ':', '_']
   # Loop within input range
    for char in range(len(input)):   
        # Iterate over sympols   
        for sympol in sympols:
            #Check if char in input equals the iterated sympol rais a VError.
            if input[char] == sympol:
               
                raise ValidationError(_(f'input cannot contain sympols! Please enter another input'))
            
        
class KhottbahEditeModelForm(forms.ModelForm):
    
    
    def clean_title(self):
        
        data = self.cleaned_data['title']
        
        check_bad_words(data)
        
        return data
    
    def clean_content(self):
        data = self.cleaned_data['content']

        # Check if khottbah characters is within the limits.
        if len(data) > 30:
            raise ValidationError(_('Khottbah is too long (Limit is 30 characters)'))
        
        # Check if khottbah contains Bad words.
        check_bad_words(data)
        
        return data
    
    class Meta:
        model = Khottbah
        fields = ['title', 'content']
        labels = {'title': _('Khottbah Title'), 'content': _('Khottbah')}
        help_texts = {'title': _('Write the Title of the khottbah'), 'content': _('Write the Khottbah Here')}
        
        
class ImamCreateForm(forms.Form):
    first_name = forms.CharField(max_length=40)
    middle_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    nationality = forms.CharField(max_length=50)
    
    
    
    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        
        check_sympols(data)
        check_bad_words(data)
                
        return data
    
    def clean_middle_name(self):
        data = self.cleaned_data['middle_name']
        
        check_sympols(data)
        check_bad_words(data)
                
        return data
    
    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        
        check_sympols(data)
        check_bad_words(data)
                
        return data
    
    def clean_nationality(self):
        data = self.cleaned_data['nationality']
        
        check_sympols(data)
        check_bad_words(data)
                
        return data
    
    
    
    
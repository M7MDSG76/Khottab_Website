from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from datetime import datetime 

from django.contrib.auth.models import User


class Imam(models.Model):
    
    first_name = models.CharField(max_length=40) 
    
    middel_name = models.CharField(max_length=30, blank = True,
                                   null= True)
    
    last_name = models.CharField(max_length=30, blank = True,
                                   null= True)
    
    nationality = models.CharField(max_length=50, blank=True,
                                   null=True)
    
    user = models.ForeignKey(User ,on_delete= models.SET_NULL, null=True, blank=True)
    
    
    class Meta:
        ordering = ['nationality']
        permissions = (('can_view', 'view'),)
        
        
    def __str__(self):
     return self.first_name   
 
    def get_abslute_url(self):
        return reverse('imam-detail', args=[str(self.id)])
    
    
class Khottbah(models.Model):
    LANGUAGES = (
        ('ara', 'Arabic'),
        ('eng', 'English'),
        ('ord', 'Ordo')
    )
    title = models.CharField(max_length=50 )
    
    content = models.TextField()
    
    imam = models.ForeignKey(Imam, on_delete= models.SET_NULL, blank=True, null= True)
    
    mosque = models.CharField(max_length=50, blank=True, null = True)
    
    time = models.DateTimeField(default= datetime.now, blank=True)
    
    resources = models.TextField(max_length=2000,null= True, blank=True)
    
    language = models.CharField(max_length=3, choices=LANGUAGES,
                                default='ara', help_text='The kottbah Language',
                                blank=True)
    
    def __str__(self):
        return self.title

    def get_abslute_url(self):
        return reverse('khottbah-detail', args=[str(self.id)]) 
    
    

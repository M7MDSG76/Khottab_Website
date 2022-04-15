from django.contrib import admin
from .models import *
# Register your models here.

class KhottbahInline(admin.TabularInline):
    model = Khottbah
    
    
@admin.register(Imam)
class ImamAdmin(admin.ModelAdmin):
    # list display is what data will showup in the admin list view model page.
    list_display = ('first_name', 'last_name', 'nationality')
    
    # setup the filter settings for the model in the admin view.
    list_filter = ('first_name', 'nationality')
    
    fieldsets = (
        ('Name', {'fields': ('first_name', 'middel_name', 'last_name', 'user')}),
        ('Nationality', {'fields':('nationality',)})
    )
    inlines = [KhottbahInline]
    
    
@admin.register(Khottbah)
class KhottbahAdmin(admin.ModelAdmin):
    list_display = ('title', 'imam', 'mosque', 'language')
    list_filter = ('imam', 'mosque', 'time', 'language')
    
    
    
    
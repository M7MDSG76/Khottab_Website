from django.urls import path, include
from khottab import views


urlpatterns = [
    path('',views.index, name = 'index'),
    path('imams/', views.ImamListView.as_view(), name='imam-list'),
    path('khottabs/', views.KhottabListView.as_view(), name = 'khottab-list'),
    path('imam/<int:pk>', views.ImamDetailView.as_view(), name = 'imam-detail'),
    path('khottbah/<int:pk>', views.KhottbahDetailView.as_view(), name = 'khottbah-detail'),
    
    #Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('khottbah/<int:pk>/edite/', views.khottbah_edite_Imam, name='khottbah-edite'),
    
    # view Imam profile 
    path('imam/<int:pk>/profile', views.ImamProfile.as_view(), name= 'imam-profile'),
    
    # Imam Edite urls
    path('imam/create', views.imam_create_Imam, name= 'imam-create'),
    
    
    
    
    
    
    
]
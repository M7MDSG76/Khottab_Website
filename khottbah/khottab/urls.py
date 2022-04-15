from django.urls import path, include
from khottab import views


urlpatterns = [
    path('',views.index, name = 'index'),
    path('imams/', views.ImamListView.as_view(), name='imam_list'),
    path('khottabs/', views.KhottabListView.as_view(), name = 'khottab_list'),
    path('imam/<int:pk>', views.ImamDetailView.as_view(), name = 'imam-detail'),
    path('khottbah/<int:pk>', views.KhottbahDetailView.as_view(), name = 'khottbah-detail'),
    
    #Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
    
    
    
    
]
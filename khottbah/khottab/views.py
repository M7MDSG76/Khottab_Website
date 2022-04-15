from multiprocessing import context
from urllib import request
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.contrib.auth.models import User



def index(request):
    
    return render(request, 'gen_base.html')


class ImamListView( ListView):
    model = Imam
    template_name = 'imam/imam_list.html'
    context_object_name = 'imams'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super(ImamListView, self).get_context_data(**kwargs)
        context.update({
                'num_visits' : self.request.session['num_visits']  
            })
        return context
    
    def get(self, *args, **kwargs):
        num_visits = self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = num_visits + 1
        
        return super().get(self.request, *args, **kwargs)
    
    
class KhottabListView(ListView):
    model = Khottbah
    template_name = 'khottbah/khottbah_list.html'
    context_object_name = 'khottab'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super(KhottabListView, self).get_context_data(**kwargs)
        context.update({
                'num_visits' : self.request.session['num_visits']
            })
        return context
    
    def get(self, *args, **kwargs):
        num_visits = self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = num_visits + 1
        return super().get(self.request, *args, **kwargs)
   
    
class ImamDetailView(PermissionRequiredMixin,LoginRequiredMixin, DetailView):
    model = Imam
    template_name = 'imam/imam_detail.html'
    permission_required  = 'khottab.can_view'
       
    def get_queryset(self):
        return Imam.objects.filter(user=self.request.user)
        
    def get_context_data(self, **kwargs):
        context = super(ImamDetailView, self).get_context_data(**kwargs)
        context.update({
                'num_visits' : self.request.session['num_visits']
            })
        return context
    
    def get(self, *args, **kwargs):
        num_visits = self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = num_visits + 1
        return super().get(self.request, *args, **kwargs)
  
    
class KhottbahDetailView(DetailView):
    model = Khottbah
    template_name = 'khottbah/khottbah_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(KhottbahDetailView, self).get_context_data(**kwargs)
        context.update({
                'num_visits' : self.request.session['num_visits']
            })
        return context
    
    def get(self, *args, **kwargs):
        num_visits = self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = num_visits + 1
        return super().get(self.request, *args, **kwargs)
    
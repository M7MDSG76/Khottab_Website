from multiprocessing import context
from urllib import request
import uuid
from xml.dom import ValidationErr
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ImamCreateForm
from .models import *
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from khottab.forms import KhottbahEditeModelForm

# acceess and login decorators
from django.contrib.auth.decorators import login_required, permission_required

# Exeption Handeling 
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



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
       
    # def get_queryset(self):
        # return Imam.objects.filter(id=)
        
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


@login_required
@permission_required('khottab.can_edite_khottbah')
def khottbah_edite_Imam(request, pk):
    
    khottbah = get_object_or_404(Khottbah, pk = pk)
    
    if request.method == 'POST':
        
        form = KhottbahEditeModelForm(request.POST)
        
        if form.is_valid():
            khottbah.content = form.cleaned_data['content']
            khottbah.title = form.cleaned_data['title']
            khottbah.save()
            return HttpResponseRedirect(reverse('khottab-list'))
        
        context = {
            'form': form,
            'khottbah': khottbah 
        }
        return render(request, 'khottbah/khottbah_edite.html', context)
    
    else:
        
        form = KhottbahEditeModelForm(initial={'title': khottbah.title, 'content': khottbah.content})
        
        context = {
            'form': form,
            'khottbah': khottbah 
        }
        return render(request, 'khottbah/khottbah_edite.html', context)



def imam_create_Imam(request):
    
    if request.method == 'POST':
        
        form = ImamCreateForm(request.POST)
        
        if form.is_valid():
            current_user = request.user
            print(f'current user: {current_user}, id: {current_user.id}')
            if Imam.objects.filter(user = current_user):
                return HttpResponse('<h1>This account is Already registerd, Pleas try agin with another account!!!</h1>')            
            imam = Imam( first_name = form.cleaned_data['first_name'], middel_name = form.cleaned_data['middle_name'], 
                        last_name = form.cleaned_data['last_name'], nationality = form.cleaned_data['nationality'],
                        user = current_user)
            imam.save()
            
            return HttpResponseRedirect(reverse('imam-list'))
        
        context = {
            'form': form,
        }            
        return render(request, 'imam/create_imam_form.html', context)
    
    # if first load for the form (request == GET || request == else.)
    else:
        form = ImamCreateForm(initial={'first_name': 'mohammed', 'last_name': 'Al-Ghanmi', 'nationality' : 'Saudi Arabian'})
        
        context = {
            'form': form
        }
        return render(request, 'imam/create_imam_form.html', context)
    
    
        
class ImamProfile(DetailView):
    model = Imam
    template_name = 'imam/imam_profile.html'
    
    def get_context_data(self, **kwargs):
        
        context = super(ImamProfile, self).get_context_data(**kwargs)
        context.update({
            'profile_visits': self.request.session['profile_visits'],
            
            # 'khottab': self.request.
        })
        print(f'----------{context}')
        return context
    
        
    def get(self, *args, **kwargs):
        num_visits = self.request.session.get('profile_visits', 0)
        self.request.session['profile_visits'] = num_visits + 1
        return super().get(self.request, *args, **kwargs)
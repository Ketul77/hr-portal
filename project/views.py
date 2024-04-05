from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .forms import CelebrationCreationForm, Celebration_participantsCreationForm, LeaveCreationForm, EmployeeCreationForm
from django.views.generic import ListView
from django.views.generic import UpdateView, DeleteView, DetailView
from .models import Celebration, Celebration_participants, Employee

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from .models import Celebration, Leave
from .forms import CelebrationCreationForm  
from django.views import View
from django.contrib.auth.views import LoginView 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Celebration
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, UpdateView, DeleteView




# Create your views here.


class CelebrationCreationView(CreateView):
    template_name = 'project/create.html'
    model= Celebration
    form_class = CelebrationCreationForm
    success_url = '/project/list'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class CelebrationListView(ListView):
    template_name = 'project/list.html'
    model= Celebration
    context_object_name = "celebrations"  


class CelebrationDeleteView(DeleteView):
    model=Celebration
    def get(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)
    success_url='/project/list/'

class CelebrationUpdateView(UpdateView):
    model=Celebration
    def get(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)
    success_url='/project/list/'


class CelebrationDetailView(DetailView):
    model = Celebration  
    template_name = 'project/detail.html'      
    success_url='/project/detail/'
    context_object_name = 'c'

class CelebrationUpdateView(UpdateView):
    model = Celebration 
    form_class = CelebrationCreationForm
    template_name = 'project/create.html'      
    success_url='/project/list/'
    
    
        

class Celebration_participantsCreationView(CreateView):
    template_name = 'project/participants_create.html'
    model= Celebration_participants
    form_class = Celebration_participantsCreationForm
    success_url = '/project/participants_list'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class Celebration_participantsListView(ListView):
    template_name = 'project/participants_list.html'
    model = Celebration_participants
    context_object_name = "celebrations"

class Celebration_participantsDeleteView(DeleteView):
    model= Celebration_participants
    def get(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)
    success_url='/project/participants_list/'


class Celebration_participantsDetailView(DetailView):
    model = Celebration_participants  
    template_name = 'project/pdetail.html'      
    success_url='/project/participantsdetail/'
    context_object_name = 'c'


class Celebration_participantsUpdateView(UpdateView):
    model=Celebration_participants  
    def get(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    success_url='/project/participants_list/'


class LeavecreationView(CreateView):
    template_name = 'project/leavecreate.html'
    model= Leave
    form_class = LeaveCreationForm
    success_url = '/project/leavelist'



    def form_valid(self, form):
         form.instance.user = self.request.user
         return super().form_valid(form)
    

class LeaveListView(ListView):
    template_name = 'project/leavelist.html'
    model = Leave
    context_object_name = "celebrations"



class LeaveDeleteView(DeleteView):
    model=Leave
    def get(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)
    success_url='/project/leavelist/'

class LeaveDetailView(DetailView):
    model = Leave 
    template_name = 'project/leavedetail.html'      
    success_url='/project/leavedetail/'
    context_object_name = 'c'

class LeaveUpdateView(UpdateView):
    model =Leave 
    form_class = LeaveCreationForm
    template_name = 'project/leavecreate.html'      
    success_url='/project/leavelist/'

class UpdateStatusView(View):

    def post(self, request, pk):
        leave = Leave.objects.get(id=pk)

        if leave.status == 'pending':
            leave.status = 'approved'
        elif leave.status == 'approved':
            leave.status = 'rejected'
        else:
             leave.status = 'pending'

        leave.save()
        
        return redirect(reverse('hr_dashboard'))
    

class EmployeeCreationView(CreateView):
    template_name = 'project/employeecreate.html'
    model= Employee
    form_class = EmployeeCreationForm
    success_url = '/project/employeelist'
   

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class EmployeeListView(ListView):
    template_name = 'project/employeelist.html'
    model = Employee
    context_object_name = "celebrations"



def employee_dashboard(request):
    # Fetch pending, approved, and rejected leaves
    pending_leaves = Leave.objects.filter(status='Pending')
    approved_leaves = Leave.objects.filter(status='Approved')
    rejected_leaves = Leave.objects.filter(status='Rejected')
    
    # Pass the lists to the template context
    return render(request, 'employee_dashboard.html', {
        'pending_leaves': pending_leaves,
        'approved_leaves': approved_leaves,
        'rejected_leaves': rejected_leaves,
    })



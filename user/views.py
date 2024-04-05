
from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .forms import HrCreationForm,EmployeeCreationForm
from django.contrib.auth.views import LoginView 
from django.views.generic import FormView, TemplateView,ListView


class HrRegisterView(CreateView):
    model = User
    form_class = HrCreationForm
    template_name = 'user/hr_register.html'
    success_url = '/user/login/'

class EmployeeRegisterView(CreateView): 
    model = User
    form_class = EmployeeCreationForm
    template_name = 'user/employee_register.html'
    success_url = '/user/login/'   
   


class UserLoginView(LoginView):  
    template_name = 'user/login.html'   
    model = User
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_employee:
                return '/user/employee_dashboard/'
            else:
                return '/user/hr_dashboard/'

class HrDashboardView(ListView):
    
    def get(self, request, *args, **kwargs):
       
        print("HrDashboardView")
      
        
        return render(request, 'user/hr_dashboard.html')
    
    
    template_name = 'user/hr_dashboard.html'

class EmployeeDashboardView(ListView):
    
    def get(self, request, *args, **kwargs):
       
        print("EmployeeDashboardView")
       
        
        return render(request, 'user/employee_dashboard.html')
    
    
    template_name = 'user/employee_dashboard.html'


    

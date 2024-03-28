from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.views.generic import FormView, TemplateView,ListView
from django.db import transaction

class HrCreationForm(UserCreationForm):
     class Meta(UserCreationForm.Meta):
         model = User
         fields = UserCreationForm.Meta.fields + ('is_hr',)
         fields = ('username','email','maritialstatus','dateofbirth','dateofjoining','contactnumber','password1','password2','age')
    
    
     @transaction.atomic
     def save(self):
         user = super().save(commit=False)
         user.is_hr = True
         user.save()
         return user


class EmployeeCreationForm(UserCreationForm):
     class Meta(UserCreationForm.Meta):
         model = User
         fields = ('username','email','maritialstatus','dateofbirth','dateofjoining','contactnumber','password1','password2','age')
        
     @transaction.atomic
     def save(self):
         user = super().save(commit=False)
         user.is_employee = True
         user.save()
         return user

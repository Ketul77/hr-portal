from django.contrib import admin
from django.urls import path, include
from .views import HrRegisterView,EmployeeRegisterView,UserLoginView
from django.contrib.auth.views import LogoutView
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [

path("hr_register/",HrRegisterView.as_view(),name="hr_register"),
path("employee_register/",EmployeeRegisterView.as_view(),name="employee_register"),
path("login/",UserLoginView.as_view(),name="login"),
path("logout/",LogoutView.as_view(),name="logout"),
path("hr_dashboard/",views.HrDashboardView.as_view(),name="hr_dashboard"),
path("employee_dashboard/",views.EmployeeDashboardView.as_view(),name="employee_dashboard"),
]
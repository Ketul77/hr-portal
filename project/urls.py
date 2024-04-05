from django.contrib import admin
from django.urls import path, include
from .views import*
from django.contrib.auth.views import LogoutView
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .import views


urlpatterns = [
    path("create/", CelebrationCreationView.as_view(), name="create" ),
    path("list/", CelebrationListView.as_view(), name="list"),  
    path("participants_create/", Celebration_participantsCreationView.as_view(), name="participants_create" ),
    path("participants_list/", Celebration_participantsListView.as_view(), name="participants_list"),
    path("leavelist/", LeaveListView.as_view(), name="leavelist"),
    path("leavecreate/", LeavecreationView.as_view(), name="leavecreate" ),
    path("leave_status_update/<int:pk>/", UpdateStatusView.as_view(), name="update_status" ),
    path("employeecreate/", EmployeeCreationView.as_view(), name="employeecreate" ),
    path("employeelist/", EmployeeListView.as_view(), name="employeelist" ),
    path("delete/<int:pk>/", CelebrationDeleteView.as_view(), name='delete'),   
    path("update/<int:pk>/", CelebrationUpdateView.as_view(), name='update'),  
    path("detail/<int:pk>/", CelebrationDetailView.as_view(), name='detail'),   
    path("leavesdelete/<int:pk>/", LeaveDeleteView.as_view(), name='leavesdelete'),
    path("leavesdetail/<int:pk>/", LeaveDetailView.as_view(), name='leavesdetail'),
    path("leavesupdate/<int:pk>/", LeaveUpdateView.as_view(), name='leavesupdate'),
    path("participantsdelete/<int:pk>/", Celebration_participantsDeleteView.as_view(), name='participantsdelete'),
    path("participantsdetail/<int:pk>/", Celebration_participantsDetailView.as_view(), name='participantsdetail'),
    path("participantsupdate/<int:pk>/", Celebration_participantsUpdateView.as_view(), name='participantsupdate'),
]

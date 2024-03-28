from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    maritialstatus = models.CharField(max_length=100)
    dateofjoining =  models.CharField(max_length=100)
    dateofbirth =  models.CharField(max_length=100)
    contactnumber =  models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True,blank=True)
    is_hr = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'user'




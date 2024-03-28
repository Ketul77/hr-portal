from django.db import models
from user.models import User
from django.contrib.auth import get_user_model
# from django.db import models
# from django.contrib.auth import user
#from django.contrib.auth.models import User


# Create your models here.

STATUS_CHOICES = [
    ("cleared", "Cleared"),
    ("uncleared" , "Uncleared"),
]

STATUS= [
    ("approved", "Approved"),
    ("pending" , "Pending"),
    ("rejected", "Rejected")
]

class  Celebration(models.Model):
    user  = models.ForeignKey("user" ,on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)
    
    class Meta:
        db_table = "Celebration"

    def  __str__ (self):
        return self.title


class  Celebration_participants(models.Model):
    user  = models.ForeignKey(User ,on_delete=models.CASCADE,null= True)
    # user = models.CharField(max_length=100)
    celebration_participants = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    celebration = models.ForeignKey("celebration" ,on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    class Meta:
        db_table = "Celebration_participants"

    def __str__(self):
        return self.name
    

    

class Leave(models.Model):
    user  = models.ForeignKey(User ,on_delete=models.CASCADE,null= True)
    # user  = models.ForeignKey("user" ,on_delete=models.CASCADE)
    leave = models.CharField(max_length=100)
    dates = models.DateField()
    status =  models.CharField(max_length=100, choices=STATUS, default = 'pending')
    reason = models.CharField(max_length=100)
   

class Meta:
        db_table = "Leave"


def  __str__ (self):
        return f"Leave for {self.user.username}"

    

class Employee(models.Model):
    user  = models.ForeignKey(User ,on_delete=models.CASCADE,null= True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # password = models.CharField(max_length=100)
    # department = models.CharField(max_length=100)
    maritialstatus = models.CharField(max_length=100)
    dateofjoining =  models.CharField(max_length=100)
    dateofbirth =  models.CharField(max_length=100)
    contactnumber =  models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True,blank=True)
    is_hr = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'Employee'
    

# class EmployeeSalary(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     base = models.FloatField(default=0)
#     ctc = models.FloatField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    


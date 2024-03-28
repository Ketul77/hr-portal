from django.contrib import admin
from .models import Celebration, Leave, Employee, Celebration_participants
# Register your models here

admin.site.register(Celebration)
admin.site.register(Celebration_participants)
admin.site.register(Leave)
admin.site.register(Employee)
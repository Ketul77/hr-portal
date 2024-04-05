from django  import forms 
from .models import Celebration, Celebration_participants, Leave, Employee


class CelebrationCreationForm(forms.ModelForm):
    class Meta:
        model = Celebration
        exclude = ['user']
        widgets = {
            'date' : forms.DateInput(attrs= {'type':'date'})
        }
        # fields  ='__all__'
        


class Celebration_participantsCreationForm(forms.ModelForm):
    class Meta:
        model = Celebration_participants
        exclude = ['user']



class LeaveCreationForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['leave', 'dates', 'reason', 'status']
        widgets = {
            'date' : forms.DateInput(attrs= {'type':'date'})
        }

        

class EmployeeCreationForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['user']



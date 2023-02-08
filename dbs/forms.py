

from django import forms 
from .models import Student

from django.forms import widgets


class Register(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ('firstname', 'lastname', 'gender', 'dob')
        widgets = {
            'dob': widgets.DateInput(attrs={'type:': 'date'}),
        }
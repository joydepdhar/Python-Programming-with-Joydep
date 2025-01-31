from django import forms
from .models import Student

from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'course']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name', 'required': True, 'pattern': '[A-Za-z ]{2,100}'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number', 'required': True, 'pattern': '\\d{10,15}'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course name', 'required': True}),
        }

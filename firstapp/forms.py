from dataclasses import fields
import imp
from pyexpat import model
from tkinter.ttk import Widget
from django import forms
from . models import Student ,Track
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password')

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('fname','lname','age','student_track')
        widgets={
            'fname':forms.TextInput(attrs={'placeholder':'example: nayra','class':'form-control'}),
            'lname':forms.TextInput(attrs={'placeholder':'example: elsalamoney','class':'form-control'}),
        }
class TrackForm(forms.ModelForm):
    class Meta: 
        model=Track
        fields=('track_name',)
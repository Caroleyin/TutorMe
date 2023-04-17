from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from tutorme.models import AppUser

class AddClass(forms.Form):
    class_name = forms.CharField(label='CS', max_length=100)
    class_num = forms.CharField(label='2150', max_length=10)

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = AppUser
        # fields = ['username','last_name', 'first_name', 'email', 'year', 'major', 'description','hourly_rate'] 
        fields = ['username','last_name', 'first_name', 'email', 'year', 'major', 'description'] 
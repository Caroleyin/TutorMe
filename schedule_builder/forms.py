from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from tutorme.models import AppUser


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = AppUser
        # fields = ['username','last_name', 'first_name', 'email', 'year', 'major', 'description','hourly_rate'] 
        fields = ['first_name', 'last_name', 'email', 'year', 'major', 'description', 'hourly_rate'] 

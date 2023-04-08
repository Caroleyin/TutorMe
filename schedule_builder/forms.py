from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from tutorme.models import TutorProfile, AppUser


class UserUpdateForm(forms.ModelForm):
   

    class Meta:
        model = AppUser
        fields = ['username','last_name', 'first_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = TutorProfile
        fields = ['hourly_rate']

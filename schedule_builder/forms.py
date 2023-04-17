from django import forms 
from tutorme.models import AppUser

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = AppUser
        fields = ['first_name', 'last_name', 'year', 'major', 'description','hourly_rate'] 
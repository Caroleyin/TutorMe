from allauth.socialaccount.forms import SignupForm
from django import forms

from .models import AppUser
from .models import StudentProfile
 
 
class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='Username')
    interests = forms.ChoiceField(
        choices= [('TUTOR','Tutor'), ('STUDENT', 'Student')],
        widget= forms.Select,
        required=True
    )
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        if self.cleaned_data.get('interests') == "TUTOR":
            user.is_student = False
            user.is_tutor = True
        else:
            user.is_student = True
            user.is_tutor = False
        user.save()
        return user

class ProfileForm(forms.ModelForm):
	class Meta: 
		model = StudentProfile
		fields = ('about', 'courses')
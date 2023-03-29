from django import forms 

class AddClass(forms.Form):
    class_name = forms.CharField(label='CS', max_length=100)
    class_num = forms.CharField(label='2150', max_length=10)
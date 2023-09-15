from django import forms
from . models import Information

class InformationForms(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['number','name','occupation','location','age','thumb']
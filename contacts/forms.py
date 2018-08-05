from django import forms
from .models import contact

class contactForm(forms.Form):
    Name = forms.CharField(label='Enter Name', max_length=30)
    Email = forms.EmailField(label='Enter Email', max_length=25)
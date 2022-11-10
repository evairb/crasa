from django import forms
from . import models
from django.contrib.auth.models import User




class AutoForm(forms.ModelForm):


  class Meta:
    model = User
    fields = ('is_active',)
   
  
  
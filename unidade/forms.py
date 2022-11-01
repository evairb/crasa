from django import forms
from django import forms
from . import models
from django.contrib.auth.models import User
from utils.validacpf import valida_cpf



class AutoForm(forms.ModelForm):


  class Meta:
    model = User
    fields = ('is_active',)
   
  
  
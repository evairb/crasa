from django import forms
from . import models
from django.contrib.auth.models import User
from usuario.models import Perfil




class AutoForm(forms.ModelForm):


  class Meta:
    model = User
    fields = ('is_active',)
    
class AutoPerfilForm(forms.ModelForm):


  class Meta:
    model = Perfil
    fields = ('nivel_acesso',)
   
  
  
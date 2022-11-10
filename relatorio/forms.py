from django import forms
from usuario import models
 



STATUS_CHOICES = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
        ('ambos', 'Ambos'),
    )
class RelatorioForm(forms.Form):
  status = forms.ChoiceField(choices = STATUS_CHOICES)  
  data_inicio = forms.DateField(required=False, label='Data inicio', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control", "type": "date"}))
  data_fim = forms.DateField(required=False, label='Data fim', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control", "type": "date"}))
  
  
class UnidadeForm(forms.ModelForm):
  class Meta:
    model = models.Formulario
    fields = ('unidade',)
  
  
   
  
  
 
from django import forms
from . import models
 



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
    model = models.SelectUnidade
    fields = ('unidade',)
  
  
  



SELECIONAR_CHOICE = (('iniciais', 'INICIAIS'),  ('cns', 'CNS'),  ('cpf', 'CPF'),  ('dtinicio', 'DATA INICIO'),  ('unidade__nome', 'UNIDADE'),
  ('sexo', 'SEXO'),  ('cor', 'COR'),  ('dnasc', 'DATA NASCIMENTO'),  ('log', 'LOG TIPO'),  ('end', 'LOG ENDERECO'),  ('numero', 'NUMERO'),
  ('complemento', 'COMPLEMENTO'), ('cep', 'CEP'), ('responsavel', 'RESPONSAVEL'), ('tipo', 'TIPO'), ('situacao', 'SITUACAO'), ('orgaos', 'ORGÃOS'),)
  
  
class SelecionarCamposForm(forms.Form):
  
  selecionar = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                      choices=SELECIONAR_CHOICE)
  
  

  




  
  


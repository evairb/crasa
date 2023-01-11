from django import forms
from . import models
from django.contrib.auth.models import User
from unidade.models import Unidade
from utils.validacpf import valida_cpf
import re
from datetime import date


class PerfilForm(forms.ModelForm):
  rg = forms.CharField(required=False, label='RG', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control rg", "data-mask":"00.000.000-0","maxlength":"12" }))
  dnasc = forms.CharField(required=False, label='Data de nascimento', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control", "type": "date"}))
  fone = forms.CharField(required=False, label='Telefone', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control phone_with_ddd", "data-mask":"(00)00000-0000","maxlength":"14"}))
  class Meta:
    model = models.Perfil    
    fields = '__all__'
    exclude = ('usuario','nivel_acesso',)
    
class PerfilAtualizarForm(forms.ModelForm):
  rg = forms.CharField(required=False, label='RG', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control rg", "data-mask":"00.000.000-0","maxlength":"12" }))
  dnasc = forms.CharField(required=False, label='Data de nascimento', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control", "type": "date"}))
  fone = forms.CharField(required=False, label='Telefone', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control phone_with_ddd", "data-mask":"(00)00000-0000","maxlength":"14"}))
  class Meta:
    model = models.Perfil    
    fields = '__all__'
    exclude = ('usuario','nivel_acesso','unidade')
    
    
class UserForm(forms.ModelForm):
  
  #atualização não e requerido
  username = forms.CharField(required=False, label='CPF', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control cpf", "data-mask":"000.000.000-00","maxlength":"14"}))
  def __init__(self, usuario=None, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.usuario = usuario



  class Meta:
    model = User
    fields = ('first_name','last_name', 'username', 'email',)#is_active.
   
  
  def clean(self, *args, **kwargs):        
    data = self.data
    cleaned = self.cleaned_data
    validation_error_msgs = {}

    usuario_data = cleaned.get('username')
    email_data = cleaned.get('email')

    usuario_db = User.objects.filter(username=usuario_data).first()
    if usuario_db:
      email_atual = usuario_db.email
    email_db = User.objects.filter(email=email_data).first()
    
    
    error_msg_user_exists = 'CPF ja existe'
    error_msg_user_invalid = 'Digite um CPF valido com 11 digitos sendo apenas numeros'
    error_msg_email_exists = 'Email ja existe'
    error_msg_senha_different = 'Senhas não conferem'
    error_msg_senha_short = 'Sua senha precisa de pelo menos 6 caracteres'
    error_msg_required_field = 'Este campo é obrigatorio'
    error_msg_senha_lower = 'Senha precisa ter ao menos 1 caracter maiusculo e minusculo'
    error_msg_senha_number = 'Senha precisa ter ao menos 1 numero'
    error_msg_senha_special = 'Senha precisa ter ao menos 1 caracter especial @,#,!,* etc'

    
    #usuarios logados: atualizar
    if self.usuario:
      
      if not valida_cpf(usuario_data):
        validation_error_msgs['username'] = error_msg_user_invalid

      if usuario_data != usuario_db.username:              
        if usuario_db.username:          
          validation_error_msgs['username'] = error_msg_user_exists
          
      
      if email_data != email_atual:
        if email_db:
      #   if email_data != email_db.email:
          
          validation_error_msgs['email'] = error_msg_email_exists

      #TODO: remover e colocar em campo aparte
      
        
      





    #usuarios nao logados:
    else:
      if not valida_cpf(usuario_data):        
        validation_error_msgs['username'] = error_msg_user_invalid

      if usuario_db:
          validation_error_msgs['username'] = error_msg_user_exists
      
      if email_db:        
          validation_error_msgs['email'] = error_msg_email_exists
      
    
      
      
      
    if validation_error_msgs:
      raise(forms.ValidationError(validation_error_msgs))
    
    
    
    

ORGAOS_CHOICE = (('CAPS', 'CAPS'),  ('CAPS_A', 'CAPS_A'),  ('CAPS_I', 'CAPS_I'),  ('CER', 'CER'),  ('NIR', 'NIR'),
  ('UBS', 'UBS'),  ('URSI', 'URSI'),  ('SAD', 'SAD'),  ('EMAD', 'EMAD'),  ('PAI', 'PAI'),  ('PAVS', 'PAVS'),
  ('ESF_C', 'ESF_C'), ('ESF', 'ESF'), ('NASF', 'NASF'), ('UVIS', 'UVIS'), ('DVZ', 'DVZ'), ('CRAS', 'CRAS'),
  ('SASF', 'SASF'), ('CD_D', 'CD_D'), ('NPJ', 'NPJ'), ('NCI', 'NCI'), ('MP_IDOSO', 'MP_IDOSO'), ('MP_IS', 'MP_IS'),
  ('MP_PD', 'MP_PD'), ('MP_SP', 'MP_SP'), ('MP_GECAP', 'MP_GECAP'),)



 
class FormularioForm(forms.ModelForm):
  
  
  #unidade = forms.ModelChoiceField(queryset= Unidade.objects.filter(supervisao__nome=usuario))
  #TODO: resolver
  #dnasc = forms.CharField(required=False, label='Data de nascimento', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control", "type": "date"}))
  dtinicio = forms.DateField(required=False, label='Data de inicio', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control", "type": "date"}))
  orgaos = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                      choices=ORGAOS_CHOICE)
  unidade = forms.ModelChoiceField(required=False, queryset=None)
  
  
  def __init__(self, user, *args, **kwargs):
        super(FormularioForm, self).__init__(*args, **kwargs)
        self.fields['unidade'].queryset = Unidade.objects.filter(supervisao__nome=user.perfil.unidade.supervisao)
  
  #unidade = forms.ModelChoiceField(queryset= Unidade.objects.filter(supervisao__nome=usuario.perfil.unidade.supervisao))
  
  class Meta:
    model = models.Formulario    
    fields = '__all__'
    exclude = ('prefeitura','supervisao')
    #fields = ('cor','cpf','cns')
    
    
    
  def clean(self, *args, **kwargs):
    data = self.data
    cleaned = self.cleaned_data
    validation_error_msgs = {}
    
    iniciais_data = cleaned.get('iniciais')
    iniciais_data = iniciais_data.replace(" ","")
    #############
    cns_data = cleaned.get('cns')
    cpf_data = cleaned.get('cpf')
    cep_data = cleaned.get('cep')
    dtinicio_data = cleaned.get('dtinicio')
    dnasc_data = cleaned.get('dnasc')
    ni_data = cleaned.get('ni')
    cpfni_data = cleaned.get('cpfnaoinformado')
    cnsni_data = cleaned.get('cnsnaoinformado')
    
    
    
    
    error_msg_cns_number = 'Digite apenas numberos'
    error_msg_cns_number_15 = 'CNS diferente de 15 digitos'
    error_msg_cpf = 'Digite um CPF valido'
    error_msg_cnsni = 'CNS não informado, informe o motivo'
    error_msg_cpfni = 'CPF não informado, informe o motivo'
    error_msg_cep = 'Verifique o cep informado'
    error_msg_date = 'Campo obrigatorio, padrao dd/mm/aaaa'
    error_msg_date_invalid = 'Data nascimento invalida'
    
    if not cnsni_data and not cns_data:
      validation_error_msgs['cns'] = error_msg_cnsni
      
    if cns_data:
      if re.search(r'[^0-9]', cns_data):
        validation_error_msgs['cns'] = error_msg_cns_number
      
      if len(cns_data) >15 or len(cns_data) <15:
        validation_error_msgs['cns'] = error_msg_cns_number_15
    
    
    if not cpfni_data and not cpf_data:
      validation_error_msgs['cpf'] = error_msg_cpfni
      
    if cpf_data:
      if not valida_cpf(cpf_data):
        validation_error_msgs['cpf'] = error_msg_cpf
    
    # if not cpf_data and not cns_data:
    #   validation_error_msgs['cns'] = error_msg_cpf_or_cns
    #   validation_error_msgs['cpf'] = error_msg_cpf_or_cns
    
    if len(cep_data) < 8:
      validation_error_msgs['cep'] = error_msg_cep
    
         
    if dtinicio_data == None:
      validation_error_msgs['dtinicio'] = error_msg_date
    
    if dnasc_data == None and ni_data == False:
      validation_error_msgs['dnasc'] = error_msg_date
    
    if dnasc_data != None:
      if dnasc_data >= date.today():
        validation_error_msgs['dnasc'] = error_msg_date_invalid
    
       
      
    if validation_error_msgs:
      raise(forms.ValidationError(validation_error_msgs)) 
    
   
   
   
class ObservacaoForm(forms.ModelForm):
  
  class Meta:
    model = models.Observacao
    fields = ('observacao',)
    






class SituacaoForm(forms.ModelForm):

  class Meta:
    model = models.Formulario
    fields = ('situacao',)
    
    

class OrgaoAtualizar(forms.ModelForm):
  orgaos = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple,
                      choices=ORGAOS_CHOICE)
  class Meta:
    model = models.Formulario
    fields = ('orgaos',) 
    



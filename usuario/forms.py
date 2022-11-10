from django import forms
from . import models
from django.contrib.auth.models import User
from utils.validacpf import valida_cpf


class PerfilForm(forms.ModelForm):
  rg = forms.CharField(required=False, label='RG', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control rg", "data-mask":"00.000.000-0","maxlength":"12" }))
  dnasc = forms.CharField(required=False, label='Data de nascimento', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control", "type": "date"}))
  fone = forms.CharField(required=False, label='Telefone', help_text='Apenas numeros', widget=forms.TextInput(attrs={"class": "form-control phone_with_ddd", "data-mask":"(00) 0000-0000","maxlength":"14"}))
  class Meta:
    model = models.Perfil    
    fields = '__all__'
    exclude = ('usuario',)
    
    
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
      
      if email_data:
        if email_data != email_db.email:
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
    
    
    

class FormularioForm(forms.ModelForm):
  
  class Meta:
    model = models.Formulario    
    fields = '__all__'
    #fields = ('cor','cpf','cns')
    
    
  def clean(self, *args, **kwargs):        
    data = self.data
    cleaned = self.cleaned_data
    validation_error_msgs = {}
    
    iniciais_data = cleaned.get('iniciais')
    
    iniciais_data = iniciais_data.replace(" ","")
   
class ObservacaoForm(forms.ModelForm):
  
  class Meta:
    model = models.Observacao
    fields = ('observacao',)
     
    
    
class SituacaoForm(forms.ModelForm):


  class Meta:
    model = models.Formulario
    fields = ('situacao',)
    
    



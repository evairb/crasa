from django import forms
from django import forms
from . import models
from django.contrib.auth.models import User
from utils.validacpf import valida_cpf


class PerfilForm(forms.ModelForm):
  
  class Meta:
    model = models.Perfil    
    fields = '__all__'
    exclude = ('usuario',)
    
    
class UserForm(forms.ModelForm):
  #atualização não e requerido
  password = forms.CharField(required=False, widget=forms.PasswordInput(), label='Senha', help_text='Obrigadorio 6 a 20 caracteres, Letras Maiusculas é minusculas, numeros e caracteres especiais')
  confirm = forms.CharField(required=False, widget=forms.PasswordInput(), label='Confirmação Senha')
  username = forms.CharField(required=False, label='CPF', help_text='Apenas numeros')

  def __init__(self, usuario=None, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.usuario = usuario



  class Meta:
    model = User
    fields = ('first_name','last_name', 'username', 'password','confirm', 'email',)#is_active.
   
  
  def clean(self, *args, **kwargs):        
    data = self.data
    cleaned = self.cleaned_data
    validation_error_msgs = {}

    usuario_data = cleaned.get('username')
    password_data = cleaned.get('password')
    confirm_data = cleaned.get('confirm')
    email_data = cleaned.get('email')

    usuario_db = User.objects.filter(username=usuario_data).first()
    email_db = User.objects.filter(email=email_data).first()
    
    
    error_msg_user_exists = 'CPF ja existe'
    error_msg_user_invalid = 'Digite um CPF valido, apneas numeros'
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
      if password_data:
        if password_data != confirm_data:
          validation_error_msgs['password'] = error_msg_senha_different
          validation_error_msgs['confirm'] = error_msg_senha_different
        
        if len(password_data) <6 or len(password_data) >20:
          validation_error_msgs['password'] = error_msg_senha_short
          if password_data.islower():
            validation_error_msgs['password'] = error_msg_senha_lower            
            if password_data.isalpha():
              validation_error_msgs['password'] = error_msg_senha_special
        
      





    #usuarios nao logados:
    else:
      if not valida_cpf(usuario_data):        
        validation_error_msgs['username'] = error_msg_user_invalid

      if usuario_db:
          validation_error_msgs['username'] = error_msg_user_exists
      
      if email_db:        
          validation_error_msgs['email'] = error_msg_email_exists
      
      if not password_data:
        validation_error_msgs['password'] = error_msg_required_field
      
      if password_data != confirm_data:
          validation_error_msgs['password'] = error_msg_senha_different
          validation_error_msgs['confirm'] = error_msg_senha_different
        
      if len(password_data) <6 or len(password_data) >20:
          validation_error_msgs['password'] = error_msg_senha_short
      elif password_data.islower():
          validation_error_msgs['password'] = error_msg_senha_lower
      elif password_data.isdigit():          
          validation_error_msgs['password'] = error_msg_senha_number          
      elif password_data.isalpha():
          validation_error_msgs['password'] = error_msg_senha_special
      
      
      
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
    print(iniciais_data)
    
    
    
    
    
    



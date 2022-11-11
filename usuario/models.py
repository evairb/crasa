from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from datetime import date
import re
from utils.validacpf import valida_cpf
from unidade.models import Unidade,Prefeitura,Supervisao
from django.utils import timezone





class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)    
    dnasc = models.DateField(blank=True,null=True)
    funcao = models.CharField( max_length=100)
    rg = models.CharField(max_length=60)
    unidade = models.ForeignKey(Unidade, on_delete=models.SET_NULL, null=True)
    fone = models.CharField(max_length=14)     
    

    def __str__(self):
        return f'{self.usuario.first_name}'


    def clean(self):
        error_messages = {}          
             

        if re.search(r'[^\(0-9\)\-\s]+', self.fone):
            error_messages['fone'] = 'Telefone invalido, digite apenas números com ddd'
        
        if len(self.fone)<10:
            error_messages['fone'] = 'Numero invalido, faltam números, informe também o ddd'
            
        if self.dnasc == None:
            error_messages['dnasc'] = 'Campo obrigatorio, padrao dd/mm/aaaa'

        else:
            if self.dnasc >= date.today():
                error_messages['dnasc'] = 'Data nascimento invalida'
        

        if re.search(r'[^0-9\.\-]+', self.rg):
            error_messages['rg'] = 'Digite apenas numeros'        

        if error_messages:
            raise ValidationError(error_messages)
        
    class Meta:
        verbose_name= 'Perfil'
        verbose_name_plural = 'Perfis'



class Formulario(models.Model):
    prefeitura = models.ForeignKey(Prefeitura, on_delete=models.SET_NULL, null=True)
    supervisao = models.ForeignKey(Supervisao, on_delete=models.SET_NULL, null=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.SET_NULL, null=True)
    iniciais = models.CharField(max_length=40, null=True)    
    sexo = models.CharField(max_length=10, default=None, choices= (('Feminino', 'feminino'),('Masculino', 'masculino'),))
    Color = (
        ('Branca', 'branca'),
        ('Parda', 'parda'),
        ('Preta', 'preta'),
        ('Amarela', 'amarela'),
        ('Indigena', 'indigena'), 
    )

    cor = models.CharField(max_length=10, default=None, choices=Color)
    cns = models.CharField(max_length=15, null=True)
    cpf = models.CharField(max_length=11,null=True)
    ni = models.BooleanField(default=False, verbose_name='Data Nascimento não Informada')
    dnasc = models.DateField(blank=True,null=True)
    Endereco = (
        ('Rua', 'rua'),
        ('Estrada', 'est'),
        ('Avenida', 'av'),
    )    
    log =  models.CharField(max_length=10,default=None, choices=Endereco)
    end = models.CharField(max_length=255)
    numero = models.PositiveIntegerField(default=0)
    complemento = models.CharField(max_length=80, null=True)
    cep = models.CharField(max_length=9, null=True)
    responsavel = models.CharField(max_length=55, null=True)
    tipo = models.CharField(max_length=10, default='materiais', choices= (('Materiais', 'materiais'),('Animais', 'animais'),('Ambos', 'ambos')))
    dtinicio = models.DateField(blank=True,null=True)    
    situacao = models.CharField(max_length=10, default='ativo', choices= (('Ativo', 'ativo'),('Inativo', 'inativo')))
    caps = models.BooleanField(default=False, verbose_name='CAPS AD')
    caps_a = models.BooleanField(default=False, verbose_name='CAPS ADULTO')
    caps_i = models.BooleanField(default=False, verbose_name='CAPS IJ')
    cer = models.BooleanField(default=False, verbose_name='CER')
    nir = models.BooleanField(default=False, verbose_name='NIR')
    ubs = models.BooleanField(default=False, verbose_name='UBS')
    ursi = models.BooleanField(default=False, verbose_name='URSI')
    sad = models.BooleanField(default=False, verbose_name='SAD')
    emad = models.BooleanField(default=False, verbose_name='EMAD')
    pai = models.BooleanField(default=False, verbose_name='PAI')
    pavs = models.BooleanField(default=False, verbose_name='PAVS')
    esf_c = models.BooleanField(default=False, verbose_name='ESF-CNR')
    esf = models.BooleanField(default=False, verbose_name='ESF')
    nasf = models.BooleanField(default=False, verbose_name='NASF')
    uvis = models.BooleanField(default=False, verbose_name='UVIS')
    dvz = models.BooleanField(default=False, verbose_name='DVZ')
    cras = models.BooleanField(default=False, verbose_name='CRAS')
    creas = models.BooleanField(default=False, verbose_name='CREAS')
    sasf = models.BooleanField(default=False, verbose_name='SASF')
    cd_d = models.BooleanField(default=False, verbose_name='CD - Centro Dia')
    npj = models.BooleanField(default=False, verbose_name='NPJ')
    nci = models.BooleanField(default=False, verbose_name='NCI')
    mp_idoso = models.BooleanField(default=False, verbose_name='MP-PJDH-Idoso')
    mp_is = models.BooleanField(default=False, verbose_name='MP-PJDH-IS')
    mp_pd = models.BooleanField(default=False, verbose_name='MP-PJDH-PD')
    mp_sp = models.BooleanField(default=False, verbose_name='MP-PJDH-SP')
    mp_gecap = models.BooleanField(default=False, verbose_name='MP–GECAP')
    
    
    #orgaos acompanhando
    #outros orgaos
    #observacoes

    


    def __str__(self):
      return self.cpf
    
    def clean(self):
        error_messages = {}
        
        if re.search(r'[^0-9]', self.cns):
            error_messages['cns'] = 'Digite apenas Numeros'
            
        if len(self.cns) >15 or len(self.cns) <15:
            error_messages['cns'] = 'verifique a falta de números'
        
        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF valido'    


        if re.search(r'[^0-9]', self.cep):
            error_messages['cep'] = 'Cep invalido digite apenas numeros'
        
        if len(self.cep) < 8:
            error_messages['cep'] = 'Cep faltando numeros'
        
        if self.dtinicio == None:
            error_messages['dinicio'] = 'Campo obrigatorio, padrao dd/mm/aaaa'       
        
        
        
        if self.dnasc == None:
            error_messages['dnasc'] = 'Campo obrigatorio, padrao dd/mm/aaaa'

        else:
            if self.dnasc >= date.today():
                error_messages['dnasc'] = 'Data nascimento invalida'
                
        
        if error_messages:
            raise ValidationError(error_messages)




class Observacao(models.Model):
    observacao = models.TextField()
    formulario_observacao = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    data_observacao = models.DateTimeField(default=timezone.now)
    usuario_observacao = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.formulario_observacao
    

    

    
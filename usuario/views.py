import re
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView,View,CreateView
from . import models
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



class BasePerfil(View):
    template_name = "cadastrar.html"
    
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        
        #usuario logado
        self.perfil = None
        if self.request.user.is_authenticated:
            self.perfil = models.Perfil.objects.filter(usuario=self.request.user).first()
            
            self.contexto = {
                
                'userform' : forms.UserForm(data=self.request.POST or None, usuario=self.request.user, instance=self.request.user),
                'perfilform' : forms.PerfilForm(data=self.request.POST or None, instance=self.perfil)
                
            }
        #criando usuario
        else:
            self.contexto = {
                'userform' : forms.UserForm(data=self.request.POST or None),
                'perfilform': forms.PerfilForm(data=self.request.POST or None)
            }
        self.userform = self.contexto['userform']
        self.perfilform = self.contexto['perfilform']
        
    
        if self.request.user.is_authenticated:
            self.template_name = "atualizar.html"
            
        self.renderizar = render(self.request, self.template_name, self.contexto)
        
    def get(self, *args, **kwargs):
        return self.renderizar
        

class Cadastrar(BasePerfil):    
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.perfilform.is_valid():
        
            
            return self.renderizar
        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        #enviar formulario
        #usuario logado
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(User, username=self.request.user.username )
            usuario.username = username

            if password:
                usuario.set_password(password)
            

            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()

            if not self.perfil:
                self.perfilform.cleaned_data['usuario'] = usuario
                perfil = models.Perfil(**self.perfilform.cleaned_data)
                perfil.save()
            else:
                perfil = self.perfilform.save(commit=False)
                perfil.usuario = usuario
                perfil.save()

        else:
            usuario = self.userform.save(commit=False)
            usuario.set_password(password)
            usuario.save()

            perfil = self.perfilform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()
            
            #TODO: mudar retorno para pagina informando que deve aguardar autorização

        return self.renderizar


class Login(TemplateView):
    template_name = "login.html"

    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(self.request, 'Error')            
            return redirect('usuario:login')            
        
        usuario = authenticate(self.request, username=username, password=password)
        
        if not usuario:            
            return redirect('usuario:login')
        
        login(self.request, user=usuario)
        messages.success(
                self.request, 'Usuário Logado.'                
        )
        return redirect('usuario:formlist')
    
    
 
class Teste(TemplateView):    
         
    def get(self, *args, **kwargs):        
            return render(self.request, "va.html")
        
        
   
    
class Logout(View):
    def get(self, *args, **kwargs):        
        logout(self.request)
        return redirect('usuario:login')


#carrega o formulario
class Formulario(View):
    template_name = 'formulario/form.html'    

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        #usuario logado        
        self.contexto = {            
            'formularioform' : forms.FormularioForm(data=self.request.POST or None)
        }    
        self.formularioform = self.contexto['formularioform']       
        self.renderizar = render(self.request, self.template_name, self.contexto)
        
    def get(self, *args, **kwargs):
        return self.renderizar

#envia o formulario
class EnviarForm(Formulario):    
    def post(self, *args, **kwargs):        
        if not self.formularioform.is_valid():
        
            return self.renderizar        
        
        iniciais = self.formularioform.cleaned_data.get('iniciais')
        iniciais = iniciais.replace(" ","")
        formulario = self.formularioform.save(commit=False)
        formulario.iniciais=iniciais        
        formulario.save() 
  
        return self.renderizar        




class FormList(TemplateView): 
    
   
       
        template_name = "formulario/form_list.html"
        def get(self, *args, **kwargs): 
            if not self.request.user.is_authenticated: 
                return redirect('usuario:login')
                                  
            context = super().get(self,*args, **kwargs)            
            form_list = models.Formulario.objects.all() 
            print(context)                
            return render(*args, "formulario/form_list.html", {'form_list':form_list})          

        

   
def ver_contato(request, contato_id):
    contato = models.Formulario.objects.get(id=contato_id)
    return render(request, 'formulario/detalhes.html', {'contato': contato})



        

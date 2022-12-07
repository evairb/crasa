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
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from utils.email import mail
from utils.acesso import nivel_acesso
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.views.decorators.cache import never_cache






    


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
                'perfilform' : forms.PerfilAtualizarForm(data=self.request.POST or None, instance=self.perfil),
                
            }
            
        else:
            self.contexto = {
                'userform' : forms.UserForm(data=self.request.POST or None),
                'perfilform': forms.PerfilForm(data=self.request.POST or None),
            }
        
        self.userform = self.contexto['userform']
        self.perfilform = self.contexto['perfilform']
        
    
        if self.request.user.is_authenticated:
            self.template_name = "atualizar.html"
            
        self.renderizar = render(args[0], self.template_name, self.contexto)
        
    def get(self, *args, **kwargs):
        return self.renderizar
        

class Cadastrar(BasePerfil):    
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.perfilform.is_valid():             
            return self.renderizar
        username = self.userform.cleaned_data.get('username')        
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        #enviar formulario
        #usuario logado
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(User, username=self.request.user.username )
            usuario.username = username
            
            #if password:
            #    usuario.set_password(password)

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
                messages.success(
                self.request,'Usuario atualizado.') 
                return redirect('usuario:cadastrar')

        else:
            usuario = self.userform.save(commit=False) 
            password = usuario.last_name+"dtic2022"
            usuario.set_password(password)
            usuario.is_active = False         
            usuario.save()
            #mail(usuario.email,usuario,usuario.pk) envia email para cadastro de senha   
            

            perfil = self.perfilform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()
            return redirect('usuario:success')
            
            #TODO: mudar retorno para pagina informando que deve aguardar autorização

        return self.renderizar


class Login(TemplateView):
    template_name = "login.html"

    def post(self, *args, **kwargs):  
        self.request.COOKIES.clear()
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        
        if not username or not password:
            messages.error(self.request, 'Error')            
            return render(args[0],"login.html", {"login": "Usuário ou senha incorretos"})        
        
       
        usuario = authenticate(args[0], username=username, password=password)
       
        if usuario is None:            
           return render(args[0],"login.html", {"login": {"text":"Usuário ou senha incorretos"}}) 
             
        login(args[0], user=usuario)
        messages.success(
               args[0], 'Usuário Logado.'                
        )
        
        return redirect('usuario:formlist')
    
    
        
        
                    
   
    
class Logout(View):
    def post(self, *args, **kwargs):        
        logout(args[0])
        
        
        return redirect('usuario:login')


#carrega o formulario
@method_decorator(login_required, name='get')
class Formulario(View):
    template_name = 'formulario/form.html' 
    
    
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        
        
        #usuario logado        
        self.contexto = {            
            'formularioform' : forms.FormularioForm(data=self.request.POST or None),
            'observacaoform' : forms.ObservacaoForm(data=self.request.POST or None), 
               
        }    
        self.formularioform = self.contexto['formularioform']
        self.observacaoform = self.contexto['observacaoform']  
        
         
        self.renderizar = render(self.request, self.template_name, self.contexto)
    @method_decorator(never_cache)  
    def get(self, *args, **kwargs):
         
        return self.renderizar

#envia o formulario
#@method_decorator(login_required, name='post')

class EnviarForm(Formulario):
    @method_decorator(login_required)     
     
    def post(self, *args, **kwargs):        
        if not self.formularioform.is_valid():
        
            return self.renderizar        
        usuario = get_object_or_404(User, username=self.request.user.username )
        iniciais = self.formularioform.cleaned_data.get('iniciais')
        iniciais = iniciais.replace(" ","")
        iniciais = iniciais.upper()
                       
        formulario = self.formularioform.save(commit=False)
        formulario.iniciais=iniciais
        formulario.unidade= usuario.perfil.unidade   
        formulario.save() 
        
        
        observacao = self.observacaoform.save(commit=False)
        observacao.formulario_observacao = formulario
        observacao.usuario_observacao = usuario
        observacao.save()
        
        messages.success(
               args[0], 'Formulario Cadastrado com sucesso.'                
        )
                      
        return redirect('usuario:formlist')



#@method_decorator(login_required, name='get')
class FormList(TemplateView):
    @method_decorator(never_cache)
    @method_decorator(login_required)
    def get(self, *args, **kwargs): 
        nivel = self.request.user.perfil.nivel_acesso
        filtro = self.request.user.perfil.unidade
                
        if nivel ==  'crasa':
            form_list = models.Formulario.objects.filter()
        else:
            q = nivel_acesso(nivel,filtro) 
            form_list = models.Formulario.objects.filter(q)
                
        
                       
        return render(args[0], "formulario/form_list.html", {'form_list':form_list})          

        

@login_required
@never_cache 
def ver_contato(request, contato_id):
    formulario = models.Formulario.objects.filter(id=contato_id).first()
    
    print(formulario.id)
    contexto = { 
        'contato': models.Formulario.objects.get(id=contato_id),
        'observacao': models.Observacao.objects.filter(formulario_observacao_id=contato_id),        
        'observacaoform': forms.ObservacaoForm(data=request.POST or None),
        'orgaosform': forms.OrgaoAtualizar(data=request.POST or None, instance=formulario),
        
        }
    
    observacaoform = contexto['observacaoform']
    orgaosform = contexto['orgaosform'] 
    contato = contexto['contato']    
    usuario = get_object_or_404(User, username=request.user.username)
   
    
    
       
    if request.method == 'POST':
        
        formulario = orgaosform.save(commit=False)
        formulario.save()
        
        observacao = observacaoform.save(commit=False)
        observacao.formulario_observacao = contato
        observacao.usuario_observacao = usuario
        observacao.save()
        return redirect('usuario:formlist')
               
        
            
    
    return render(request, 'formulario/detalhes.html', contexto)


#TODO:envia email
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
            
			if associated_users.exists():
				for user in associated_users:
					subject = "Reset de senha solicitada"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
                    #TODO: PRODAM DESCOMENTE
                    #'domain':'172.17.8.4:8000',    
					'domain':'172.17.8.4:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
                    
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'oci@smsprefeiturasp.org' , [user.email],fail_silently=False)                        
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
                        
					return redirect ("/password_reset/done/") 
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})


       
def success(request):
    return render(request, template_name="message/success.html" )


@login_required
@login_required
def atualizar(request,contato_id):
    situacao = models.Formulario.objects.filter(id=contato_id).first()
    if situacao.situacao == "Ativo":
        situacao.situacao = "Inativo"
        situacao.save()
    else:
        situacao.situacao = "Ativo"
        situacao.save()
    
    return redirect('usuario:formlist')


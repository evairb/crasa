from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView,View
from usuario import models
from . import forms
from django.contrib import messages
from utils.email import mail
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from utils.acesso import nivel_acesso_user
from django.views.decorators.cache import never_cache


# Create your views here.
@method_decorator(login_required, name='get')
@method_decorator(never_cache, name='get')
class UserList(TemplateView): 
    template_name = "user_list.html"
    
      
    def get(self, *args, **kwargs):
        
        # if not self.request.user.is_superuser: 
        #     return redirect('usuario:formlist')
        # user_list= models.User.objects.all()
        
        nivel = self.request.user.perfil.nivel_acesso
        filtro = self.request.user.perfil.unidade

        if nivel == 'usuario':
            return redirect('usuario:formlist')
        
        else:
            if nivel ==  'crasa':
                user_list= models.User.objects.all()
                
                
            else:
                q = nivel_acesso_user(nivel,filtro) 
                user_list= models.User.objects.filter(q)
                
                
            
            
            
        return render(*args, "user_list.html", {'user_list':user_list})
    
    
        
@login_required 
@never_cache
def atualizar(request,id_form):
        usuario = models.User.objects.filter(id=id_form).first()
        
        contexto = {
            'userform' : forms.AutoForm(data=request.POST or None,instance=usuario),
            'usuario' : usuario,
            'userperfilform' : forms.AutoPerfilForm(data=request.POST or None, instance=usuario.perfil),
        
            }
        ativo = usuario.is_active
        
        userform = contexto['userform']
        userperfilform = contexto['userperfilform']
        if request.method == 'POST':
            nivel = request.POST.get('select_nivel')
            
            
              
            if request.user.perfil.nivel_acesso == 'crasa':
                
                
                usuario.perfil = userperfilform.save(commit=False)
                usuario.perfil.save()
                
                
                usuario = userform.save(commit=False)
                usuario.save()
            
            else:
                usuario = userform.save(commit=False)
                usuario.perfil.nivel_acesso = nivel
                usuario.perfil.save()        
                usuario.save()
            
            
          
            if usuario.is_active != ativo and usuario.is_active:
                
                mail(usuario.email,usuario,usuario.pk)
            return redirect('unidade:userlist') 
        return render(request, 'autorizar.html', contexto)
    
    



    
 
    
    
    
    
    
    


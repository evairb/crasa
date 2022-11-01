from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView,View
from usuario import models
from . import forms
from django.contrib import messages
from utils.email import mail


# Create your views here.
class UserList(TemplateView): 
    template_name = "user_list.html"
    def get(self, *args, **kwargs): 
        if not self.request.user.is_superuser: 
            return redirect('usuario:formlist')
        user_list= models.User.objects.all()
        return render(*args, "user_list.html", {'user_list':user_list})   
    


    

def atualizar(request,id_form):
        usuario = models.User.objects.filter(id=id_form).first()
        contexto = {
            'userform' : forms.AutoForm(data=request.POST or None,instance=usuario),
            'usuario' : usuario
            }
        userform = contexto['userform']
        if request.method == 'POST':
            usuario = userform.save(commit=False)
            usuario.save() 
            if usuario.is_active:
                mail(usuario.email,usuario,usuario.pk)
            return redirect('unidade:userlist') 
        return render(request, 'autorizar.html', contexto)
    
    

def relatorio():
    pass


    
 
    
    
    
    
    
    


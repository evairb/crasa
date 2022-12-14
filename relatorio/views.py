from django.shortcuts import render,redirect
from usuario.models import Formulario
from datetime import datetime
from django.http import HttpResponse
from utils.export import export_xlsx, MDATA
from django import forms
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q
from unidade.models import Unidade
from utils.acesso import nivel_acesso_relatorio
from django.views.decorators.cache import never_cache





@method_decorator(login_required, name='get')
@method_decorator(never_cache, name='get')
class Relatorio(View):
    template_name = 'relatorio.html'    
    
    def setup(self, *args, **kwargs, ):
        super().setup(*args, **kwargs)
        
        
        self.contexto = {            
            'relatorioform' : forms.RelatorioForm(data=self.request.POST or None),
            'unidadeform' : forms.UnidadeForm(data=self.request.POST or None),
            
        }    
        self.relatorioform = self.contexto['relatorioform']
        self.unidadeform = self.contexto['unidadeform']
                
        self.renderizar = render(self.request, self.template_name, self.contexto)
        
        
    def get(self, *args, **kwargs):        
        return self.renderizar




@method_decorator(login_required, name='post') 
@method_decorator(never_cache,name='post')
class EnviarForm(Relatorio):
       
    def post(self, *args, **kwargs):        
        if not self.relatorioform.is_valid():
        
            return self.renderizar 
                    
        status = self.relatorioform.cleaned_data.get('status')
        data_inicio = self.relatorioform.cleaned_data.get('data_inicio')       
        data_fim = self.relatorioform.cleaned_data.get('data_fim')
        values = ['iniciais','cns','cpf','dtinicio','unidade__nome','sexo','cor','dnasc','end','bairro','numero','complemento','cep','responsavel','tipo','situacao','orgaos','outros']
        unidade = None
        
        response = exportar_xlsx_vi(values, status, data_inicio, data_fim, unidade)
        return response
        
    
    
    
        
                     
        



def exportar_xlsx_vi(values, status, data_inicio, data_fim, unidade):
#def exportar_xlsx_vi(values):   
    filename = 'formulario.xls'
    _filename = filename.split('.')
    filename_final = f'{_filename[0]}_{MDATA}.{_filename[1]}'
    
    
   
    
    
    if status == 'ambos':#sem filtro no status
        
        
        if unidade == None:            
            q = Q(Q(dtinicio__gte=data_inicio))
            
        else:
            q = Q(Q(dtinicio__gte=data_inicio)  & Q(unidade=unidade)) 
        
        q2 = Q(dtinicio__gt=data_fim)        
        queryset = Formulario.objects.filter(q).exclude(q2).values_list(*values)
      
        
    else:
        if unidade == None:            
            q = Q(Q(dtinicio__gte=data_inicio) & Q(situacao=status))
            
        else:
            q = Q(Q(dtinicio__gte=data_inicio) & Q(situacao=status) & Q(unidade=unidade)) 
            
        
        q2 = Q(dtinicio__gt=data_fim)
        queryset = Formulario.objects.filter(q).exclude(q2).values_list(*values)
 
        
   
    response = export_xlsx(filename_final, queryset, values)
    return response
    # print(type(queryset))
    # return redirect('relatorio:geral')




class Selecionar(View):
    
    template_name = 'detalhado.html'    
    
    def setup(self, *args, **kwargs, ):
        super().setup(*args, **kwargs)
        
        nivel = self.request.user.perfil.nivel_acesso
        filtro = self.request.user.perfil.unidade
        
        
        if nivel ==  'crasa':
            unidade_list = Unidade.objects.all()
        else:
            q = nivel_acesso_relatorio(nivel,filtro)  
            unidade_list = Unidade.objects.filter(q)
                   
              
        self.contexto = {            
             
            'relatorioform' : forms.RelatorioForm(data=self.request.POST or None),                    
            'selecionarform' : forms.SelecionarCamposForm(data=self.request.POST or None),
            #'unidade' : Unidade.objects.all()
            'unidade' : unidade_list
        }    
        self.relatorioform = self.contexto['relatorioform']        
        self.selecionarform = self.contexto['selecionarform']
        
                
        self.renderizar = render(self.request, self.template_name, self.contexto)
    @method_decorator(login_required)
    @method_decorator(never_cache) 
        
    def get(self, *args, **kwargs):        
        return self.renderizar


class EnviarSelecao(Selecionar):
    @method_decorator(login_required)
    @method_decorator(never_cache)   
    def post(self, *args, **kwargs):       
        
        if not self.selecionarform.is_valid():
        
            return self.renderizar 
        values = self.selecionarform.cleaned_data.get('selecionar')        
        status = self.relatorioform.cleaned_data.get('status')
        data_inicio = self.relatorioform.cleaned_data.get('data_inicio')       
        data_fim = self.relatorioform.cleaned_data.get('data_fim')       
        unidade = self.request.POST.get('select_unidade')
        
        if unidade == 'Null':
            unidade = None
        
        #return redirect('relatorio:detalhado')
        response = exportar_xlsx_vi(values, status, data_inicio, data_fim, unidade)
        return response
        

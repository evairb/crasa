from django.shortcuts import render
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




#MDATA = datetime.now().strftime('%Y-%m-%d')
class Relatorio(View):
    template_name = 'relatorio_unidade.html'    
    @method_decorator(login_required)
    def setup(self, *args, **kwargs, ):
        super().setup(*args, **kwargs)
        #usuario logado        
        self.contexto = {            
            'relatorioform' : forms.RelatorioForm(data=self.request.POST or None),
            'unidadeform' : forms.UnidadeForm(data=self.request.POST or None),
            
        }    
        self.relatorioform = self.contexto['relatorioform']
        self.unidadeform = self.contexto['unidadeform']
                
        self.renderizar = render(self.request, self.template_name, self.contexto)
        
        
    def get(self, *args, **kwargs):        
        return self.renderizar





class EnviarForm(Relatorio):
    @method_decorator(login_required)    
    def post(self, *args, **kwargs):        
        if not self.relatorioform.is_valid():
        
            return self.renderizar              
        status = self.relatorioform.cleaned_data.get('status')
        data_inicio = self.relatorioform.cleaned_data.get('data_inicio')       
        data_fim = self.relatorioform.cleaned_data.get('data_fim')
        
        
        response = exportar_xlsx_vi(status, data_inicio, data_fim)
        return response
    
    
    
        
                     
        



def exportar_xlsx_vi(status, data_inicio, data_fim):
    
    filename = 'formulario.xls'
    _filename = filename.split('.')
    filename_final = f'{_filename[0]}_{MDATA}.{_filename[1]}'
    
    
    if status == 'ambos':#sem filtro no status
        
        
    
        queryset = Formulario.objects.filter(dtinicio__gte=data_inicio).exclude(dtinicio__gt=data_fim).values_list('iniciais','cns','cpf','dtinicio','unidade','sexo','cor',
                                                                           'dnasc','log','end','numero','complemento','cep','responsavel',
                                                                           'tipo','situacao')
    
    else:
        q = Q(Q(dtinicio__gte=data_inicio) & Q(situacao=status))
        q2 = Q(dtinicio__gt=data_fim)
        queryset = Formulario.objects.filter(q).exclude(q2).values_list('iniciais','cns','cpf','dtinicio','unidade__nome','sexo','cor',
                                                                           'dnasc','log','end','numero','complemento','cep','responsavel',
                                                                           'tipo','situacao')
 
        
    #return print(queryset)
    response = export_xlsx(filename_final, queryset)
    return response






class Relatorio(View):
    template_name = 'relatorio_unidade.html'    
    @method_decorator(login_required)
    def setup(self, *args, **kwargs, ):
        super().setup(*args, **kwargs)
        #usuario logado        
        self.contexto = {            
            'relatorioform' : forms.RelatorioForm(data=self.request.POST or None),
            'unidadeform' : forms.UnidadeForm(data=self.request.POST or None),
            
        }    
        self.relatorioform = self.contexto['relatorioform']
        self.unidadeform = self.contexto['unidadeform']
                
        self.renderizar = render(self.request, self.template_name, self.contexto)
        
        
    def get(self, *args, **kwargs):        
        return self.renderizar





class EnviarForm(Relatorio):
    @method_decorator(login_required)    
    def post(self, *args, **kwargs):        
        if not self.relatorioform.is_valid():
        
            return self.renderizar              
        status = self.relatorioform.cleaned_data.get('status')
        data_inicio = self.relatorioform.cleaned_data.get('data_inicio')       
        data_fim = self.relatorioform.cleaned_data.get('data_fim')
        
        
        response = exportar_xlsx_vi(status, data_inicio, data_fim)
        return response


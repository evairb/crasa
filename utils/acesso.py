from django.db.models import Q

#formulario
def nivel_acesso(nivel, filtro):
    
   
    if nivel == 'supervisao':
        q = Q(unidade__supervisao=filtro.supervisao)
    if nivel == 'unidade' or nivel == 'usuario':
        q = Q(unidade=filtro)
    
    return q




#usuarios
def nivel_acesso_user(nivel, filtro):
    
   
    if nivel == 'supervisao':
        q = Q(perfil__unidade__supervisao=filtro.supervisao)
    if nivel == 'unidade':
        q = Q(perfil__unidade=filtro)
        
    
    return q

#relatorio
def nivel_acesso_relatorio(nivel, filtro):
    
   
    if nivel == 'supervisao':
        q = Q(supervisao=filtro.supervisao)
    if nivel == 'unidade' or nivel == 'usuario':
        q = Q(nome=filtro)
    
    return q
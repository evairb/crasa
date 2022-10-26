from django.urls import path
from . import views


app_name = "usuario"

urlpatterns = [
    path('login/', views.Login.as_view(), name="login"),
    path('cadastrar/', views.Cadastrar.as_view(), name="cadastrar"),    
    path('logout/', views.Logout.as_view(), name="logout"),
    
    
    path('form/', views.EnviarForm.as_view(), name="form"),
    path('', views.FormList.as_view(), name="formlist"),
    path('<int:contato_id>', views.ver_contato, name="detalhes" ),
    
    
    
    
    
    
    path('teste/', views.Teste.as_view(), name="teste"),
 
    
]

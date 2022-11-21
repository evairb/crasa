from django.urls import path
from . import views


app_name = "relatorio"

urlpatterns = [
    
#path('export/', views.exportar_xlsx_vi, name="export"),
path('geral/', views.EnviarForm.as_view(), name="geral"),
path('detalhado/', views.EnviarSelecao.as_view(), name="detalhado"),
    
]
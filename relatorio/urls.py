from django.urls import path
from . import views


app_name = "relatorio"

urlpatterns = [
    
#path('export/', views.exportar_xlsx_vi, name="export"),
path('exportar/', views.EnviarForm.as_view(), name="exportar"),
path('export/<int:a>', views.EnviarForm.as_view(), name="exportgeral"),

    
]
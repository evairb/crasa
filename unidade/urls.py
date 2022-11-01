from django.urls import path
from . import views


app_name = "unidade"

urlpatterns = [
    path('userlist/', views.UserList.as_view(), name="userlist"),
    path('<int:id_form>', views.atualizar, name="ative"),
    #path('<int:contato_id>', views.ver_contato, name="detalhes" ),
    
]
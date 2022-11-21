from django.db import models
from unidade.models import Unidade

# Create your models here.
class SelectUnidade(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.SET_NULL, null=True, blank=True)
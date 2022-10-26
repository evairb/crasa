from django.db import models




class Prefeitura(models.Model):
    nome = models.CharField(max_length=80, null=True)
    def __str__(self):
        return self.nome



class Supervisao(models.Model):
    nome = models.CharField(max_length=80, null=True)
    prefeitura = models.ForeignKey('Prefeitura', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Supervisão'
        verbose_name_plural = 'Supervisões'



class Unidade(models.Model):
    nome = models.CharField(max_length=80, null=True)
    supervisao = models.ForeignKey('Supervisao', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


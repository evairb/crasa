# Generated by Django 4.1.4 on 2023-01-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0021_formulario_cpfnaoinformado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='cnsnaoinformado',
            field=models.CharField(blank=True, choices=[('Nao Informado', 'Criança não possui'), ('Nao Informado', 'Pessoa se recusa fornecer'), ('Nao Informado', 'Pessoa com Condição CLinica ou Neurologica Grave'), ('Nao Informado', 'Pessoa Estrangeira'), ('Nao Informado', 'Pessoa com Transtorno Mental')], max_length=60, null=True, verbose_name='CNS Não Informado'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='cpfnaoinformado',
            field=models.CharField(blank=True, choices=[('Nao Informado', 'Criança não possui'), ('Nao Informado', 'Pessoa se recusa fornecer'), ('Nao Informado', 'Pessoa com Condição CLinica ou Neurologica Grave'), ('Nao Informado', 'Pessoa Estrangeira'), ('Nao Informado', 'Pessoa com Transtorno Mental')], max_length=60, null=True, verbose_name='CNS Não Informado'),
        ),
    ]

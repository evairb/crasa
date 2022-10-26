# Generated by Django 4.1.2 on 2022-10-24 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unidade', '0002_supervisao_prefeitura_unidade_supervisao'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='status',
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iniciais', models.CharField(max_length=40, null=True)),
                ('sexo', models.CharField(choices=[('Feminino', 'feminino'), ('Masculino', 'masculino')], default=None, max_length=10)),
                ('cor', models.CharField(choices=[('Branca', 'branca'), ('Parda', 'parda'), ('Preta', 'preta'), ('Amarela', 'amarela'), ('Indigena', 'indigena')], default=None, max_length=10)),
                ('cns', models.CharField(max_length=14, null=True)),
                ('cpf', models.CharField(max_length=11, null=True)),
                ('ni', models.BooleanField(default=False)),
                ('dnasc', models.DateField(blank=True, null=True)),
                ('log', models.CharField(choices=[('Rua', 'rua'), ('Estrada', 'est'), ('Avenida', 'av')], default=None, max_length=10)),
                ('end', models.CharField(max_length=255)),
                ('number', models.PositiveIntegerField(default=0)),
                ('complemento', models.CharField(max_length=80, null=True)),
                ('cep', models.CharField(max_length=9, null=True)),
                ('dtinicio', models.DateField(blank=True, null=True)),
                ('situacao', models.CharField(choices=[('Ativo', 'ativo'), ('Inativo', 'inativo')], default='ativo', max_length=10)),
                ('prefeitura', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unidade.prefeitura')),
                ('supervisao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unidade.supervisao')),
                ('unidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unidade.unidade')),
            ],
        ),
    ]
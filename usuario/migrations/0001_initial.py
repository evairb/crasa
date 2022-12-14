# Generated by Django 4.1.2 on 2022-10-21 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unidade', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dnasc', models.DateField(blank=True, null=True)),
                ('funcao', models.CharField(max_length=100)),
                ('rg', models.CharField(max_length=60)),
                ('fone', models.CharField(max_length=11)),
                ('status', models.BooleanField(default=False)),
                ('unidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unidade.unidade')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
            },
        ),
    ]

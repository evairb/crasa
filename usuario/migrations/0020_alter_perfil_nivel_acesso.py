# Generated by Django 4.1.4 on 2022-12-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0019_formulario_outros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='nivel_acesso',
            field=models.CharField(choices=[('crasa', 'Crasa'), ('supervisao', 'Supervisão'), ('unidade', 'Unidade'), ('usuario', 'Usuario')], default='usuario', max_length=16),
        ),
    ]

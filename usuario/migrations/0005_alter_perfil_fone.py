# Generated by Django 4.1.2 on 2022-11-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_rename_number_formulario_numero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='fone',
            field=models.CharField(max_length=14),
        ),
    ]
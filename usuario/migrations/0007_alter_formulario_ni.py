# Generated by Django 4.1.3 on 2022-11-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_observacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='ni',
            field=models.BooleanField(default=False, verbose_name='Data Nascimento não Informada'),
        ),
    ]
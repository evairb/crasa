# Generated by Django 4.1.3 on 2022-11-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0009_remove_formulario_caps_remove_formulario_caps_a_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='orgaos',
            field=models.CharField(max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='formulario',
            name='outros',
            field=models.CharField(blank='True', max_length=40, verbose_name='Outros Orgãos'),
        ),
        migrations.DeleteModel(
            name='OrgaosAcompanhamento',
        ),
    ]

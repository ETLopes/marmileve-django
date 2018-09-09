# Generated by Django 2.0.6 on 2018-08-13 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemarmileve', '0031_cliente_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='tamanho',
            field=models.CharField(choices=[('P', 'Pequeno'), ('G', 'Grande'), ('S', 'Sopa')], max_length=1),
        ),
    ]

# Generated by Django 2.0.6 on 2018-08-07 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemarmileve', '0024_endereco_endereco_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='endereco',
            field=models.CharField(default='a', max_length=200),
        ),
    ]
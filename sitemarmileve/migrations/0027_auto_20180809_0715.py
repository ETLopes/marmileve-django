# Generated by Django 2.0.6 on 2018-08-09 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemarmileve', '0026_auto_20180807_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='data',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='prato',
            field=models.CharField(max_length=200),
        ),
    ]

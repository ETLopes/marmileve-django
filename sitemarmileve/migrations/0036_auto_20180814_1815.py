# Generated by Django 2.0.6 on 2018-08-14 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitemarmileve', '0035_auto_20180814_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estoque',
            name='pedidoid',
        ),
        migrations.RemoveField(
            model_name='itempedido',
            name='estoqueid',
        ),
    ]

# Generated by Django 2.0.6 on 2018-07-17 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemarmileve', '0017_auto_20180717_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 2.0.6 on 2018-07-14 22:57

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('sitemarmileve', '0007_auto_20180714_2024'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pedidos',
            new_name='Pedido',
        ),
        migrations.AlterField(
            model_name='itempedidos',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
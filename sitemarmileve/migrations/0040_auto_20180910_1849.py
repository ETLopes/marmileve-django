# Generated by Django 2.0.6 on 2018-09-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemarmileve', '0039_auto_20180910_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frete',
            name='valorfrete',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valortotal',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='preco',
            name='preco',
            field=models.FloatField(),
        ),
    ]

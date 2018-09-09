# Generated by Django 2.0.6 on 2018-08-10 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemarmileve', '0027_auto_20180809_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstoqueCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prato', models.CharField(max_length=200)),
                ('qtd', models.SmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='estoque',
            name='data_fabricacao',
            field=models.DateField(),
        ),
    ]

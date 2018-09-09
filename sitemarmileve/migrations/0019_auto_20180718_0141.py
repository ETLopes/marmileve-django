# Generated by Django 2.0.6 on 2018-07-18 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitemarmileve', '0018_auto_20180717_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endereco',
            old_name='id_cliente',
            new_name='nome_cliente',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='email',
        ),
        migrations.AddField(
            model_name='produto',
            name='pratonumero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sitemarmileve.NumeroProduto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='numeroproduto',
            name='pratonumero',
            field=models.IntegerField(unique=True),
        ),
    ]

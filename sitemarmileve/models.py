from django.db import models


# Create your models here.

class NumeroProduto(models.Model):
    pratonumero = models.IntegerField()

    def __str__(self):
        return str(self.pratonumero)


class Produto(models.Model):
    prato = models.ForeignKey(NumeroProduto, on_delete=models.CASCADE)
    prato_text = models.CharField(max_length=200)
    tam_text = models.CharField(max_length=1)
    pub_date = models.DateTimeField('Data de adição')
    ativo = models.BooleanField()

    def __str__(self):
        return self.prato_text


class Cliente(models.Model):
    nome_text = models.CharField(max_length=200)
    email = models.EmailField()
    cpf = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_text


class Endereco(models.Model):
    nome = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco_text = models.CharField(max_length=200)
    numero_text = models.IntegerField()
    complemento_text = models.CharField(max_length=200)
    bairro_text = models.CharField(max_length=200)
    cidade_text = models.CharField(max_length=200)

    def __str__(self):
        return self.endereco_text


class Pedido(models.Model):
    nome = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    email = models.EmailField()
    cpf = models.CharField(max_length=13)

    def __str__(self):
        return str(self.nome)


class ItemPedido(models.Model):
    item = models.AutoField()
    data = models.DateField(auto_now=True)
    prato = models.CharField(max_length=200)
    tamanho = models.CharField(max_length=1)
    qtd = models.PositiveSmallIntegerField()


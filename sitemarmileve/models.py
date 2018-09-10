from django.db import models


# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nome)


class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco =models.CharField(max_length=200)
    numero = models.PositiveSmallIntegerField()
    complemento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    endereco_ativo = models.BooleanField()

    def __str__(self):
        return self.endereco


class Prato(models.Model):
    pratonumero = models.PositiveSmallIntegerField()
    prato = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.prato)


class Preco(models.Model):
    tamanho = models.CharField(max_length=1, choices=(('P', 'Pequeno'), ('G', 'Grande'), ('S', 'Sopa')))
    preco = models.FloatField()
    data_ativo = models.DateField()  # A data a partir da qual tamanho e preço são validos para cada prato.

    def ___str__(self):
        return self.tamanho


class Estoque(models.Model):
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    tamanho = models.CharField(max_length=1, choices=(('P', 'Pequeno'), ('G', 'Grande'), ('S', 'Sopa')))
    qtd = models.PositiveSmallIntegerField()
    data_fabricacao = models.DateField()


    def __str__(self):
        return str(self.id)


class Pedido(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200, default="a")
    data = models.DateField(auto_now=True)
    valortotal = models.FloatField(default=None, null=True)

    def __str__(self):
        return str(self.nome)


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    prato = models.CharField(max_length=200)
    tamanho = models.CharField(max_length=1, choices=(('P', 'Pequeno'), ('G', 'Grande'), ('S', 'Sopa')))
    qtd = models.PositiveSmallIntegerField()
    data_pedido = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.pedido)


class EstoqueCheck(models.Model):
    source = models.CharField(max_length=200)
    sourceid = models.SmallIntegerField()
    prato = models.CharField(max_length=200)
    tamanho = models.CharField(max_length=1)
    qtd = models.SmallIntegerField()

class Frete(models.Model):
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    valorfrete = models.FloatField()

    def __str__(self):
        return str(self.bairro)

from django.db import models


# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    cpf = models.CharField(max_length=200)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return str(self.nome)


class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)

    def __str__(self):
        return self.endereco


class Prato(models.Model):
    prato = models.CharField(max_length=200)
    pratonumero = models.SmallIntegerField()
    tamanho = models.CharField(max_length=1, choices=(('p', 'Pequeno'), ('g', 'Grande'), ('s', 'Sopa')))
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.prato + ' - ' + self.tamanho)


class Preco(models.Model):
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    preco = models.DecimalField(decimal_places=2, max_digits=4)
    data_ativo = models.DateField(
        auto_now_add=True)  # A data a partir da qual tamanho e preço são validos para cada prato.

    def ___str__(self):
        return self.prato


class Estoque(models.Model):
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    tamanho = models.CharField(max_length=1, choices=(('p', 'Pequeno'), ('g', 'Grande'), ('s', 'Sopa')))
    qtd = models.PositiveSmallIntegerField()
    data_fabricacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.prato


class Pedido(models.Model):
    nome = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    tamanho = models.CharField(max_length=1, choices=(('p', 'Pequeno'), ('g', 'Grande'), ('s', 'Sopa')))
    qtd = models.PositiveSmallIntegerField()
    data_pedido = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.pedido)

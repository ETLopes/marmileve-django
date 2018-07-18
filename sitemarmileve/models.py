from django.db import models


# Create your models here.

class NumeroProduto(models.Model):
    pratonumero = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.pratonumero)


class Produto(models.Model):
    pratonumero = models.ForeignKey(NumeroProduto, on_delete=models.CASCADE)
    prato = models.CharField(max_length=200)
    tam = models.CharField(max_length=1)
    pub_date = models.DateTimeField('Data de adição')
    ativo = models.BooleanField()

    def __str__(self):
        return self.prato


class Cliente(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    cpf = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nome)


class Endereco(models.Model):
    nome_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)

    def __str__(self):
        return self.endereco


class Pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class ItemPedido(models.Model):
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    prato = models.CharField(max_length=200)
    tamanho = models.CharField(max_length=1)
    qtd = models.PositiveSmallIntegerField()
    data = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.pedido_id)

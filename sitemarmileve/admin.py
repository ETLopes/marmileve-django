from django.contrib import admin

from .models import Prato, Preco, Cliente, Endereco, Pedido, ItemPedido, Estoque, EstoqueCheck


# Register your models here.

class PratoAdmin(admin.ModelAdmin):
    list_display = ['pratonumero', 'prato',  'active']

    class Meta:
        model = Prato


class PrecoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tamanho', 'preco', 'data_ativo']

    class Meta:
        model = Preco


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'telefone', 'cpf']

    class Meta:
        model = Cliente


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'endereco', 'numero', 'complemento', 'bairro', 'cidade']

    class Meta:
        model = Endereco


class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'endereco', 'data']

    class Meta:
        model = Pedido


class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'id', 'prato', 'tamanho', 'qtd', 'data_pedido']

    class Meta:
        model = ItemPedido

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ['prato', 'tamanho', 'qtd', 'data_fabricacao']

class EstoqueCheckAdmin(admin.ModelAdmin):
    list_display = ['source', 'sourceid', 'prato', 'tamanho', 'qtd']

    class Meta:
        model = EstoqueCheck


admin.site.register(Prato, PratoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)
admin.site.register(Preco, PrecoAdmin)
admin.site.register(Estoque, EstoqueAdmin)
admin.site.register(EstoqueCheck, EstoqueCheckAdmin)

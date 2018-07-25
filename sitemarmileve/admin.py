from django.contrib import admin

from .models import Prato, Preco, Cliente, Endereco, Pedido, ItemPedido, Estoque


# Register your models here.

class PratoAdmin(admin.ModelAdmin):
    list_display = ['id', 'prato', 'pratonumero', 'tamanho', 'active']

    class Meta:
        model = Prato


class PrecoAdmin(admin.ModelAdmin):
    list_display = ['id', 'prato', 'preco', 'data_ativo']

    class Meta:
        model = Preco


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'cpf']

    class Meta:
        model = Cliente


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'endereco', 'numero', 'complemento', 'bairro', 'cidade']

    class Meta:
        model = Endereco


class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'endereco']

    class Meta:
        model = Pedido


class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'id', 'prato', 'tamanho', 'qtd', 'data_pedido']

    class Meta:
        model = ItemPedido


admin.site.register(Prato, PratoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)
admin.site.register(Preco, PrecoAdmin)
admin.site.register(Estoque)

from django.contrib import admin

from .models import NumeroProduto, Cliente, Endereco, Produto, Pedido, ItemPedido


# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['prato', '__str__', 'tam_text', 'pub_date', 'ativo']

    class Meta:
        model = Produto

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'cpf']

    class Meta:
        model = Pedido

class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ['id','pedido', 'prato', 'tamanho', 'qtd', 'data']

    class Meta:
        model = ItemPedido

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id','nome_text', 'email', 'cpf']

    class Meta:
        model = Cliente


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Endereco)
admin.site.register(NumeroProduto)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido,ItemPedidoAdmin)

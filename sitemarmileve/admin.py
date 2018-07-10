from django.contrib import admin

from .models import NumeroProduto, Cliente, Endereco, Produto

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['prato', '__str__', 'tam_text', 'pub_date', 'ativo']
    class Meta:
        model = Produto


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(NumeroProduto)

from django.contrib import admin

from .models import NumeroProduto, Cliente, Endereco, Produto

# Register your models here.

admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(NumeroProduto)

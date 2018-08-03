from django.urls import path

from sitemarmileve.views import index, cliente, cliente_create, endereco_create, cliente_lookup, pratos, product_list_view, addpedido, additem, cliente_success

urlpatterns = [
    path('', index, name='index'),
    path('cliente/', cliente, name='clientes'),
    path('cliente/cliente_create/', cliente_create, name='create_clientes'),
    path('cliente/cliente_create/<int:id>/endereco_create/', endereco_create),
    path('cliente/cliente_create/<int:id>/endereco_create/cliente_success/', cliente_success),
    path('cliente/cliente_lookup/', cliente_lookup),
    path('pratos/', pratos, name='pratos'),
    path('productview/', product_list_view),
    path('addpedido/', addpedido),
    path('addpedido/additem/<int:id>/', additem)

]

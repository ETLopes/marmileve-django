from django.urls import path

from sitemarmileve.views import index, pratos, cliente, cliente_create_view, cliente_lookup, product_list_view, addpedido, additem

urlpatterns = [
    path('', index, name='index'),
    path('pratos/', pratos, name='pratos'),
    path('clientes/', cliente, name='clientes'),
    path('create_clientes/',cliente_create_view, name='create_clientes'),
    path('clientelookup/<int:my_id>/',cliente_lookup),
    path('productview/',product_list_view),
    path('addpedido/', addpedido),
    path('addpedido/additem/<int:id>/', additem)

]

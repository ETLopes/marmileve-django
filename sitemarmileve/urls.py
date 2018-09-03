from django.urls import path

from sitemarmileve.views import (index,
                                 cliente,
                                 cliente_create,
                                 endereco_create,
                                 cliente_lookup,
                                 cliente_success,
                                 pedido,
                                 pedido_create,
                                 pedidoitem_create,
                                 pedido_success,
                                 pedido_remove,
                                 pedido_lookup,
                                 estoque,
                                 estoque_create,
                                 estoque_sucess,
                                 estoque_lookup,
                                 pratos,
                                 product_list_view,
                                 )

urlpatterns = [
    path('', index, name='index'),
    path('cliente/', cliente, name='clientes'),
    path('cliente/cliente_create/', cliente_create, name='create_clientes'),
    path('cliente/cliente_create/<int:id>/endereco_create/', endereco_create),
    path('cliente/cliente_create/<int:id>/endereco_create/cliente_success/', cliente_success),
    path('cliente/cliente_lookup/', cliente_lookup),
    path('pedido/', pedido),
    path('pedido/pedido_create/', pedido_create),
    path('pedido/pedido_create/<int:id>/pedidoitem_create/', pedidoitem_create),
    path('pedido/pedido_create/<int:id>/pedidoitem_create/pedido_success/', pedido_success),
    path('pedido/pedido_remove/', pedido_remove),
    path('pedido/pedido_lookup/', pedido_lookup),
    path('estoque/', estoque),
    path('estoque/estoque_create/', estoque_create),
    path('estoque/estoque_create/estoque_success/', estoque_sucess),
    path('estoque/estoque_lookup/', estoque_lookup),
    path('pratos/', pratos, name='pratos'),
    path('productview/', product_list_view),
]

from django.urls import path

from sitemarmileve.views import index, cliente, pratos, cliente_create, cliente_lookup, product_list_view, addpedido, \
    additem

urlpatterns = [
    path('', index, name='index'),
    path('cliente/', cliente, name='clientes'),
    path('pratos/', pratos, name='pratos'),
    path('cliente/cliente_create/', cliente_create, name='create_clientes'),
    path('cliente/cliente_lookup/', cliente_lookup),
    path('productview/', product_list_view),
    path('addpedido/', addpedido),
    path('addpedido/additem/<int:id>/', additem)

]

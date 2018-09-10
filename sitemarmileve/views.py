from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClienteForm, PedidoForm, AddItemForm, EnderecoForm, EstoqueForm
from .models import Cliente, Pedido, ItemPedido, Prato, Endereco, Estoque, EstoqueCheck, Preco, Frete
from django.db.models import Sum

"""Página Inicial"""


def index(request):
    template_name = 'sitemarmileve/index.html'
    context = {}
    return render(request, template_name, context)


"""

    Início - Criação e visualização de dados de clientes

"""


def cliente(request):
    template_name = 'sitemarmileve/cliente.html'
    context = {}
    return render(request, template_name, context)


def cliente_create(request):
    form = ClienteForm(request.POST or None)
    context = {'form': form}
    template_name = 'sitemarmileve/cliente_create.html'
    if form.is_valid():
        form.save()
        nome = request.POST.get('nome')
        obj = Cliente.objects.get(nome=nome)
        id = obj.id
        return redirect(str(id) + '/endereco_create/')

    return render(request, template_name, context)


def endereco_create(request, id):
    template_name = 'sitemarmileve/endereco_create.html'
    obj_cliente = get_object_or_404(Cliente, pk=id)

    if request.method == 'GET':
        form = EnderecoForm()

    else:
        form = EnderecoForm(request.POST or None)
        if form.is_valid():
            endereco = request.POST.get('endereco')
            numero = request.POST.get('numero')
            complemento = request.POST.get('complemento')
            bairro = request.POST.get('bairro')
            cidade = request.POST.get('cidade')
            formulario = Endereco(endereco=endereco, numero=numero, complemento=complemento, bairro=bairro,
                                  cidade=cidade, cliente_id=id, endereco_ativo=True)
            formulario.save()
            return redirect('cliente_success/')

    context = {'obj_cliente': obj_cliente,
               'form': form,
               }

    return render(request, template_name, context)


def cliente_success(request, id):
    obj_cliente = get_object_or_404(Cliente, pk=id)
    obj_endereco = get_object_or_404(Endereco, cliente_id=id)

    template_name = 'sitemarmileve/cliente_success.html'

    return render(request, template_name, {'obj_cliente': obj_cliente, 'obj_endereco': obj_endereco})


def cliente_lookup(request):
    template_name = 'sitemarmileve/cliente_lookup.html'
    cliente = Cliente.objects.all().order_by('nome')
    endereco = []

    if request.method == 'POST':
        nome = request.POST.get('nome')
        print(nome)
        cliente_select = Cliente.objects.get(nome=nome)
        endereco = Endereco.objects.filter(cliente_id=cliente_select.id)

        context = {'cliente': cliente,
                   'endereco': endereco,
                   'cliente_select': cliente_select
                   }

        return render(request, template_name, context)

    context = {'cliente': cliente,
               'endereco': endereco,
               }

    return render(request, template_name, context)


"""

    Fim - Criação e visualização de dados de clientes

"""

"""
    
    Início - Criação e visualização de pedidos
    
"""


def pedido(request):
    template_name = 'sitemarmileve/pedido.html'
    context = {}

    return render(request, template_name, context)


def pedido_create(request):
    template_name = 'sitemarmileve/pedido_create.html'
    form = PedidoForm()
    nome_lista = Cliente.objects.all().order_by('nome')
    context = {
        'form': form,
        'nome': nome_lista
    }

    if request.method == 'POST':
        form = PedidoForm()

        nome = request.POST.get('dropdown_nome')
        nome_lista = Cliente.objects.filter(nome=nome)
        nome_lista2 = Cliente.objects.get(nome=nome)

        endereco_lista = Endereco.objects.filter(cliente_id=nome_lista2.id)

        context = {'form': form,
                   'nome': nome_lista,
                   'endereco': endereco_lista}

        if request.POST.get('dropdown_endereco') == None:
            return render(request, template_name, context)
        else:
            print(request.POST.get('dropdown_endereco'))
            endereco_nome = request.POST.get('dropdown_endereco')
            form_pedido = Pedido(nome=nome, endereco=endereco_nome)
            form_pedido.save()
            return redirect(str(form_pedido.id) + '/' + 'pedidoitem_create/')

    return render(request, template_name, context)


def pedidoitem_create(request, id):
    template_name = 'sitemarmileve/pedidoitem_create.html'
    form = AddItemForm()
    pedidos = get_object_or_404(Pedido, pk=id)
    prod = Prato.objects.filter(active=True).order_by('pratonumero')

    tamanho = ["P", "G", "S"]
    qtd = range(1, 41)

    context = {'form': form,
               'pedidos': pedidos,
               'produtos': prod,
               'tamanho': tamanho,
               'qtd': qtd,

               }

    if request.method == 'POST':
        prato = request.POST.get('dropdown_prato')
        tamanho = request.POST.get('dropdown_tamanho')

        qtd = request.POST.get('dropdown_qtd')
        formulario = ItemPedido(prato=prato, tamanho=tamanho, qtd=qtd, pedido_id=id)
        formulario.save()
        itempedido = ItemPedido.objects.filter(pedido_id=id)
        context['itempedido'] = itempedido
        return render(request, template_name, context)

    return render(request, template_name, context)


def pedido_remove(request):
    template_name = 'sitemarmileve/pedido_remove.html'
    pedidos = Pedido.objects.all()
    item = ItemPedido.objects.all()
    context = {'pedidos': pedidos,
               'item': item}

    if request.method == 'POST':
        id = request.POST.get('dropdown_id')
        detalhes = ItemPedido.objects.filter(pedido_id=id)

        context = {'pedidos': pedidos,
                   'item': item,
                   'detalhes': detalhes}

    return render(request, template_name, context)


def pedido_success(request, id):
    template_name = 'sitemarmileve/pedido_success.html'
    pedido = Pedido.objects.get(pk=id)
    cliente = Cliente.objects.get(nome=pedido.nome)
    itempedido = ItemPedido.objects.filter(pedido_id=id)
    preco = Preco.objects.all()
    #endereco = Endereco.objects.get(endereco=pedido.endereco)

    def valortotal(itempedido):
        soma = 0.00
        qtd = 0
        for i in itempedido:
            for j in preco:
                if i.tamanho == j.tamanho:
                    soma += (j.preco * i.qtd)
                    qtd += int(i.qtd)
        print(qtd)
        if qtd >= 25:
            soma = (float(soma) * 0.85)
        elif qtd >= 15:
            soma = (float(soma) * 0.9)


        get_bairro = Endereco.objects.filter(endereco=pedido.endereco)
        for i in get_bairro:
            bairro = i.bairro
        frete = Frete.objects.get(bairro=bairro)
        print(frete)
        pedido.valortotal = (float(soma)) + float(frete.valorfrete)
        pedido.save()

        return pedido.valortotal

    context = {
        'cliente': cliente,
        'pedido': pedido,
        'itempedido': itempedido,
        'valortotal': valortotal(itempedido),

    }

    return render(request, template_name, context)


def pedido_lookup(request):
    template_name = 'sitemarmileve/pedido_lookup.html'
    pedidos = Pedido.objects.all()

    if request.method == 'POST':
        pedidoid = request.POST.get('dropdown_id')
        pedidos2 = Pedido.objects.get(id=pedidoid)
        dadoscliente = Cliente.objects.get(nome=pedidos2.nome)
        itempedido = ItemPedido.objects.filter(pedido_id=pedidoid)
        context = {'pedidos': pedidos,
                   'pedidos2': pedidos2,
                   'dadoscliente': dadoscliente,
                   'itempedido': itempedido}

        return render(request, template_name, context)

    context = {'pedidos': pedidos}
    return render(request, template_name, context)


"""

    Fim - Criação e visualização de pedidos

"""

"""
__________________________________________________

    Início - Criação e visualização de Estoque
__________________________________________________

"""


def estoque(request):
    template_name = 'sitemarmileve/estoque.html'

    return render(request, template_name, context={})


def estoque_create(request):
    template_name = 'sitemarmileve/estoque_create.html'

    form = EstoqueForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect('estoque_success/')

    return render(request, template_name, context)


def estoque_sucess(request):
    template_name = 'sitemarmileve/estoque_success.html'

    return render(request, template_name, context={})


def estoque_lookup(request):
    template_name = 'sitemarmileve/estoque_lookup.html'
    estoque = Estoque.objects.all()
    pedidos = ItemPedido.objects.all()
    conciliado = EstoqueCheck.objects.all()

    conciliado_estoque = []
    conciliado_pedidos = []

    for i in conciliado:
        if i.source == 'estoque':
            conciliado_estoque.append(i.sourceid)
        else:
            conciliado_pedidos.append(i.sourceid)

    for i in pedidos:
        if i.id not in conciliado_pedidos:
            for j in range(0, i.qtd):
                form_pedidos = EstoqueCheck(source='pedidos',
                                            sourceid=i.id,
                                            prato=i.prato,
                                            tamanho=i.tamanho,
                                            qtd=-1
                                            )
                form_pedidos.save()

    for i in estoque:
        if i.id not in conciliado_estoque:
            for j in range(0, i.qtd):
                form_estoque = EstoqueCheck(source='estoque',
                                            sourceid=i.id,
                                            prato=i.prato,
                                            tamanho=i.tamanho,
                                            qtd=1
                                            )
                form_estoque.save()

    form = EstoqueCheck.objects.values('prato', 'tamanho').annotate(sum=Sum('qtd'))
    pratos = Prato.objects.all()

    context = {'form': form,
               'pratos': pratos}

    return render(request, template_name, context)


"""

    Fim - Criação e visualização de Estoque

"""


# listas abaixo


def pratos(request, produtos):
    template_name_name = 'sitemarmileve/pratos.html'

    return render(request, template_name_name, {'my_context': produtos})


def product_list_view(request):
    queryset = Cliente.objects.all()
    context = {'object_list': queryset}
    template_name = 'sitemarmileve/productview.html'
    return render(request, template_name, context)

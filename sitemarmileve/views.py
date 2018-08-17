from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClienteForm, PedidoForm, AddItemForm, EnderecoForm, EstoqueForm
from .models import Cliente, Pedido, ItemPedido, Prato, Endereco, Estoque, EstoqueCheck
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
    endereco = []
    if request.method == 'GET':
        form = ClienteForm()
    else:
        nome = request.POST.get('nome')
        obj = Cliente.objects.get(nome=nome)
        id = obj.id
        for i in (Endereco.objects.filter(cliente_id=id)):
            endereco.append(i)

        form = ClienteForm(instance=obj, )

    context = {'form': form,
               'endereco': endereco
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
    nome_lista = []
    for i in Cliente.objects.all():
        print(i.nome)
        nome_lista.append(i.nome)
    context = {
        'form': form,
        'nome': nome_lista
    }

    if request.method == 'POST':
        form = PedidoForm()

        endereco_lista = []
        nome_lista = []

        nome = request.POST.get('dropdown_nome')
        nome_lista.append(nome)
        nome2 = Cliente.objects.get(nome=nome)
        nome_id = nome2.id
        endereco = Endereco.objects.filter(cliente_id=nome_id)

        for i in endereco:
            endereco_lista.append(i.endereco)
        context = {'form': form,
                   'nome': nome_lista,
                   'endereco': endereco_lista}

        if request.POST.get('dropdown_endereco') == None:
            print('número um')
            print(request.POST.get('dropdown_endereco'))
            return render(request, template_name, context)
        else:
            print('número 2')
            print(nome)
            print(nome2.nome)
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
    prod = Prato.objects.all()

    def lista_produtos(prod):
        lista = []
        for i in prod:
            if i.prato not in lista:
                lista.append(i.prato)
        return sorted(lista)

    tamanho = ["P", "G", "S"]
    qtd = range(1, 21)

    listaprodutos = lista_produtos(prod)

    context = {'form': form,
               'pedidos': pedidos,
               'produtos': listaprodutos,
               'tamanho': tamanho,
               'qtd': qtd,

               }

    if request.method == 'POST':
        prato = request.POST.get('dropdown_prato')
        tamanho = request.POST.get('dropdown_tamanho')
        print(tamanho)
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
    return render(request, template_name, context)


def pedido_success(request, id):
    template_name = 'sitemarmileve/pedido_success.html'
    pedido = Pedido.objects.get(pk=id)
    cliente = Cliente.objects.get(nome=pedido.nome)
    itempedido = ItemPedido.objects.filter(pedido_id=id)
    context = {
        'cliente': cliente,
        'pedido': pedido,
        'itempedido': itempedido,
    }

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
    print(form)

    context = {'form': form}

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

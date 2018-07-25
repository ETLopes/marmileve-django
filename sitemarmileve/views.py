from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClienteForm, AddPedidoForm, AddItemForm
from .models import Cliente, Pedido, ItemPedido, Prato, Endereco

clientes = Cliente.objects.all()
produtos = Prato.objects.all()


def listaclientes(clientes):
    lista = []
    for i in clientes:
        if i.nome not in lista:
            lista.append(i.nome)
    return sorted(lista)


def listaemail(clientes):
    lista = []
    for i in clientes:
        if i.email not in lista:
            lista.append(i.email)
    return sorted(lista)


def listacpf(clientes):
    lista = []
    for i in clientes:
        if i.cpf not in lista:
            lista.append(i.cpf)
    return sorted(lista)


lista_clientes = listaclientes(clientes)


def index(request):
    template_name = 'sitemarmileve/index.html'
    context = {}
    return render(request, template_name, context)


def cliente(request):
    template = 'sitemarmileve/cliente.html'
    context = {}
    return render(request, template, context)


def cliente_create(request):
    form = ClienteForm(request.POST or None)
    context = {'form': form}
    template = 'sitemarmileve/cliente_create.html'
    if form.is_valid():
        form.save()
    return render(request, template, context)


def cliente_lookup(request):
    template = 'sitemarmileve/cliente_lookup.html'
    endereco = []
    if request.method == 'GET':
        form = ClienteForm()
    else:
        nome = request.POST.get('nome')
        obj = Cliente.objects.get(nome=nome)
        id = obj.id
        for i in (Endereco.objects.filter(cliente_id=id)):
            endereco.append(i)

        form = ClienteForm(instance=obj)


    context = {'cliente': lista_clientes,
               'form': form,
               'endereco': endereco
               }
    print(endereco)
    return render(request, template, context)


def pratos(request, produtos):
    template_name = 'sitemarmileve/pratos.html'

    return render(request, template_name, {'my_context': produtos})


def product_list_view(request):
    queryset = Cliente.objects.all()
    context = {'object_list': queryset}
    template = 'sitemarmileve/productview.html'
    return render(request, template, context)


def addpedido(request):
    template = 'sitemarmileve/addpedido.html'

    lista_clientes = listaclientes(clientes)
    lista_email = listaemail(clientes)
    lista_cpf = listacpf(clientes)

    form = AddPedidoForm()
    nome = request.POST.get('dropdown_cliente')
    email = request.POST.get('dropdown_email')
    cpf = request.POST.get('dropdown_cpf')

    if request.method == 'GET':
        form = AddPedidoForm()
    else:
        formulario = Pedido(nome=nome, email=email, cpf=cpf)
        formulario.save()
        return redirect('additem/' + str(formulario.id) + '/')

    context = {'form': form,
               'clientes': lista_clientes,
               'emails': lista_email,
               'cpfs': lista_cpf
               }
    return render(request, template, context)


def additem(request, id):
    template = 'sitemarmileve/additem.html'
    form = AddItemForm(request.POST or None)
    pedidos = get_object_or_404(Pedido, pk=id)
    prod = Prato.objects.all()

    def lista_produtos(prod):
        lista = []
        for i in prod:
            if i.prato_text not in lista:
                lista.append(i.prato_text)
        return sorted(lista)

    listaprodutos = lista_produtos(prod)

    if request.method == 'GET':
        form = AddItemForm()
    else:
        formulario = ItemPedido(prato=nome, tamanho=email, qtd=cpf)
        formulario.save()
        return redirect('additem/' + str(formulario.id) + '/')

    context = {'form': form,
               'pedidos': pedidos,
               'produtos': listaprodutos
               }
    return render(request, template, context)

# listas abaixo

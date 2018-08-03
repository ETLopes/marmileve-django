from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClienteForm, AddPedidoForm, AddItemForm, EnderecoForm
from .models import Cliente, Pedido, ItemPedido, Prato, Endereco

clientes = Cliente.objects.all()
produtos = Prato.objects.all()


def listaclientes(clientes):
    lista = []
    for i in clientes:
        if i.nome not in lista:
            lista.append(i.nome)
    return sorted(lista)


lista_clientes = listaclientes(clientes)


def index(request):
    template_name = 'sitemarmileve/index.html'
    context = {}
    return render(request, template_name, context)


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
        form = EnderecoForm(request.POST or None, instance=obj_cliente)
        form.save()
        return redirect('cliente_success/')

    context = {'obj_cliente': obj_cliente,
               'form': form,
               }

    return render(request, template_name, context)

def cliente_success(request, id):
    obj_cliente = get_object_or_404(Cliente, pk=id)
    template_name = 'sitemarmileve/cliente_success.html'

    return render(request, template_name, {'obj': obj_cliente})


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

        form = ClienteForm(instance=obj,)

    context = {'cliente': lista_clientes,
               'form': form,
               'endereco': endereco
               }
    return render(request, template_name, context)


def pratos(request, produtos):
    template_name_name = 'sitemarmileve/pratos.html'

    return render(request, template_name_name, {'my_context': produtos})


def product_list_view(request):
    queryset = Cliente.objects.all()
    context = {'object_list': queryset}
    template_name = 'sitemarmileve/productview.html'
    return render(request, template_name, context)


def addpedido(request):
    template_name = 'sitemarmileve/addpedido.html'

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
    return render(request, template_name, context)


def additem(request, id):
    template_name = 'sitemarmileve/additem.html'
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
    return render(request, template_name, context)

# listas abaixo

from django.shortcuts import render, get_object_or_404, redirect

from .forms import RawClienteForm, ClienteForm
from .models import Produto, Cliente


def index(request):
    template_name = 'sitemarmileve/index.html'
    context = {
        'my_text': 'This is my text',
        'my_number': 123,
        'my_list': [123, 456, 689]
    }
    return render(request, template_name, context)


def pratos(request):
    template_name = 'sitemarmileve/pratos.html'
    my_context = Produto.objects.all()
    return render(request, template_name, {'my_context': my_context})


def cliente(request):
    template = 'sitemarmileve/cliente.html'
    cli = Cliente.objects.get(pk=1)
    context = {'cli': cli}
    return render(request, template, context)


def cliente_create_view(request):
    form = ClienteForm(request.POST or None)
    context = {'form': form}
    template = 'sitemarmileve/cliente_create.html'
    if form.is_valid():
        form.save()
    return render(request, template, context)


def cliente_lookup(request, my_id):
    obj = get_object_or_404(Cliente, pk=my_id)
    context = {'object': obj}
    template = 'sitemarmileve/clientelookup.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    return render(request, template, context)


def product_list_view(request):
    queryset = Cliente.objects.all()
    context = {'object_list': queryset}
    template = 'sitemarmileve/productview.html'
    return render(request, template, context)

# Create your views here.

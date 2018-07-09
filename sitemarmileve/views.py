from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
from django.template import loader


def Index(request):
    template_name = 'sitemarmileve/index.html'
    my_list = Produto.objects.get(pk=1)
    return render(request, template_name)

# Create your views here.

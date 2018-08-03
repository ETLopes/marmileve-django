from django import forms

from .models import Cliente, ItemPedido, Endereco


class ClienteForm(forms.ModelForm):
    nome = forms.CharField(max_length=200)
    email = forms.CharField(required=False)
    cpf = forms.CharField(required=False)

    class Meta:
        model = Cliente
        fields = [
            'nome',
            'email',
            'cpf'
        ]

class EnderecoForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = [
            'endereco',
            'numero',
            'complemento',
            'bairro',
            'cidade',
        ]



class AddPedidoForm(forms.Form):
    nome = forms.CharField()
    cpf = forms.CharField(max_length=13)
    email = forms.EmailField()


class AddItemForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = [
            'prato',
            'tamanho',
            'qtd'
        ]

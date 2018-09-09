import datetime

from django import forms

from .models import Cliente, ItemPedido, Endereco, Pedido, Estoque, Frete


class ClienteForm(forms.ModelForm):
    nome = forms.CharField(max_length=200)
    email = forms.CharField(required=False)
    telefone = forms.CharField(max_length=11, required=False)
    cpf = forms.CharField(required=False)

    class Meta:
        model = Cliente
        fields = [
            'nome',
            'email',
            'telefone',
            'cpf'
        ]

class EnderecoForm(forms.ModelForm):

    bairro = forms.ModelChoiceField(queryset=Frete.objects.all(), to_field_name='bairro')
    cidade = forms.ChoiceField(choices=(('Salvador', 'Salvador'),('Lauro de Freitas', 'Lauro de Freitas')))

    class Meta:
        model = Endereco
        fields = [
            'endereco',
            'numero',
            'complemento',
            'bairro',
            'cidade',
        ]



class PedidoForm(forms.Form):

    class Meta:
        model = Pedido
        fields = [
            'nome',
            'endereco',
            'id'
        ]


class AddItemForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = [
            'prato',
            'tamanho',
            'qtd'
        ]

class EstoqueForm(forms.ModelForm):

    data_fabricacao = forms.DateField(initial=datetime.datetime.now)

    class Meta:
        model = Estoque
        fields = [
            'prato',
            'tamanho',
            'qtd',
            'data_fabricacao'
        ]
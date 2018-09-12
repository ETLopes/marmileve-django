import datetime

from django import forms

from .models import Cliente, ItemPedido, Endereco, Pedido, Estoque, Frete, Prato


class ClienteForm(forms.ModelForm):
    nome = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome do cliente'
        }
    ))
    email = forms.CharField(required=False, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite o email do cliente'
        }
    ))

    telefone = forms.CharField(max_length=11, required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite o telefone com DDD sem traços'
        }
    ))
    cpf = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite o CPF do cliente'
        }
    ))

    class Meta:
        model = Cliente
        fields = [
            'nome',
            'email',
            'telefone',
            'cpf'
        ]


class EnderecoForm(forms.ModelForm):
    endereco = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite aqui o endereço'
        }
    ))

    numero = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite aqui o Numero'
        }
    ))

    complemento = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite aqui o complemento'
        }
    ))

    bairro = forms.ModelChoiceField(queryset=Frete.objects.all(), to_field_name='bairro', widget=forms.Select(
        attrs={
            'class': 'form-control'
        })

                                    )
    cidade = forms.ChoiceField(choices=(('Salvador', 'Salvador'), ('Lauro de Freitas', 'Lauro de Freitas')),
                               widget=forms.Select(
                                   attrs={
                                       'class': 'form-control'
                                   }))

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
    prato = forms.ModelChoiceField(queryset=Prato.objects.all().order_by('id'), to_field_name='prato',
                                   widget=forms.Select(
                                       attrs={
                                           'class': 'form-control'
                                       })
                                   )
    tamanho = forms.ChoiceField(choices=(('P', 'Pequeno'), ('G', 'Grande'), ('S', 'Sopa')), widget=forms.Select(
        attrs={
            'class': 'form-control'
        })
                                )
    qtd = forms.CharField(max_length=3, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite aqui a quantidade'
        }
    ))

    data_fabricacao = forms.DateField(initial=datetime.datetime.now, widget=forms.DateInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Estoque
        fields = [
            'prato',
            'tamanho',
            'qtd',
            'data_fabricacao'
        ]

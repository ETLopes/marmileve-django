from django import forms

from .models import Cliente, Produto


class ClienteForm(forms.ModelForm):
    nome_text = forms.CharField(widget=forms.TextInput({'placeholder': 'special'}))

    class Meta:
        model = Cliente
        fields = [
            'nome_text',
            'cpf'
        ]

    def clean_cpf(self, *args, **kwargs):
        cpf = self.cleaned_data.get('cpf')
        if '123' in cpf:
            return cpf
        else:
            raise forms.ValidationError('This is not a valid cpf')

class RawClienteForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput({'placeholder': 'special'}))
    cpf = forms.CharField()

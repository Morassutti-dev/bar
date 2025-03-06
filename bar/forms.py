from django import forms
from .models import ItemComanda, Produto, Comanda

class AdicionarItemForm(forms.ModelForm):
    produto = forms.ModelChoiceField(queryset=Produto.objects.all(), label="Produto")
    quantidade = forms.IntegerField(min_value=1, label="Quantidade")

    class Meta:
        model = ItemComanda
        fields = ['produto', 'quantidade']


class EditarComandaForm(forms.ModelForm):
    class Meta:
        model = Comanda
        fields = ['status'] 

class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Comanda
        fields = ['cliente'] 

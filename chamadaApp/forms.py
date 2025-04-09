from django import forms
from chamadaApp.models import Categoria,Plano,Telefone,Cliente

class TelefoneForms(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = '__all__'
class CategoriaForms(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
class PlanoForms(forms.ModelForm):
    class Meta:
        model = Plano
        fields = '__all__'
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
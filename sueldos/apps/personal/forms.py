from .models import Personal
from django import forms

class AgregarPersonal(forms.ModelForm):
    nombre = forms.CharField(required=True, max_length=250, label='Nombre')
    cbu = forms.CharField( required=True, max_length=250, label='Cbu')

    class Meta:
        model = Personal
        fields = ['nombre', 'cbu']
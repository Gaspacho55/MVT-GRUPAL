from django import forms


class DeporteForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=50)

class ProfeForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    deporte= forms.CharField(max_length=50)
    categoria= forms.CharField(max_length=50)
    nacimiento=forms.CharField(max_length=50)
    

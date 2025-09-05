from django import forms


class LearnForm(forms.Form):
    character = forms.CharField(max_length=300,label="¿En qué personaje estabas pensando?")
    difference = forms.CharField(max_length=1500,label="¿Cuál es la diferencia?")
from django import forms
from .models import Marca, Vehiculo

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=50, label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")


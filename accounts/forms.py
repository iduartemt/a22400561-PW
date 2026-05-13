from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistoForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Escolhe os campos que queres que apareçam no formulário de registo
        fields = ("username", "email", "first_name", "last_name") 

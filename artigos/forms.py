from django import forms
from .models import Artigo, Comentario, Rating

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'texto', 'fotografia', 'link_externo']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor_nome', 'texto']
        labels = {
            'autor_nome': 'O teu nome (se não tiveres sessão iniciada)',
            'texto': 'O teu comentário',
        }
        widgets = {
            'autor_nome': forms.TextInput(attrs={'placeholder': 'Ex: João Silva'}),
            'texto': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escreve aqui o teu comentário...'}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['valor']
        labels = {
            'valor': 'Dá uma classificação de 1 a 5 estrelas',
        }
        widgets = {
            'valor': forms.Select(attrs={'class': 'rating-select'}),
        }

from django.db import models
from django.utils import timezone
import secrets


def generate_api_key():
    # Gera uma chave segura e aleatória
    return secrets.token_urlsafe(32)


# modelo para guardar e gerir chaves de acesso
class APIKey(models.Model):
    name = models.CharField(max_length=100, help_text="Nome de quem vai usar a chave")
    key = models.CharField(max_length=255, unique=True, default=generate_api_key)
    is_active = models.BooleanField(default=True)
    expiration_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {'Ativa' if self.is_active else 'Inativa'}"

    def is_valid(self):
        # Verifica se a chave está ativa e se ainda não expirou
        return self.is_active and self.expiration_date > timezone.now()
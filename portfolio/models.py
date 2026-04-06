from django.db import models

# Create your models here.
class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20)
    descricao = models.TextField()
    duracao_anos = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    pagina_lusofona = models.URLField()

    def __str__(self):
        return self.nome
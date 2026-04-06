from django.db import models

# Create your models here.
#Licenciatura
class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20)
    descricao = models.TextField()
    duracao_anos = models.IntegerField()

    def __str__(self):
        return self.nome

#Docente    
class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    pagina_lusofona = models.URLField()

    def __str__(self):
        return self.nome
    

#unidade Curricular
class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()

    licenciatura = models.ForeignKey(
        Licenciatura,
        on_delete=models.CASCADE,
        related_name='ucs'
    )

    docentes = models.ManyToManyField(
        Docente,
        related_name='ucs'
    )

    def __str__(self):
        return self.nome
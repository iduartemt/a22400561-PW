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
    
#Tecnologia
class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descricao = models.TextField()
    website_oficial = models.URLField()

    def __str__(self):
        return self.nome
    
#Competencias
class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    nivel = models.IntegerField()

    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name='competencias',
        blank=True
    )

    def __str__(self):
        return self.nome
    
#Formacao
class Formacao(models.Model):
    titulo = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    licenciatura = models.ForeignKey(
        Licenciatura,
        on_delete=models.CASCADE,
        related_name='formacoes'
    )

    competencias = models.ManyToManyField(
        Competencia,
        related_name='formacoes',
        blank=True
    )

    def __str__(self):
        return self.titulo
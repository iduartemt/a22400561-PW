from django.db import models

# Create your models here.
# ----------------------------LICENCIATURA---------------------------- 
class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20)
    descricao = models.TextField()
    duracao_anos = models.IntegerField()
    diploma_degree = models.CharField(max_length=50, blank=True)
    course_code = models.IntegerField(blank=True, null=True)
    reasons = models.JSONField(blank=True, null=True)  # Lista de razões para escolher o curso

    def __str__(self):
        return self.nome

# ----------------------------DOCENTE---------------------------- 
class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    imagem = models.ImageField(upload_to='docentes/', blank=True)
    pagina_lusofona = models.URLField(blank=True)
    
    # Campos adicionais dos dados Lusófona
    card_code = models.IntegerField(blank=True, null=True, unique=True)
    degree = models.CharField(max_length=50, blank=True)
    employee_code = models.IntegerField(blank=True, null=True)
    regimen = models.CharField(max_length=50, blank=True)
    ciencia_vitae = models.CharField(max_length=20, blank=True)
    orcid = models.CharField(max_length=20, blank=True)
    academic_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome
    

# ----------------------------UNIDADE CURRICULAR---------------------------- 
class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    curricular_unit_code = models.IntegerField(unique=True, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True)
    nature = models.CharField(max_length=20, blank=True)
    type = models.CharField(max_length=20, blank=True)
    internship = models.CharField(max_length=10, blank=True)
    objectives = models.TextField(blank=True)
    programme = models.TextField(blank=True)
    presentation = models.TextField(blank=True)
    bibliography = models.TextField(blank=True)
    assessment = models.TextField(blank=True)
    methodology = models.TextField(blank=True)
    organic_unit = models.CharField(max_length=100, blank=True)
    group_code = models.IntegerField(blank=True, null=True)
    institution_code = models.IntegerField(blank=True, null=True)

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
    
# ----------------------------TECNOLOGIA---------------------------- 
class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descricao = models.TextField()
    website_oficial = models.URLField()

    def __str__(self):
        return self.nome
    
# ----------------------------COMPETENCIA---------------------------- 
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
    
# ----------------------------FORMAÇÃO---------------------------- 
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
    
# ----------------------------PROJETOS---------------------------- 
class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    ano = models.IntegerField()
    github_url = models.URLField()

    unidade_curricular = models.ForeignKey(
        UnidadeCurricular,
        on_delete=models.CASCADE,
        related_name='projetos'
    )

    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name='projetos'
    )

    competencias = models.ManyToManyField(
        Competencia,
        related_name='projetos',
        blank=True
    )

    def __str__(self):
        return self.titulo
    
# ----------------------------TFC---------------------------- 
class TFC(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=100, blank=True, null=True)
    
    # Relação com o modelo Docente
    orientador = models.ForeignKey(
        Docente,
        on_delete=models.SET_NULL, # Se apagares o docente da BD, o TFC não é apagado (o orientador passa a Null)
        related_name='tfcs_orientados',
        blank=True, 
        null=True
    )
    
    curso = models.CharField(max_length=150, blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    resumo = models.TextField(blank=True, null=True)
    palavras_chave = models.CharField(max_length=250, blank=True, null=True)
    
    area = models.CharField(max_length=100, blank=True, null=True)
    destaque = models.BooleanField(default=False)

    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name='tfcs',
        blank=True
    )

    competencias = models.ManyToManyField(
        Competencia,
        related_name='tfcs',
        blank=True
    )

    def __str__(self):
        return self.titulo
    
# ----------------------------ALUNO---------------------------- 
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.TextField()


    def __str__(self):
        return self.nome
    
# ----------------------------MAKING OF---------------------------- 
class MakingOf(models.Model):
    titulo = models.CharField(max_length=100)
    entidade = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='makingof/', blank=True)
    descricao_processo = models.TextField(blank=True)
    decisoes_tomadas = models.TextField(blank=True)
    erros_correcao = models.TextField(blank=True)
    justificacao_modelacao = models.TextField(blank=True)
    uso_ia = models.TextField(blank=True)
    evidencia = models.CharField(max_length=255, blank=True)
    data = models.DateField()
    tipo_registo = models.CharField(max_length=50)
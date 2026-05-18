from django.db import models
from django.contrib.auth.models import User

class Artigo(models.Model):
    titulo = models.CharField(max_length=200, help_text="Título do artigo")
    texto = models.TextField(help_text="Conteúdo do artigo (podes usar Markdown se quiseres)")
    fotografia = models.ImageField(upload_to='artigos_fotos/', blank=True, null=True, help_text="Imagem de destaque")
    link_externo = models.URLField(max_length=500, blank=True, null=True, help_text="Link externo opcional (ex: fonte ou vídeo)")
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    # O autor tem de ser um utilizador do sistema (do grupo bloggers, mas essa validação fazemos nas views)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artigos_escritos')
    
    # Para o sistema de likes (muitos utilizadores podem gostar de muitos artigos)
    likes = models.ManyToManyField(User, related_name='artigos_gostados', blank=True)

    def numero_de_likes(self):
        return self.likes.count()

    def media_ratings(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(r.valor for r in ratings) / ratings.count(), 1)
        return 0.0

    def __str__(self):
        return f"{self.titulo} - por {self.autor.username}"


class Comentario(models.Model):
    # O artigo ao qual este comentário pertence
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    
    # Quem escreveu o comentário (pode ser um utilizador registado ou anónimo)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios_escritos', null=True, blank=True)
    autor_nome = models.CharField(max_length=100, default='Anónimo', help_text="Nome exibido se não estiver autenticado")
    
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        nome = self.autor.username if self.autor else self.autor_nome
        return f"Comentário de {nome} no artigo: {self.artigo.titulo}"


class Rating(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='ratings')
    valor = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], help_text="Pontuação de 1 a 5")
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating {self.valor} no artigo: {self.artigo.titulo}"

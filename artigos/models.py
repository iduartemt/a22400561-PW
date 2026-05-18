from django.db import models
from django.contrib.auth.models import User

class Artigo(models.Model):
    titulo = models.CharField(max_length=200, help_text="Título do artigo")
    texto = models.TextField(help_text="Conteúdo do artigo (podes usar Markdown se quiseres)")
    fotografia = models.ImageField(upload_to='artigos_fotos/', blank=True, null=True, help_text="Imagem de destaque")
    link_externo = models.URLField(max_length=500, blank=True, null=True, help_text="Link externo opcional (ex: fonte ou vídeo)")
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    # O autor tem de ser um utilizador do sistema (do grupo autores, mas essa validação fazemos nas views)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artigos_escritos')
    
    # Para o sistema de likes (muitos utilizadores podem gostar de muitos artigos)
    likes = models.ManyToManyField(User, related_name='artigos_gostados', blank=True)

    def numero_de_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.titulo} - por {self.autor.username}"


class Comentario(models.Model):
    # O artigo ao qual este comentário pertence
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    
    # Quem escreveu o comentário (só autenticados)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios_escritos')
    
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username} no artigo: {self.artigo.titulo}"

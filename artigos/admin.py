from django.contrib import admin
from .models import Artigo, Comentario, Rating

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao', 'media_ratings')
    search_fields = ('titulo', 'texto')
    list_filter = ('data_criacao', 'autor')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'autor', 'autor_nome', 'data_criacao')
    search_fields = ('texto', 'autor_nome')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'valor', 'data_criacao')
    list_filter = ('valor', 'data_criacao')

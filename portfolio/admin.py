from django.contrib import admin
from .models import Licenciatura, Docente, UnidadeCurricular, Tecnologia

# Register your models here.
@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'duracao_anos')
    search_fields = ('nome', 'sigla', 'descricao')
    list_filter = ('duracao_anos',)

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'pagina_lusofona')
    search_fields = ('nome', 'email')

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects', 'licenciatura')
    search_fields = ('nome',)
    list_filter = ('ano', 'semestre')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'website_oficial')
    search_fields = ('nome', 'tipo')
    list_filter = ('tipo',)
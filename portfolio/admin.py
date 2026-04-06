from django.contrib import admin
from .models import Licenciatura

# Register your models here.
@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'duracao_anos')
    search_fields = ('nome', 'sigla', 'descricao')
    list_filter = ('duracao_anos',)
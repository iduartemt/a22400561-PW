# Views do Django para renderizar as páginas do portfolio.
# Aqui carregamos os dados dos modelos e enviamos para os templates.
from django.shortcuts import render, get_object_or_404
from .models import Licenciatura, UnidadeCurricular

# Página inicial: lista o curso e organiza as UCs por ano.
def home(request):
    licenciatura = Licenciatura.objects.first()
    ucs_por_ano = {}
    for uc in UnidadeCurricular.objects.all().order_by('ano', 'semestre', 'nome'):
        ano = uc.ano
        if ano not in ucs_por_ano:
            ucs_por_ano[ano] = []
        ucs_por_ano[ano].append(uc)
    
    context = {
        'licenciatura': licenciatura,
        'ucs_por_ano': ucs_por_ano,
    }
    return render(request, 'portfolio/home.html', context)

# Página de detalhe do curso: mostra informação geral do curso.
def curso_detail(request):
    licenciatura = get_object_or_404(Licenciatura)
    context = {
        'licenciatura': licenciatura,
    }
    return render(request, 'portfolio/curso_detail.html', context)

def uc_detail(request, uc_id):
    uc = get_object_or_404(UnidadeCurricular, pk=uc_id)
    context = {
        'uc': uc,
    }
    return render(request, 'portfolio/uc_detail.html', context)

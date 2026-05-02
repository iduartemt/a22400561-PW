# Views do Django para renderizar as páginas do portfolio.
# Aqui carregamos os dados dos modelos e enviamos para os templates.
from django.shortcuts import render, get_object_or_404
from .models import Licenciatura, UnidadeCurricular, Projeto, Tecnologia, TFC, Docente

def home(request):
    # Página inicial passa a ser apenas um menu global, já não precisa de carregar a licenciatura
    return render(request, 'portfolio/home.html')

# Página com a lista de todos os cursos
def cursos_view(request):
    cursos = Licenciatura.objects.all()
    context = {
        'cursos': cursos,
    }
    return render(request, 'portfolio/cursos.html', context)

# Página de detalhe de um curso específico: precisa do ID
def curso_detail(request, curso_id):
    licenciatura = get_object_or_404(Licenciatura, pk=curso_id)

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

## Adiciona esta nova função para as UCs
def ucs_view(request):
    #buscar a lógica de agrupar por anos que tinhas na home
    ucs_por_ano = {}
    for uc in UnidadeCurricular.objects.all().order_by('ano', 'semestre', 'nome'):
        ano = uc.ano
        if ano not in ucs_por_ano:
            ucs_por_ano[ano] = []
        ucs_por_ano[ano].append(uc)
    
    context = {
        'ucs_por_ano': ucs_por_ano,
    }
    # Mandamos os dados para um novo ficheiro chamado ucs.html
    return render(request, 'portfolio/ucs.html', context)

def projetos_view(request):
    # Busca todos os projetos ordenados por ano e depois por UC
    projetos_ordenados = Projeto.objects.all()
    
    # Agrupa por UC para manter a estrutura do template (se preferires)
    # Se preferires uma lista simples, apenas passas 'projetos_ordenados'
    projetos_por_uc = {}
    for projeto in projetos_ordenados:
        uc_nome = projeto.unidade_curricular.nome
        if uc_nome not in projetos_por_uc:
            projetos_por_uc[uc_nome] = []
        projetos_por_uc[uc_nome].append(projeto)

    context = {
        'projetos_por_uc': projetos_por_uc,
        # 'projetos_ordenados': projetos_ordenados # Alternativa: usar lista simples
    }
    return render(request, 'portfolio/projetos.html', context)

def tecnologias_view(request):
    # Vai buscar todas as tecnologias, ordenadas por nome (alfabeticamente)
    tecnologias = Tecnologia.objects.all().order_by('nome')
    context = {'tecnologias': tecnologias}
    return render(request, 'portfolio/tecnologias.html', context)

def tfcs_view(request):
    # Vai buscar todos os TFCs, ordenados do mais recente para o mais antigo
    tfcs = TFC.objects.all().order_by('-ano', 'titulo')
    context = {'tfcs': tfcs}
    return render(request, 'portfolio/tfcs.html', context)

def docentes_view(request):
    # Vai buscar todos os docentes, ordenados alfabeticamente
    docentes = Docente.objects.all().order_by('nome')
    context = {'docentes': docentes}
    return render(request, 'portfolio/docentes.html', context)

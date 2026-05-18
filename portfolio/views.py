# Views do Django para renderizar as páginas do portfolio.
# Aqui carregamos os dados dos modelos e enviamos para os templates.
import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Licenciatura, UnidadeCurricular, Projeto, Tecnologia, TFC, Docente, Aluno, Competencia, Formacao, MakingOf
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm
from django.contrib.auth.decorators import login_required


def home(request):
    # Página inicial passa a ser a hero page com o menu integrado
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

def curso_ucs_view(request, curso_id):
    curso = get_object_or_404(Licenciatura, pk=curso_id)
    ucs_por_ano = {}
    for uc in curso.ucs.all().order_by('ano', 'semestre', 'nome'):
        ano = uc.ano
        if ano not in ucs_por_ano:
            ucs_por_ano[ano] = []
        ucs_por_ano[ano].append(uc)
    
    context = {
        'curso': curso,
        'ucs_por_ano': ucs_por_ano,
    }
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

def alunos_view(request):
    # Vai buscar todos os alunos, ordenados alfabeticamente
    alunos = Aluno.objects.all().order_by('nome')
    context = {'alunos': alunos}
    return render(request, 'portfolio/alunos.html', context)

def competencias_view(request):
    # Agrupar as competências pelo tipo facilita a visualização
    competencias_ordenadas = Competencia.objects.all().prefetch_related('tecnologias').order_by('tipo', '-nivel', 'nome')
    
    competencias_por_tipo = {}
    for comp in competencias_ordenadas:
        tipo = comp.tipo
        if tipo not in competencias_por_tipo:
            competencias_por_tipo[tipo] = []
        competencias_por_tipo[tipo].append(comp)

    context = {'competencias_por_tipo': competencias_por_tipo}
    return render(request, 'portfolio/competencias.html', context)

def formacoes_view(request):
    # Vai buscar todas as formacoes, ordenadas da mais recente para a mais antiga
    formacoes = Formacao.objects.all().prefetch_related('competencias').order_by('-data_inicio')
    context = {'formacoes': formacoes}
    return render(request, 'portfolio/formacoes.html', context)

def makingof_view(request):
    # Vai buscar todos os registos do Making Of, do mais recente para o mais antigo
    registos = MakingOf.objects.all().order_by('-data')
    context = {'registos': registos}
    return render(request, 'portfolio/makingof.html', context)

@login_required
def novo_projeto_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projetos')

    else:
        form = ProjetoForm()

    return render(request, 'portfolio/projeto_form.html', {
        'form': form,
        'titulo': 'Novo Projeto'
    })

@login_required
def edita_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)

        if form.is_valid():
            form.save()
            return redirect('projetos')

    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'portfolio/projeto_form.html', {
        'form': form,
        'titulo': 'Editar Projeto'
    })

@login_required
def apaga_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')

    return render(request, 'portfolio/projeto_confirm_delete.html', {
        'projeto': projeto
    })

def nova_tecnologia_view(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('tecnologias')

    else:
        form = TecnologiaForm()

    return render(request, 'portfolio/tecnologia_form.html', {
        'form': form,
        'titulo': 'Nova Tecnologia'
    })

def edita_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)

    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)

        if form.is_valid():
            form.save()
            return redirect('tecnologias')

    else:
        form = TecnologiaForm(instance=tecnologia)

    return render(request, 'portfolio/tecnologia_form.html', {
        'form': form,
        'titulo': 'Editar Tecnologia'
    })


def apaga_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)

    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')

    return render(request, 'portfolio/tecnologia_confirm_delete.html', {
        'tecnologia': tecnologia
    })

def nova_competencia_view(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm()
    return render(request, 'portfolio/competencia_form.html', {
        'form': form,
        'titulo': 'Nova Competência'
    })

def edita_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, request.FILES, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'portfolio/competencia_form.html', {
        'form': form,
        'titulo': 'Editar Competência'
    })

def apaga_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'portfolio/competencia_confirm_delete.html', {
        'competencia': competencia
    })

def nova_formacao_view(request):
    if request.method == 'POST':
        form = FormacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm()
    return render(request, 'portfolio/formacao_form.html', {
        'form': form,
        'titulo': 'Nova Formação'
    })

def edita_formacao_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    if request.method == 'POST':
        form = FormacaoForm(request.POST, request.FILES, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm(instance=formacao)
    return render(request, 'portfolio/formacao_form.html', {
        'form': form,
        'titulo': 'Editar Formação'
    })

def apaga_formacao_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_confirm_delete.html', {
        'formacao': formacao
    })

def sobre_view(request):
    # Carregar o conteúdo do models.py para mostrar no ecrã dinamicamente
    models_file_path = os.path.join(settings.BASE_DIR, 'portfolio', 'models.py')
    try:
        with open(models_file_path, 'r', encoding='utf-8') as f:
            models_content = f.read()
    except Exception:
        models_content = "Não foi possível carregar o ficheiro models.py"

    # NOVO: Carregar o ficheiro markdown bruto para o template tratar com markdownify
    making_of_md_path = os.path.join(settings.BASE_DIR, 'making_of.md')
    try:
        with open(making_of_md_path, 'r', encoding='utf-8') as f:
            making_of_content = f.read()
    except Exception as e:
        making_of_content = f"O ficheiro 'making_of.md' não foi encontrado. ({e})"

    # Tentar encontrar o Projeto do Portfolio para carregar as tecnologias
    from .models import Projeto, Tecnologia
    
    portfolio_projeto = Projeto.objects.filter(titulo__icontains="Portfolio").first()
    techs_por_tipo = {}

    if portfolio_projeto:
        # Obter todas as tecnologias associadas ao projeto, trazendo também o objeto do tipo associado
        techs = portfolio_projeto.tecnologias.all().select_related('tipo_categoria')
        
        for t in techs:
            # Se não tiver tipo, coloca na categoria "Outros"
            tipo_nome = t.tipo_categoria.nome if t.tipo_categoria else "Não Categorizado"
            if tipo_nome not in techs_por_tipo:
                techs_por_tipo[tipo_nome] = []
            techs_por_tipo[tipo_nome].append(t)

    return render(request, 'portfolio/sobre.html', {
        'models_code': models_content,
        'techs_por_tipo': techs_por_tipo,
        'projeto': portfolio_projeto,
        'making_of_content': making_of_content
    })

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cursos/', views.cursos_view, name='cursos'),
    path('curso/<int:curso_id>/', views.curso_detail, name='curso_detail'),
    path('curso/<int:curso_id>/ucs/', views.curso_ucs_view, name='curso_ucs'),
    path('uc/<int:uc_id>/', views.uc_detail, name='uc_detail'),
    # Quando alguém for a /ucs/, corre a views.ucs_view
    path('ucs/', views.ucs_view, name='ucs'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('docentes/', views.docentes_view, name='docentes'),
    path('alunos/', views.alunos_view, name='alunos'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('makingof/', views.makingof_view, name='makingof'),
    #urls de projetos (criar, editar,apagar)
    path('projeto/novo/', views.novo_projeto_view, name='novo_projeto'),
    path('projeto/<int:projeto_id>/editar/', views.edita_projeto_view, name='edita_projeto'),
    path('projeto/<int:projeto_id>/apagar/', views.apaga_projeto_view, name='apaga_projeto'),
    #urls de tecnologias (criar, editar,apagar)
    path('tecnologia/novo/', views.nova_tecnologia_view, name='nova_tecnologia'),
    path('tecnologia/<int:tecnologia_id>/editar/', views.edita_tecnologia_view, name='edita_tecnologia'),
    path('tecnologia/<int:tecnologia_id>/apagar/', views.apaga_tecnologia_view, name='apaga_tecnologia'),
    #urls de competencias (criar, editar, apagar)
    path('competencia/nova/', views.nova_competencia_view, name='nova_competencia'),
    path('competencia/<int:competencia_id>/editar/', views.edita_competencia_view, name='edita_competencia'),
    path('competencia/<int:competencia_id>/apagar/', views.apaga_competencia_view, name='apaga_competencia'),
    #urls de formacoes (criar, editar, apagar)
    path('formacao/nova/', views.nova_formacao_view, name='nova_formacao'),
    path('formacao/<int:formacao_id>/editar/', views.edita_formacao_view, name='edita_formacao'),
    path('formacao/<int:formacao_id>/apagar/', views.apaga_formacao_view, name='apaga_formacao'),
]

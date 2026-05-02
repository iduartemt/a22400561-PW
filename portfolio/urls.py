from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cursos/', views.cursos_view, name='cursos'),
    path('curso/<int:curso_id>/', views.curso_detail, name='curso_detail'),
    path('uc/<int:uc_id>/', views.uc_detail, name='uc_detail'),
    # Quando alguém for a /ucs/, corre a views.ucs_view
    path('ucs/', views.ucs_view, name='ucs'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
]

from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.lista_artigos, name='lista_artigos'),
    path('novo/', views.novo_artigo, name='novo_artigo'),
    path('<int:artigo_id>/', views.detalhe_artigo, name='detalhe_artigo'),
    path('<int:artigo_id>/editar/', views.edita_artigo, name='edita_artigo'),
    path('<int:artigo_id>/apagar/', views.apaga_artigo, name='apaga_artigo'),
    path('<int:artigo_id>/gostar/', views.gostar_artigo, name='gostar_artigo'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('curso/', views.curso_detail, name='curso_detail'),
    path('uc/<int:uc_id>/', views.uc_detail, name='uc_detail'),
    # Quando alguém for a /ucs/, corre a views.ucs_view
    path('ucs/', views.ucs_view, name='ucs'),
]

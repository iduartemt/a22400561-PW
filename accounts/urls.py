from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('registo/', views.registo_view, name='registo'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # ROTAS DO LINK MÁGICO:
    path('pedir-link/', views.pedir_link_view, name='pedir_link'),
    path('login-link/<str:token>/', views.login_link_view, name='login_link'),
]

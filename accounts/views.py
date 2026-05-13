from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistoForm
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

# View de Registo
def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Faz login automático após o registo
            return redirect('home')
    else:
        form = RegistoForm()
    return render(request, 'accounts/registo.html', {'form': form})

# View de Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# View de Logout
def logout_view(request):
    logout(request)
    return redirect('home')

# 1. Página onde o utilizador pede o link
def pedir_link_view(request):
    link_gerado = None
    if request.method == "POST":
        username = request.POST.get('username')
        try:
            # Tenta ver se o utilizador existe
            user = User.objects.get(username=username)
            
            # GERA O TOKEN MÁGICO
            signer = TimestampSigner()
            token = signer.sign(username) # Criptografa o username com a data atual
            
            # Constrói o URL completo (ex: http://127.0.0.1:8000/accounts/login-link/TOKEN)
            link_relativo = reverse('accounts:login_link', kwargs={'token': token})
            if settings.SITE_BASE_URL:
                link_gerado = f"{settings.SITE_BASE_URL.rstrip('/')}{link_relativo}"
            else:
                link_gerado = request.build_absolute_uri(link_relativo)
            # Imprime no terminal para poderes clicar!
            print("\n" + "="*30)
            print(f"LINK MÁGICO PARA O USER '{username}':\n{link_gerado}")
            print("="*30 + "\n")

        except User.DoesNotExist:
            # Se não existe, não fazemos nada (por segurança não avisamos que não existe)
            pass
            
        # Mostramos uma página a dizer "Verifica o terminal"
        return render(request, 'accounts/link_enviado.html', {'link': link_gerado})

    return render(request, 'accounts/pedir_link.html')

# 2. Página que processa o clique no link
def login_link_view(request, token):
    signer = TimestampSigner()
    try:
        # Tenta descodificar o token. 'max_age=300' faz com que o link expire em 5 minutos (300s)!
        username = signer.unsign(token, max_age=300)
        user = User.objects.get(username=username)
        
        # Faz Login automático!
        login(request, user)
        return redirect('home')
        
    except (BadSignature, SignatureExpired, User.DoesNotExist):
        # Se o link for falso, alterado, ou já tiver expirado: erro!
        return render(request, 'accounts/link_erro.html')

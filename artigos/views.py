from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm

def lista_artigos(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    return render(request, 'artigos/lista_artigos.html', {'artigos': artigos})

def detalhe_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = artigo.comentarios.all().order_by('-data_criacao')
    
    if request.method == 'POST' and request.user.is_authenticated:
        # Só utilizadores autenticados podem submeter comentários
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
            return redirect('artigos:detalhe_artigo', artigo_id=artigo.id)
    else:
        form = ComentarioForm()
        
    context = {
        'artigo': artigo,
        'comentarios': comentarios,
        'form': form,
    }
    return render(request, 'artigos/detalhe_artigo.html', context)

@login_required
def novo_artigo(request):
    # Apenas utilizadores do grupo 'bloggers' podem criar
    if not request.user.groups.filter(name='bloggers').exists() and not request.user.is_superuser:
        raise PermissionDenied("Não tens permissões para criar artigos.")
        
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect('artigos:detalhe_artigo', artigo_id=artigo.id)
    else:
        form = ArtigoForm()
        
    return render(request, 'artigos/form_artigo.html', {'form': form, 'acao': 'Criar'})

@login_required
def edita_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    
    # Apenas autores podem editar e apenas os SEUS próprios artigos
    if request.user != artigo.autor and not request.user.is_superuser:
        raise PermissionDenied("Apenas podes editar os teus próprios artigos.")
        
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:detalhe_artigo', artigo_id=artigo.id)
    else:
        form = ArtigoForm(instance=artigo)
        
    return render(request, 'artigos/form_artigo.html', {'form': form, 'acao': 'Editar'})

@login_required
def apaga_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    
    if request.user != artigo.autor and not request.user.is_superuser:
        raise PermissionDenied("Apenas podes apagar os teus próprios artigos.")
        
    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos:lista_artigos')
        
    return render(request, 'artigos/apaga_artigo.html', {'artigo': artigo})

@login_required
def gostar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)
    return redirect('artigos:detalhe_artigo', artigo_id=artigo.id)

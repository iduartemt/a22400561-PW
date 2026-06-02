from ninja import NinjaAPI
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Ingrediente, Receita, Utilizador
from .schemas import (
    IngredienteInputSchema,
    IngredienteOutputSchema,
    ReceitaInputSchema,
    ReceitaOutputSchema,
    UtilizadorInputSchema,
    UtilizadorOutputSchema,
)

api = NinjaAPI(
    title="API de Receitas",
    description="API para gestão de receitas culinárias, utilizadores e ingredientes."
)

#---------------------------INGREDIENTE----------------------

@api.get("/ingredientes", response=list[IngredienteOutputSchema], tags=["Ingredientes"])
def lista_ingredientes(
    request,
    nome: str = None,
    limit: int = 10,
    offset: int = 0
):
    ingredientes = Ingrediente.objects.all()

    if nome:
        ingredientes = ingredientes.filter(nome__icontains=nome)

    return ingredientes[offset:offset + limit]

@api.get("/ingredientes/{ingrediente_id}", response=IngredienteOutputSchema, tags=["Ingredientes"])
def ver_ingrediente(request, ingrediente_id: int):
    return get_object_or_404(Ingrediente, id= ingrediente_id)

@api.post("/ingredientes", response=IngredienteOutputSchema, tags=["Ingredientes"])
def cria_ingrediente(request, ingrediente: IngredienteInputSchema):
    return Ingrediente.objects.create(**ingrediente.dict())

@api.put("/ingredientes/{ingrediente_id}", response=IngredienteOutputSchema, tags=["Ingredientes"])
def atualiza_ingrediente(request, ingrediente_id: int, ingrediente: IngredienteInputSchema):
    ingrediente_guardado = get_object_or_404(Ingrediente, id=ingrediente_id)
    ingrediente_guardado.nome = ingrediente.nome
    ingrediente_guardado.save()
    return ingrediente_guardado

@api.delete("/ingredientes/{ingrediente_id}", tags=["Ingredientes"])
def apaga_ingrediente(request, ingrediente_id: int):
    ingrediente = get_object_or_404(Ingrediente, id=ingrediente_id)
    ingrediente.delete()
    return {"mensagem": "Ingrediente apagado com sucesso"}


#------------------------UTILIZADOR----------------------

@api.get("/utilizadores", response=list[UtilizadorOutputSchema], tags=["Utilizadores"])
def lista_utilizadores(
    request,
    nome: str = None,
    limit: int = 10,
    offset: int = 0
):
    utilizadores = Utilizador.objects.all()

    if nome:
        utilizadores = utilizadores.filter(nome__icontains=nome)

    return utilizadores[offset:offset + limit]

@api.get("/utilizadores/{utilizador_id}", response=UtilizadorOutputSchema, tags=["Utilizadores"])
def ver_utilizador(request, utilizador_id: int):
    return get_object_or_404(Utilizador, id=utilizador_id)

@api.post("/utilizadores", response=UtilizadorOutputSchema, tags=["Utilizadores"])
def cria_utilizador(request, utilizador: UtilizadorInputSchema):
    return Utilizador.objects.create(**utilizador.dict())

@api.put("/utilizadores/{utilizador_id}", response=UtilizadorOutputSchema, tags=["Utilizadores"])
def atualiza_utilizador(request, utilizador_id: int, utilizador: UtilizadorInputSchema):
    utilizador_guardado = get_object_or_404(Utilizador, id=utilizador_id)
    utilizador_guardado.nome = utilizador.nome
    utilizador_guardado.email = utilizador.email
    utilizador_guardado.save()
    return utilizador_guardado

@api.delete("/utilizadores/{utilizador_id}", tags=["Utilizadores"])
def apaga_utilizador(request, utilizador_id: int):
    utilizador = get_object_or_404(Utilizador, id=utilizador_id)
    utilizador.delete()
    return {"mensagem": "Utilizador apagado com sucesso"}


#---------------------------RECEITA----------------------

@api.get("/receitas", response=list[ReceitaOutputSchema], tags=["Receitas"])
def lista_receitas(
    request,
    titulo: str = None,
    limit: int = 10,
    offset: int = 0
):
    receitas = Receita.objects.all()

    if titulo:
        receitas = receitas.filter(titulo__icontains=titulo)

    return receitas[offset:offset + limit]

@api.get("/receitas/{receita_id}", response=ReceitaOutputSchema, tags=["Receitas"])
def ver_receita(request, receita_id: int):
    return get_object_or_404(Receita, id=receita_id)

@api.post("/receitas", response=ReceitaOutputSchema, tags=["Receitas"])
def cria_receita(request, receita: ReceitaInputSchema):
    utilizador = get_object_or_404(Utilizador, id=receita.utilizador_id)
    ingredientes = list(Ingrediente.objects.filter(id__in=receita.ingredientes_ids))
    if len(ingredientes) != len(set(receita.ingredientes_ids)):
        raise Http404("Um ou mais ingredientes nao existem")

    receita_guardada = Receita.objects.create(
        titulo=receita.titulo,
        descricao=receita.descricao,
        tempo_preparacao=receita.tempo_preparacao,
        utilizador=utilizador,
    )
    receita_guardada.ingredientes.set(ingredientes)
    return receita_guardada

@api.put("/receitas/{receita_id}", response=ReceitaOutputSchema, tags=["Receitas"])
def atualiza_receita(request, receita_id: int, receita: ReceitaInputSchema):
    receita_guardada = get_object_or_404(Receita, id=receita_id)
    utilizador = get_object_or_404(Utilizador, id=receita.utilizador_id)
    ingredientes = list(Ingrediente.objects.filter(id__in=receita.ingredientes_ids))
    if len(ingredientes) != len(set(receita.ingredientes_ids)):
        raise Http404("Um ou mais ingredientes nao existem")

    receita_guardada.titulo = receita.titulo
    receita_guardada.descricao = receita.descricao
    receita_guardada.tempo_preparacao = receita.tempo_preparacao
    receita_guardada.utilizador = utilizador
    receita_guardada.save()
    receita_guardada.ingredientes.set(ingredientes)
    return receita_guardada

@api.delete("/receitas/{receita_id}", tags=["Receitas"])
def apaga_receita(request, receita_id: int):
    receita = get_object_or_404(Receita, id=receita_id)
    receita.delete()
    return {"mensagem": "Receita apagada com sucesso"}

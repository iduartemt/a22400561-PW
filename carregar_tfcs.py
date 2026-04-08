import os
import django
import json
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import (
    Licenciatura,
    UnidadeCurricular,
    Docente,
    Aluno,
    Competencia,
    Tecnologia,
    Projeto,
    Formacao,
    TFC,
)


def limpar_texto(valor):
    if valor is None:
        return ''
    return str(valor).strip()


def limpar_lista(valor):
    if not valor:
        return []

    itens = []

    if isinstance(valor, list):
        for v in valor:
            texto = limpar_texto(v)
            if texto:
                itens.append(texto)
    else:
        texto = limpar_texto(valor)
        if texto:
            itens.append(texto)

    resultado = []
    for item in itens:
        partes = re.split(r';+', item)
        for parte in partes:
            parte = limpar_texto(parte)
            if parte:
                resultado.append(parte)

    return resultado


def imprimir_info(texto):
    print(f"\033[36m{texto}\033[0m")


def imprimir_sucesso(texto):
    print(f"\033[32m{texto}\033[0m")


def imprimir_aviso(texto):
    print(f"\033[33m{texto}\033[0m")


def imprimir_erro(texto):
    print(f"\033[31m{texto}\033[0m")


def carregar_dados():
    caminho_ficheiro = 'portfolio/tfcs_2025.json'

    imprimir_aviso('A apagar dados antigos...')
    Licenciatura.objects.all().delete()
    UnidadeCurricular.objects.all().delete()
    Docente.objects.all().delete()
    Aluno.objects.all().delete()
    Competencia.objects.all().delete()
    Tecnologia.objects.all().delete()
    Projeto.objects.all().delete()
    Formacao.objects.all().delete()
    TFC.objects.all().delete()
    imprimir_sucesso('Dados antigos apagados.')

    with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
        dados_tfcs = json.load(f)

    imprimir_info(f"Encontrados {len(dados_tfcs)} registos. A iniciar o carregamento...")

    total_tfcs = 0
    total_docentes_criados = 0
    total_tecnologias_criadas = 0

    for indice, item in enumerate(dados_tfcs, start=1):
        titulo = limpar_texto(item.get('titulo'))
        curso = limpar_texto(item.get('curso'))
        ano = item.get('ano') or 2025
        resumo = limpar_texto(item.get('resumo'))
        palavras_chave = item.get('palavras_chave')

        # Ignorar entradas inválidas / cabeçalhos
        if not titulo or titulo.lower() == '559 trabalhos finais de curso':
            imprimir_aviso(f'[{indice}/{len(dados_tfcs)}] Registo ignorado: título inválido')
            continue

        imprimir_info(f"[{indice}/{len(dados_tfcs)}] TFC: {titulo}")

        orientadores_objs = []
        nomes_orientadores = limpar_lista(item.get('orientador'))

        for nome_orientador in nomes_orientadores:
            docente_obj, created = Docente.objects.get_or_create(nome=nome_orientador)

            if created:
                total_docentes_criados += 1
                imprimir_sucesso(f"  Docente criado: {nome_orientador}")
            else:
                imprimir_aviso(f"  Docente já existia: {nome_orientador}")

            orientadores_objs.append(docente_obj)

        # Criar TFC apenas com campos que existem no modelo
        tfc = TFC.objects.create(
            titulo=titulo,
            curso=curso,
            ano=ano,
            resumo=resumo,
            palavras_chave=palavras_chave,
        )

        total_tfcs += 1
        imprimir_sucesso(f"  TFC criado: {titulo}")

        # Associar orientador
        if orientadores_objs:
            if hasattr(tfc, 'orientador_id'):
                tfc.orientador = orientadores_objs[0]
                tfc.save()
                imprimir_sucesso(f"  Orientador associado: {orientadores_objs[0].nome}")
            elif hasattr(tfc, 'orientadores'):
                tfc.orientadores.set(orientadores_objs)
                nomes = ', '.join(docente.nome for docente in orientadores_objs)
                imprimir_sucesso(f"  Orientadores associados: {nomes}")

        tecnologias_json = item.get('tecnologias')

        for tech_nome in limpar_lista(tecnologias_json):
            tech_obj, created = Tecnologia.objects.get_or_create(
                nome=tech_nome,
                defaults={
                    'tipo': 'Não definido',
                    'descricao': 'Gerado automaticamente através do script de TFCs',
                    'website_oficial': 'https://#'
                }
            )

            if created:
                total_tecnologias_criadas += 1
                imprimir_sucesso(f"  Tecnologia criada: {tech_nome}")
            else:
                imprimir_aviso(f"  Tecnologia já existia: {tech_nome}")

            if hasattr(tfc, 'tecnologias'):
                tfc.tecnologias.add(tech_obj)
                imprimir_sucesso(f"  Tecnologia associada ao TFC: {tech_nome}")

    print()
    imprimir_sucesso('Carregamento concluído com sucesso!')
    print(f'TFCs criados: {total_tfcs}')
    print(f'Docentes criados: {total_docentes_criados}')
    print(f'Tecnologias criadas: {total_tecnologias_criadas}')


if __name__ == '__main__':
    carregar_dados()
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()

from django.db import models
import json

from .models import *

Licenciatura.objects.all().delete()
UnidadeCurricular.objects.all().delete()
Docente.objects.all().delete()
Aluno.objects.all().delete()
Competencia.objects.all().delete()
Tecnologia.objects.all().delete()
Projeto.objects.all().delete()
Formacao.objects.all().delete()
TFC.objects.all().delete()

with open('portfolio/tfcs_2025.json') as f:
    tfcs = json.load(f)
    # tfcs é uma lista de dicionarios,
    # cada dicionario tendo informacao de um tfc

    for tfc in tfcs:
        if not tfc.get('curso') or not tfc['curso'].strip():
            continue
        orientador, created = Docente.objects.get_or_create(nome=tfc['orientador'])
        tfc_obj = TFC.objects.create(
            titulo=tfc['titulo'],
            orientador=orientador,
            curso=tfc['curso'],
            ano=tfc['ano'],
            resumo=tfc['resumo'],
            palavras_chave=[kw.strip() for kw in tfc['palavras_chave'].split(';') if kw.strip()],
            area='',
            destaque=False,
        )
        
        tech_names = [t.strip() for t in tfc['tecnologias'].split(';') if t.strip()]
        for tech_name in tech_names:
            tech, created = Tecnologia.objects.get_or_create(nome=tech_name)
            tfc_obj.tecnologias.add(tech)



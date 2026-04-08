import os
import sys
import json
import glob

# Adicionar o diretório do projeto ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular

def importar_curso():
    # Limpar dados existentes
    Licenciatura.objects.all().delete()
    UnidadeCurricular.objects.all().delete()

    # Caminho para os arquivos
    files_dir = os.path.join(os.path.dirname(__file__), 'files')

    # Importar curso geral
    curso_file = os.path.join(files_dir, 'ULHT260-PT.json')
    with open(curso_file, 'r', encoding='utf-8') as f:
        curso_data = json.load(f)

    # Criar Licenciatura
    licenciatura, created = Licenciatura.objects.get_or_create(
        nome="Engenharia Informática",  # Assumindo baseado nos dados
        defaults={
            'sigla': 'EI',
            'descricao': 'Curso de Engenharia Informática',
            'duracao_anos': 3,
            'diploma_degree': 'Licenciado',
            'course_code': 260,
            'reasons': curso_data.get('reasons', [])
        }
    )

    # Importar UCs do plano curricular
    for uc_data in curso_data.get('courseFlatPlan', []):
        UnidadeCurricular.objects.get_or_create(
            curricular_unit_code=uc_data['curricularUnitCode'],
            defaults={
                'nome': uc_data['curricularUnitName'],
                'ano': uc_data['curricularYear'],
                'semestre': 1 if '1' in str(uc_data.get('semester', '')) else 2,
                'ects': uc_data['ects'],
                'licenciatura': licenciatura,
                'type': uc_data.get('semester', ''),
                'group_code': uc_data.get('curricularUnitGroupCode'),
            }
        )

    # Importar detalhes das UCs
    uc_files = glob.glob(os.path.join(files_dir, 'ULHT260-*-PT.json'))
    for uc_file in uc_files:
        if os.path.basename(uc_file) == 'ULHT260-PT.json':
            continue  # Já processado

        with open(uc_file, 'r', encoding='utf-8') as f:
            uc_detail = json.load(f)

        curricular_unit_code = uc_detail.get('curricularUnitCode')
        if curricular_unit_code:
            try:
                uc = UnidadeCurricular.objects.get(curricular_unit_code=curricular_unit_code)
                uc.language = uc_detail.get('language', '')
                uc.nature = uc_detail.get('nature', '')
                uc.type = uc_detail.get('type', '')
                uc.internship = uc_detail.get('internship', '')
                uc.objectives = uc_detail.get('objectives', '')
                uc.programme = uc_detail.get('programme', '')
                uc.presentation = uc_detail.get('presentation', '')
                uc.bibliography = uc_detail.get('bibliography', '')
                uc.assessment = uc_detail.get('avaliacao', '')
                uc.methodology = uc_detail.get('methodology', '')
                uc.organic_unit = uc_detail.get('organicUnit', '')
                uc.group_code = uc_detail.get('groupCode')
                uc.institution_code = uc_detail.get('institutionCode')
                uc.save()
            except UnidadeCurricular.DoesNotExist:
                print(f"UC com código {curricular_unit_code} não encontrada no plano curricular")

    print("Importação concluída!")

if __name__ == '__main__':
    importar_curso()
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import TipoTecnologia, Tecnologia, Projeto, Licenciatura, UnidadeCurricular

def run():
    # 1. Criar Tipos
    tipos_nomes = ['Frontend', 'Backend', 'Base de Dados', 'Storage', 'Outros (Ferramentas)']
    tipos_map = {}
    for t_nome in tipos_nomes:
        obj, _ = TipoTecnologia.objects.get_or_create(nome=t_nome)
        tipos_map[t_nome] = obj
        print(f"Tipo '{t_nome}' garantido.")

    # 2. Criar ou Localizar o Projeto Portfolio de Programação Web
    projeto, created = Projeto.objects.get_or_create(
        titulo="Portfolio de Programação Web",
        defaults={
            'descricao': "Desenvolvimento da aplicação de portfolio académico.",
            'conceitos_aplicados': "Django, MVT, ORM, Migrações, CRUD.",
            'ano': 2026,
            'github_url': "https://github.com/",
            'unidade_curricular': UnidadeCurricular.objects.first() # just placeholder if exists
        }
    )
    
    if not projeto.unidade_curricular:
         # Try to find any UC to assign
         first_uc = UnidadeCurricular.objects.first()
         if first_uc:
             projeto.unidade_curricular = first_uc
             projeto.save()

    print(f"Projeto '{projeto.titulo}' garantido.")

    # 3. Criar e Associar Tecnologias Base
    techs = [
        ('Django', 'Backend', 'Framework web robusta para Python. Permite prototipagem rápida. Aspetos positivos: facilidade de uso e painel admin.'),
        ('HTML', 'Frontend', 'Estrutura fundamental para a web. Essencial. Simples de aprender.'),
        ('CSS', 'Frontend', 'Estilização da interface gráfica. Permite flexibilidade de design.'),
        ('Git', 'Outros (Ferramentas)', 'Controle de versões para código fonte. Permite rastreabilidade. Muito seguro.'),
        ('GitHub', 'Outros (Ferramentas)', 'Plataforma de hospedagem de código. Facilita o backup e colaboração.')
    ]

    for nome, tipo, desc in techs:
        t_obj, c = Tecnologia.objects.get_or_create(
            nome=nome,
            defaults={
                'tipo': tipo,
                'descricao': desc,
                'website_oficial': 'https://www.google.com',
                'tipo_categoria': tipos_map[tipo]
            }
        )
        if c:
            print(f"Tecnologia '{nome}' criada.")
        else:
            # Update type just to be sure
            t_obj.tipo_categoria = tipos_map[tipo]
            t_obj.save()

        # Add to project
        projeto.tecnologias.add(t_obj)
        print(f"'{nome}' associada ao projeto.")

if __name__ == '__main__':
    run()

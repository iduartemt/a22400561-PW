from django.db import transaction
from .models import Tecnologia, Competencia


TECNOLOGIAS = [
    {
        "nome": "Python",
        "tipo": "Linguagem",
        "descricao": "Linguagem versátil para backend, dados e automação.",
        "website_oficial": "https://www.python.org/",
        "competencias": [
            "Programação",
            "Backend",
            "Machine Learning",
        ],
    },
    {
        "nome": "Django",
        "tipo": "Framework",
        "descricao": "Framework web em Python.",
        "website_oficial": "https://www.djangoproject.com/",
        "competencias": [
            "Backend",
            "APIs REST",
            "Web",
        ],
    },
    {
        "nome": "React",
        "tipo": "Frontend",
        "descricao": "Biblioteca para interfaces modernas.",
        "website_oficial": "https://react.dev/",
        "competencias": [
            "Frontend",
            "Web",
            "UI/UX",
        ],
    },
    {
        "nome": "PostgreSQL",
        "tipo": "Base de Dados",
        "descricao": "Base de dados relacional robusta.",
        "website_oficial": "https://www.postgresql.org/",
        "competencias": [
            "Bases de Dados",
            "SQL",
        ],
    },
    {
        "nome": "Docker",
        "tipo": "DevOps",
        "descricao": "Containerização de aplicações.",
        "website_oficial": "https://www.docker.com/",
        "competencias": [
            "DevOps",
            "Deploy",
        ],
    },
]


COMPETENCIAS = [
    {"nome": "Programação", "tipo": "Hard Skill", "nivel": 5},
    {"nome": "Backend", "tipo": "Hard Skill", "nivel": 4},
    {"nome": "Frontend", "tipo": "Hard Skill", "nivel": 4},
    {"nome": "Web", "tipo": "Hard Skill", "nivel": 5},
    {"nome": "APIs REST", "tipo": "Hard Skill", "nivel": 4},
    {"nome": "Bases de Dados", "tipo": "Hard Skill", "nivel": 4},
    {"nome": "SQL", "tipo": "Hard Skill", "nivel": 4},
    {"nome": "DevOps", "tipo": "Hard Skill", "nivel": 3},
    {"nome": "Deploy", "tipo": "Hard Skill", "nivel": 3},
    {"nome": "Machine Learning", "tipo": "Hard Skill", "nivel": 3},
    {"nome": "UI/UX", "tipo": "Soft Skill", "nivel": 3},
]


@transaction.atomic
def seed():
    print("A criar competências...")

    competencias_por_nome = {}
    for item in COMPETENCIAS:
        comp, created = Competencia.objects.get_or_create(
            nome=item["nome"],
            defaults={
                "tipo": item["tipo"],
                "nivel": item["nivel"],
            },
        )

        if not created:
            comp.tipo = item["tipo"]
            comp.nivel = item["nivel"]
            comp.save()

        competencias_por_nome[item["nome"]] = comp

    print("A criar tecnologias e relações...")

    for item in TECNOLOGIAS:
        tech, created = Tecnologia.objects.get_or_create(
            nome=item["nome"],
            defaults={
                "tipo": item["tipo"],
                "descricao": item["descricao"],
                "website_oficial": item["website_oficial"],
            },
        )

        if not created:
            tech.tipo = item["tipo"]
            tech.descricao = item["descricao"]
            tech.website_oficial = item["website_oficial"]
            tech.save()

        # RELAÇÃO MANY TO MANY
        competencias_relacionadas = [
            competencias_por_nome[nome]
            for nome in item["competencias"]
            if nome in competencias_por_nome
        ]

        tech.competencias.set(competencias_relacionadas)

    print("✅ Seed concluída com sucesso!")
    print(f"Tecnologias: {Tecnologia.objects.count()}")
    print(f"Competências: {Competencia.objects.count()}")
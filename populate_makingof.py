import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import MakingOf

def populate():
    # Limpa registos antigos para não duplicar se correres isto várias vezes
    MakingOf.objects.all().delete()
    
    # Registo 1: Erros e Correções (Modelos Base)
    MakingOf.objects.create(
        titulo="Erros e Correções na Modelação Base",
        entidade="Tecnologia, Competência, MakingOf",
        erros_correcao="Erro 1 — Tecnologia: Inicialmente foi usado ImageField para o atributo logo, originando erro por falta da biblioteca Pillow. Correção: substituído por website_oficial.\n\nErro 2 — Competência: Campo ManyToMany com Tecnologia obrigatório. Correção: adicionado blank=True.\n\nErro 3 — MakingOf: Problemas de migração por campos obrigatórios. Correção: campos textuais definidos com blank=True.",
        data=date(2026, 4, 15),
        tipo_registo="Correção de Bugs",
        quantidade_iteracoes=3,
        commit_hash="c1a2b3d"
    )
    
    # Registo 2: Decisões de Modelação
    MakingOf.objects.create(
        titulo="Decisões de Modelação Iniciais",
        entidade="Licenciatura, UC, Projeto",
        justificacao_modelacao="Licenciatura: Incluído sigla para representação resumida. Relação 1:N com UC.\n\nUC: ects representa peso académico. Relação N:M com Docente.\n\nProjeto: github_url incluído por relevância. ManyToMany com Tecnologia.\n\nMakingOf: evidencia guarda o caminho para fotos.",
        data=date(2026, 4, 20),
        tipo_registo="Decisão Arquitetural",
        quantidade_iteracoes=2,
        commit_hash="f4e5d6c"
    )
    
    # Registo 3: Uso de Inteligência Artificial
    MakingOf.objects.create(
        titulo="Uso de Inteligência Artificial no Projeto",
        entidade="Global",
        uso_ia="Foi utilizado o ChatGPT como ferramenta de apoio na interpretação do enunciado, validação das relações entre entidades, boas práticas de Django e organização incremental do projeto.\n\nTodas as decisões foram revistas, implementadas e justificadas manualmente, garantindo compreensão total.",
        data=date(2026, 4, 25),
        tipo_registo="Ferramentas e Métodos",
        quantidade_iteracoes=1,
        commit_hash="g7h8i9j"
    )
    
    # Registo 4: Integração com API da Lusófona
    MakingOf.objects.create(
        titulo="Integração de Dados da API Lusófona",
        entidade="Licenciatura, UC",
        descricao_processo="Importação do curso geral, 31 UCs com conteúdo detalhado, 158 docentes (42 com dados completos). Criado script import_cursos_uc_doJson.py e modificado carregar_tfcs.py para preservar dados.",
        justificacao_modelacao="Licenciatura: Adicionados diploma_degree, course_code, reasons (JSONField).\n\nUC: Adicionados curricular_unit_code, language, objectives, etc. Mantidos como TextField para preservar formatação HTML da API.",
        sugestoes_implementadas="Utilização dos JSONs fornecidos pela universidade para enriquecer o portfólio. Mapeamento de campos complexos como reasons e HTML embutido.",
        data=date(2026, 4, 28),
        tipo_registo="Implementação de Feature",
        quantidade_iteracoes=5,
        commit_hash="k1l2m3n"
    )
    
    # Registo 5: Povoamento
    MakingOf.objects.create(
        titulo="Povoamento da Base de Dados (Teste)",
        entidade="Múltiplas",
        descricao_processo="Para garantir o teste de funcionalidades, foram inseridas 2 novas licenciaturas, 3 competências técnicas, 3 formações profissionais e 3 projetos. Validado o funcionamento das relações ManyToMany e ForeignKey.",
        data=date(2026, 4, 30),
        tipo_registo="Testes",
        quantidade_iteracoes=2,
        commit_hash="p4q5r6s"
    )

    # Registo 6: Refactoring para Interfaces de Consulta (Hoje)
    MakingOf.objects.create(
        titulo="Implementação das Interfaces de Consulta",
        entidade="Global",
        descricao_processo="Criação de rotas, views e templates HTML para listagem de todos os modelos do projeto. Transformação da home page num dashboard central de navegação.",
        sugestoes_implementadas="Enunciado: 'implementar interfaces de consulta (listagem) para os dados de cada modelo criado no sistema'. Cumprido a 100% com a criação de listagens dinâmicas separadas por modelo.",
        data=date(2026, 5, 2),
        tipo_registo="Implementação de Feature",
        quantidade_iteracoes=8,
        commit_hash="t7u8v9w"
    )
    
    print("Base de dados de Making Of preenchida com sucesso (6 registos inseridos)!")

if __name__ == '__main__':
    populate()

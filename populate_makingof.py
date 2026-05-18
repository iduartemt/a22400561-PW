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
        data=date(2026, 4, 6),
        tipo_registo="Correção de Bugs",
        quantidade_iteracoes=3,
        commit_hash="5c4f4d9"
    )
    
    # Registo 2: Decisões de Modelação
    MakingOf.objects.create(
        titulo="Decisões de Modelação Iniciais",
        entidade="Licenciatura, UC, Projeto",
        imagem="makingof/Relacoes.jpeg",
        justificacao_modelacao="Licenciatura: Incluído sigla para representação resumida. Relação 1:N com UC.\n\nUC: ects representa peso académico. Relação N:M com Docente.\n\nProjeto: github_url incluído por relevância. ManyToMany com Tecnologia.\n\nMakingOf: evidencia guarda o caminho para fotos.",
        data=date(2026, 4, 6),
        tipo_registo="Decisão Arquitetural",
        quantidade_iteracoes=4,
        commit_hash="e9841c2"
    )
    
    # Registo 3: Uso de Inteligência Artificial
    MakingOf.objects.create(
        titulo="Uso de Inteligência Artificial no Projeto",
        entidade="Global",
        uso_ia="Foi utilizado o ChatGPT como ferramenta de apoio na interpretação do enunciado, validação das relações entre entidades, boas práticas de Django e organização incremental do projeto.\n\nTodas as decisões foram revistas, implementadas e justificadas manualmente, garantindo compreensão total.",
        data=date(2026, 4, 6),
        tipo_registo="Ferramentas e Métodos",
        quantidade_iteracoes=1,
        commit_hash="d03bc97"
    )
    
    # Registo 4: Integração com API da Lusófona
    MakingOf.objects.create(
        titulo="Integração de Dados da API Lusófona",
        entidade="Licenciatura, UC",
        descricao_processo="Importação do curso geral, 31 UCs com conteúdo detalhado, 158 docentes (42 com dados completos). Criado script import_cursos_uc_doJson.py e modificado carregar_tfcs.py para preservar dados.",
        justificacao_modelacao="Licenciatura: Adicionados diploma_degree, course_code, reasons (JSONField).\n\nUC: Adicionados curricular_unit_code, language, objectives, etc. Mantidos como TextField para preservar formatação HTML da API.",
        sugestoes_implementadas="Utilização dos JSONs fornecidos pela universidade para enriquecer o portfólio. Mapeamento de campos complexos como reasons e HTML embutido.",
        data=date(2026, 4, 8),
        tipo_registo="Implementação de Feature",
        quantidade_iteracoes=5,
        commit_hash="37cfb0f"
    )
    
    # Registo 5: Povoamento
    MakingOf.objects.create(
        titulo="Povoamento da Base de Dados (Teste)",
        entidade="Múltiplas",
        descricao_processo="Para garantir o teste de funcionalidades, foram inseridas 2 novas licenciaturas, 3 competências técnicas, 3 formações profissionais e 3 projetos. Validado o funcionamento das relações ManyToMany e ForeignKey.",
        data=date(2026, 5, 2),
        tipo_registo="Testes",
        quantidade_iteracoes=2,
        commit_hash="e2cb9bf"
    )

    # Registo 6: Interfaces de Consulta
    MakingOf.objects.create(
        titulo="Implementação das Interfaces de Consulta",
        entidade="Global",
        descricao_processo="Criação de rotas, views e templates HTML para listagem de todos os modelos do projeto. Transformação da home page num dashboard central de navegação.",
        sugestoes_implementadas="Enunciado: 'implementar interfaces de consulta (listagem) para os dados de cada modelo criado no sistema'. Cumprido a 100% com a criação de listagens dinâmicas separadas por modelo.",
        data=date(2026, 5, 2),
        tipo_registo="Implementação de Feature",
        quantidade_iteracoes=8,
        commit_hash="cad2a60"
    )

    # NOVO Registo 7: Expansão MakingOf
    MakingOf.objects.create(
        titulo="Expansão do Modelo MakingOf",
        entidade="MakingOf",
        descricao_processo="Adição de novos campos de métricas no modelo MakingOf para rastreio aprofundado das iterações do projeto.",
        justificacao_modelacao="Campos como commit_hash e quantidade_iteracoes adicionados para suportar a rastreabilidade git solicitada.",
        data=date(2026, 5, 2),
        tipo_registo="Refactoring",
        quantidade_iteracoes=1,
        commit_hash="2e71603"
    )

    # NOVO Registo 8: Reestruturação de UCs
    MakingOf.objects.create(
        titulo="Reestruturação da Navegação de UCs",
        entidade="Licenciatura, UnidadeCurricular",
        descricao_processo="Migração da estrutura de listagem plana de Unidades Curriculares para uma exibição hierárquica aninhada dentro dos detalhes da própria Licenciatura.",
        justificacao_modelacao="Reforça a integridade e UX da navegação, refletindo que as UCs pertencem intrinsecamente a um plano curricular.",
        data=date(2026, 5, 6),
        tipo_registo="Refactoring",
        quantidade_iteracoes=3,
        commit_hash="ef75b6c"
    )
    
    # Registo 9: Operações CRUD (Hoje!)
    MakingOf.objects.create(
        titulo="Implementação de Operações CRUD Dinâmicas",
        entidade="Projeto, Tecnologia, Competência, Formação",
        descricao_processo="Desenvolvimento de rotas, views baseadas em POST/GET e templates reaproveitáveis para a criação, edição e remoção de entidades na aplicação.",
        erros_correcao="Resolvidos AttributeErrors por divergência de nomenclatura entre URLs e Views, além de clones de código defeituosos (copy-paste) entre modelos.",
        justificacao_modelacao="Uso massivo do ModelForm do Django e tags csrf_token, promovendo produtividade extrema e segurança ativa nativa.",
        data=date(2026, 5, 10),
        tipo_registo="Implementação de Feature",
        quantidade_iteracoes=15,
        commit_hash="c11ed5b"
    )
    
    # Registo 10: Página Sobre e Documentação
    MakingOf.objects.create(
        titulo="Criação da Página 'Sobre' e Documentação",
        entidade="Página Sobre",
        descricao_processo="Foi criada a página estática '/sobre' (com renderização de markdown e diagramas Mermaid) para explicar a arquitetura MVT, incluir o vídeo do tutorial e detalhar as tecnologias.",
        data=date(2026, 5, 12),
        tipo_registo="Implementação de Feature",
        quantidade_iteracoes=4,
        commit_hash="97c8c9a"
    )

    # Registo 11: Segurança e Login Mágico
    MakingOf.objects.create(
        titulo="Sistema de Autenticação e Login por Link Mágico",
        entidade="Accounts, Views",
        descricao_processo="Implementação completa do fluxo de autenticação e segurança, com proteção das rotas através de verificações de permissões e configuração de Login por Link Mágico.",
        justificacao_modelacao="A segurança e privacidade são vitais; a implementação garante que apenas utilizadores com as permissões corretas (ex: Gestor) podem criar ou editar dados.",
        data=date(2026, 5, 16),
        tipo_registo="Segurança e Acessos",
        quantidade_iteracoes=2,
        commit_hash="1525884"
    )

    # Registo 12: Melhorias de UI/UX e Media
    MakingOf.objects.create(
        titulo="Melhorias de UI/UX e Configuração de Media",
        entidade="Frontend, Settings",
        descricao_processo="Remodelação do design da página inicial com um fundo 'Mesh Gradient' minimalista, correção de conflitos de exibição das imagens nos templates e refinamento visual.",
        erros_correcao="Erro: Imagens não renderizavam. Correção: A rota de MEDIA estava mal mapeada no settings.py e em falta no urls.py. Adicionados ficheiros estáticos ao servidor Django.",
        data=date(2026, 5, 18),
        tipo_registo="UI/UX e Correção de Bugs",
        quantidade_iteracoes=1,
        commit_hash="30674b7"
    )

    # Registo 13: Ficha 5 - App Artigos, Sistema de Bloggers, Likes, Comentários, Ratings Médios e Menu Responsivo
    MakingOf.objects.create(
        titulo="Ficha 5: App Artigos, Bloggers, Likes, Comentários e Menu Responsivo",
        entidade="Artigos, Comentario, Rating, Home Navbar",
        descricao_processo="Criação da app 'artigos', destinada à publicação de conteúdos. Implementação dos modelos Artigo, Comentario e Rating. Criação automática do grupo 'bloggers' no registo de utilizadores. Integração de likes e sistema de comentários dinâmico (comentários anónimos permitidos!). Criação de 3 artigos de teste. Implementação de menu responsivo hambúrguer (dropdown) no topo da Home Page.",
        justificacao_modelacao="O modelo Rating foi desenhado com relação ForeignKey para o Artigo. O cálculo da média das pontuações é feito em tempo real com a função 'media_ratings()' no modelo Artigo, evitando redundância na base de dados. O modelo Comentario passou a permitir 'autor' como nulo para que visitantes anónimos possam comentar usando um campo de nome customizado.",
        sugestoes_implementadas="Utilizadores que se registam entram automaticamente no grupo 'bloggers'. Apenas membros deste grupo podem criar artigos e editar os seus próprios artigos. A navegação no topo da Landing Page foi atualizada para incluir a ligação de Artigos e adaptada com um botão hambúrguer responsivo para telemóveis.",
        erros_correcao="Dificuldade: Permitir comentários anónimos mantendo a integridade do modelo. Correção: O campo 'autor' passou a aceitar NULL e adicionámos o campo 'autor_nome' padrão 'Anónimo' para quando o utilizador não está logado.\n\nDificuldade: Conflitos com o reverse das rotas do accounts no login do link mágico. Correção: Ajustadas importações corretas de 'reverse' após alterações.",
        uso_ia="A Inteligência Artificial Generativa (Antigravity) funcionou como copiloto ativo. Ajudou na estruturação limpa dos formulários múltiplos (comentário + classificação), na otimização do CSS responsivo da barra de topo e no povoamento automático da base de dados com 3 artigos interessantes (Markdown, Soft Skills e Design Responsivo). A IA gerou ainda as imagens de herói personalizadas inspiradas em League of Legends (lol_hero.png).",
        data=date(2026, 5, 18),
        tipo_registo="Implementação de Feature e Refactoring",
        quantidade_iteracoes=6,
        commit_hash="2395e80"
    )

    print("Base de dados de Making Of preenchida com sucesso e alinhada com o histórico Real de Git!")

if __name__ == '__main__':
    populate()

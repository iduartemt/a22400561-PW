from django.db import migrations


def add_external_api_makingof(apps, schema_editor):
    MakingOf = apps.get_model("portfolio", "MakingOf")

    MakingOf.objects.update_or_create(
        titulo="Integração de uma API Externa de Jogos",
        defaults={
            "entidade": "API externa de Jogos",
            "descricao_processo": (
                "Foi criada no portfólio uma página dedicada ao consumo da API externa "
                "de Jogos desenvolvida por um colega. A página está disponível em "
                "/api-externa/ e demonstra a comunicação entre duas aplicações Django "
                "independentes através de endpoints REST.\n\n"
                "A página permite listar jogos obtidos através do endpoint GET /api/jogos, "
                "filtrar por título, género e ano de lançamento, ordenar resultados, consultar "
                "detalhes e realizar operações de criação, edição e remoção com pedidos POST, "
                "PUT e DELETE."
            ),
            "decisoes_tomadas": (
                "A integração foi implementada nas views do Django com a biblioteca requests, "
                "mantendo a página dentro da estrutura MVT usada no portfólio. A comunicação "
                "com a API externa foi concentrada numa função auxiliar responsável por construir "
                "os pedidos HTTP, adicionar o header X-API-Key e definir um tempo limite.\n\n"
                "Foram criados templates simples para listagem, detalhe, edição e confirmação "
                "de eliminação, separando a apresentação da lógica de comunicação com a API."
            ),
            "erros_correcao": (
                "Durante o desenvolvimento, a API externa alterou o modelo de dados: cada jogo "
                "deixou de estar associado apenas a uma consola por consola_id e passou a poder "
                "pertencer a várias consolas através de consolas_ids.\n\n"
                "Esta alteração originou erros 422 ao criar jogos, porque o payload enviado pelo "
                "portfólio já não correspondia ao schema esperado. A correção consistiu em substituir "
                "consola_id por consolas_ids, adaptar os formulários para aceitarem vários IDs e "
                "converter texto como 1,2,3 numa lista Python [1, 2, 3]."
            ),
            "justificacao_modelacao": (
                "A alteração para consolas_ids representa melhor a relação entre jogos e consolas, "
                "porque um jogo pode estar disponível em várias plataformas. No consumo da API, esta "
                "decisão obrigou a tratar esse campo como uma lista de identificadores e não como um "
                "valor único."
            ),
            "uso_ia": (
                "Foi usada IA como apoio à análise do erro 422, interpretação da alteração feita na "
                "API externa e validação dos pontos do código que tinham de ser atualizados. As "
                "alterações foram revistas e testadas manualmente."
            ),
            "sugestoes_implementadas": (
                "Foi implementada a sugestão do colega para alterar o consumo da API, deixando de "
                "enviar consola_id e passando a enviar consolas_ids como lista. Também foram adaptados "
                "os formulários e a página de detalhe para refletirem esta mudança."
            ),
            "evidencia": "/api-externa/",
            "data": "2026-06-11",
            "tipo_registo": "Integração API",
            "commit_hash": "43f3c07",
            "quantidade_iteracoes": 3,
        },
    )


def remove_external_api_makingof(apps, schema_editor):
    MakingOf = apps.get_model("portfolio", "MakingOf")
    MakingOf.objects.filter(titulo="Integração de uma API Externa de Jogos").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0026_alter_tfc_palavras_chave"),
    ]

    operations = [
        migrations.RunPython(add_external_api_makingof, remove_external_api_makingof),
    ]

## 1. Objetivo
O objetivo desta fase foi modelar e implementar incrementalmente uma aplicação Django para um portfólio académico e profissional, incluindo entidades como Licenciatura, Unidade Curricular, Projetos, Tecnologias, Competências, Formações, TFCs e Making Of.

## 2. Fotografias do DER e apontamentos
- DER inicial: `media/makingof/Relacoes.jpeg`
- Screenshot admin Licenciatura: `media/makingof/admin_licenciatura.png`
- Screenshot admin Projeto: `media/makingof/admin_projeto.png`
- Screenshot commit Docente: `media/makingof/commit_docente_admin.png`

## 2. Fotografias do DER e apontamentos
- DER inicial: `media/makingof/Relacoes.jpeg`
- Screenshot admin Licenciatura: `media/makingof/admin_licenciatura.png`
- Screenshot admin Projeto: `media/makingof/admin_projeto.png`
- Screenshot commit Docente: `media/makingof/commit_docente_admin.png`

## 4. Erros identificados e correções
### Erro 1 — Tecnologia
Inicialmente foi usado `ImageField` para o atributo `logo`, o que originou erro por falta da biblioteca Pillow.

**Correção:** o campo foi substituído por `website_oficial`, simplificando a implementação.

### Erro 2 — Competência
O campo ManyToMany com Tecnologia estava obrigatório.

**Correção:** foi adicionado `blank=True` para permitir competências interpessoais sem tecnologias associadas.

### Erro 3 — MakingOf
Ao alterar campos do modelo já existente, surgiram problemas de migração por campos obrigatórios.

**Correção:** os campos textuais foram definidos com `blank=True`.

## 5. Justificação das decisões de modelação

### Licenciatura
- Incluído `sigla` para representação resumida do curso.
- Relação 1:N com UnidadeCurricular porque uma licenciatura tem várias UCs.

### UnidadeCurricular
- `ects` representa o peso académico.
- Relação N:M com Docente porque uma UC pode ter vários docentes.

### Projeto
- `github_url` foi incluído por relevância profissional.
- ManyToMany com Tecnologia para representar várias stacks.

### MakingOf
- `evidencia` guarda o caminho para fotos e screenshots.
- FK opcionais permitem relacionar o processo com entidades específicas.

## 6. Uso de Inteligência Artificial
Foi utilizado o ChatGPT como ferramenta de apoio na interpretação do enunciado, validação das relações entre entidades, boas práticas de Django e organização incremental do projeto.

Todas as decisões foram revistas, implementadas e justificadas manualmente, garantindo compreensão total do funcionamento e capacidade de adaptação na defesa.

## 7. Revisão da Modelação com Dados da API Lusófona

Após explorar os dados disponíveis nos ficheiros JSON das APIs da Lusófona, procedeu-se a uma revisão da modelação para incorporar informações relevantes do curso e das unidades curriculares.

### Dados Disponíveis
- **Curso Geral (ULHT260-PT.json)**: Contém `reasons` (razões para escolher o curso) e `courseFlatPlan` (lista de UCs com códigos, nomes, anos, semestres, ECTS, etc.).
- **Detalhes das UCs (ULHT260-XXX-PT.json)**: Incluem `objectives`, `programme`, `presentation`, `bibliography`, `assessment`, `methodology`, `language`, `nature`, `type`, `internship`, `organicUnit`, etc.

### Alterações na Modelação

#### Licenciatura
- Adicionados campos: `diploma_degree`, `course_code`, `reasons` (JSONField para armazenar lista de razões).
- Justificação: Captura metadados do curso geral, enriquecendo a entidade sem complexidade excessiva.

#### UnidadeCurricular
- Adicionados campos: `curricular_unit_code` (único, chave de integração), `language`, `nature`, `type`, `internship`, `objectives`, `programme`, `presentation`, `bibliography`, `assessment`, `methodology`, `organic_unit`, `group_code`, `institution_code`.
- Justificação: Os dados da API fornecem conteúdo rico em texto/HTML para objetivos, programa, bibliografia e avaliação, essenciais para um portfólio académico. Mantidos como TextField para preservar formatação. Não foi criada entidade separada para evitar normalização desnecessária, já que são atributos complementares da UC.

### Implementação do Import
- Criado script `import_cursos_uc_doJson.py` que:
  - Importa curso geral e cria Licenciatura.
  - Importa lista completa de docentes da Lusófona (158 docentes, 42 com dados completos incluindo grau académico, regime, ORCID, Ciência Vitae).
  - Processa `courseFlatPlan` para criar UCs básicas.
  - Enriquecce UCs com detalhes dos ficheiros individuais.
- Modificado script `carregar_tfcs.py` para preservar dados importados da Lusófona e reutilizar docentes existentes.
- Resultado: Integração completa dos dados Lusófona com dados dos TFCs.

### Dados Finais Importados
- **1 Licenciatura**: Engenharia Informática (com 6 razões para escolher o curso)
- **31 Unidades Curriculares**: Com conteúdo detalhado (objetivos, programas, bibliografia, avaliação)
- **158 Docentes**: 42 com dados completos da Lusófona + docentes dos TFCs
- **559 TFCs**: Com orientadores associados e tecnologias
- **275 Tecnologias**: Extraídas dos TFCs

### Decisões Não Tomadas
- Não foi criada entidade `Curso` separada de `Licenciatura`, pois o foco é o portfólio pessoal e a entidade existente serve bem.
- Não foi normalizada `programme` em módulos/tópicos, mantendo como texto estruturado para simplicidade.
- Competências não foram extraídas automaticamente dos objetivos/programas, ficando para mapeamento manual posterior.

Esta revisão garante que a aplicação agora reflete fielmente a estrutura e conteúdo do curso da Lusófona, proporcionando uma base sólida para o portfólio académico.

## 8. Povoamento da Base de Dados (Teste)
**Data:** 30/04/2026

Para garantir que todas as funcionalidades e templates da aplicação pudessem ser validados, foram inseridos dados de teste em todas as tabelas que se encontravam vazias ou com poucos dados.

### Ações Realizadas:
- **Licenciatura**: Adicionadas 2 novas licenciaturas (totalizando 3).
- **Competência**: Criadas 3 competências técnicas (totalizando 3) associadas aleatoriamente a tecnologias existentes.
- **Formação**: Criadas 3 formações profissionais (totalizando 3) associadas a licenciaturas e competências.
- **Projeto**: Criados 3 projetos (totalizando 3) associados a unidades curriculares, tecnologias e competências.
- **Aluno**: Verificado que já existiam 3 alunos registados.

Esta etapa permitiu verificar o correto funcionamento das relações ManyToMany e ForeignKey nos templates da aplicação e no Django Admin.

## 9. Implementação de Interfaces CRUD Dinâmicas
**Data:** 10/05/2026

Foi implementada a gestão completa de dados (Create, Read, Update, Delete) para os modelos chave do sistema: Projetos, Tecnologias, Competências e Formações, permitindo a manipulação direta na interface pública.

### Ações Realizadas:
- **Formulários:** Criação do `forms.py` utilizando o `ModelForm` do Django, que gerou dinamicamente os campos HTML baseados nos campos da BD.
- **Lógica de Views:** Criação de views que processam o tráfego HTTP (GET para ler o formulário e POST para gravar com `form.save()`).
- **Interfaces:** Adição de botões visuais de "Adicionar", "Editar" e "Apagar" integrados nos templates de listagem e confirmação de eliminação.

### Dificuldades e Erros Corrigidos:
- **Desajuste de Nomenclatura:** Ocorreram erros de `AttributeError` e `NoReverseMatch` devido ao facto de ter nomeado funções no plural nas Views enquanto as URLs procuravam o singular. Resolvido uniformizando para singular.
- **Limpeza de Código:** Identificaram-se variáveis clonadas por "copy-paste" (ex: instanciar ProjetoForm ao editar Tecnologia), o que exigiu revisão criteriosa das queries.

### Considerações Úteis e Vantagens do Django:
- **Rapidez Absurda:** O facto de o Django gerar automaticamente HTML com os nomes corretos dos inputs e lidar com os relacionamentos N:M poupou horas de desenvolvimento.
- **Segurança Ativa:** O uso do token `{% csrf_token %}` nativo da framework protege a aplicação contra injeções de dados maliciosas, o que é fundamental em aplicações web profissionais.
- **Arquitetura:** A separação MVT facilitou replicar a funcionalidade para múltiplos modelos sequencialmente.

## 10. Expansão do Modelo MakingOf
**Data:** 02/05/2026 (Commit: `2e71603`)

Introduziram-se melhorias no modelo `MakingOf` para permitir uma rastreabilidade técnica superior do desenvolvimento da aplicação.

### Alterações:
- **Novos Campos:** Adição de `commit_hash` e `quantidade_iteracoes` para quantificar os commits reais da equipa no projeto.
- **Justificação:** Melhoria da integridade académica do portefólio, garantindo visibilidade transparente do histórico de versionamento.

## 11. Reestruturação da Navegação de UCs
**Data:** 06/05/2026 (Commit: `ef75b6c`)

Refinamento na apresentação hierárquica do plano curricular.

### Decisões:
- **Lógica:** Alteração do comportamento de listagem para que as Unidades Curriculares não fossem visualizadas apenas isoladamente, mas sim aninhadas nos detalhes da Licenciatura a que pertencem.
- **Impacto:** Melhoria drástica da User Experience (UX), simulando fielmente a estrutura real de um plano de estudos universitário.

## 12. Reestruturação e Categorização de Tecnologias
**Data:** 10/05/2026

Focando na evolução contínua da documentação técnica da aplicação.

### Alterações Realizadas:
- **Nova Classe `TipoTecnologia`**: Criação de uma tabela independente para gerir tipos (Frontend, Backend, Base de Dados, Outros), permitindo escalabilidade nas categorias.
- **Relação ForeignKey**: Adicionada ligação em `Tecnologia` para o novo modelo `TipoTecnologia`.
- **Detalhe Descritivo**: Alargamento concetual do campo `descricao` (com ajuda de meta-informação help_text) para garantir cobertura do "que faz, o que permite e opinião crítica".
- **Integração na Página Sobre**: Implementada a query de agregação dinâmica que agrupa e exibe o stack tecnológico associado ao projeto atual da plataforma.

## 13. Histórico de Commits (Versionamento)
Abaixo encontra-se o extrato real dos commits mais recentes efetuados no repositório para a implementação destas funcionalidades.

| Hash | Data | Mensagem de Commit |
| :--- | :--- | :--- |
| `3254e77` | 2026-05-10 | feat: add about page with MVT documentation and project tutorial video |
| `facfa88` | 2026-05-10 | feat: add 'sobre' page with documentation, MVT architecture diagram, and tech stack details |
| `23d3c3c` | 2026-05-10 | feat: add documentation page for MVT architecture and project tech stack |
| `c11ed5b` | 2026-05-10 | feat: implement CRUD operations for projects with corresponding forms and templates |
| `ef75b6c` | 2026-05-06 | feat: implement templates for curricular units listing and detailed view pages |
| `0919916` | 2026-05-06 | feat: implement portfolio navigation and views for courses, curriculum units, and academic details |
| `2e71603` | 2026-05-02 | feat: expand MakingOf model with tracking fields and implement corresponding template view |
| `614ee4a` | 2026-05-02 | feat: implement URL routing, views, and templates for portfolio sections including competencies, education, and making of |
| `cad2a60` | 2026-05-02 | feat: implement main dashboard and define routing and views for portfolio sections |
| `9f63ee4` | 2026-05-02 | feat: implement main menu home page and views for TFCs and Docentes |
| `317bfef` | 2026-05-02 | feat: add views, URLs, and templates to render portfolio sections for courses, projects, and technologies |
| `ca8d818` | 2026-05-02 | feat: implement academic curriculum page with grouped course list view |
| `e2cb9bf` | 2026-05-02 | docs: update making_of documentation with database population test details |

## 14. Integração da API RESTful de Receitas
**Data:** 02/06/2026

Foi integrada no portfólio uma API RESTful para gerir receitas culinárias, ingredientes e utilizadores.
A API foi construída com Django Ninja e disponibiliza operações CRUD através dos métodos HTTP
`GET`, `POST`, `PUT` e `DELETE`. A documentação Swagger é gerada automaticamente em `/api/docs`.

### Reflexão
A construção da API permitiu compreender melhor a separação entre páginas HTML e endpoints que
devolvem dados estruturados em JSON. Os schemas ajudam a validar os dados recebidos e a documentação
Swagger facilita a exploração e o teste dos endpoints. A integração no mesmo projeto Django também
permitiu disponibilizar a API no ambiente de produção já existente.


## 15. Integração de uma API Externa de Jogos
**Data:** 11/06/2026

Foi criada no portfólio uma página dedicada ao consumo da API externa de Jogos desenvolvida por um colega. Esta página está disponível em `/api-externa/` e demonstra a comunicação entre duas aplicações Django independentes através de endpoints REST.

### Funcionalidades Implementadas
- Listagem dos jogos obtidos através do endpoint `GET /api/jogos`.
- Filtros por título, género e ano de lançamento.
- Ordenação local dos resultados por título, ano ou nota.
- Consulta do detalhe de cada jogo.
- Operações de criação, edição e remoção de jogos através de pedidos `POST`, `PUT` e `DELETE`.
- Utilização do header `X-API-Key` nas operações protegidas.

### Decisões Técnicas
A integração foi implementada nas views do Django com a biblioteca `requests`, mantendo a página dentro da estrutura MVT já utilizada no portfólio. A comunicação com a API externa foi concentrada numa função auxiliar, responsável por construir os pedidos HTTP, adicionar o header da API Key e definir um tempo limite para evitar que a aplicação fique bloqueada caso a API externa não responda.

Para a interface, foram criados templates simples para a listagem, detalhe, edição e confirmação de eliminação. Esta abordagem permitiu separar a apresentação da lógica de comunicação com a API, tornando o código mais fácil de compreender e testar.

### Dificuldades Encontradas
Durante o desenvolvimento, a API externa sofreu uma alteração no modelo de dados: inicialmente cada jogo estava associado apenas a uma consola através do campo `consola_id`, mas passou a poder pertencer a várias consolas. Com esta mudança, os pedidos de criação e edição deixaram de aceitar `consola_id` e passaram a exigir `consolas_ids`, uma lista de identificadores.

Esta alteração originou erros `422` ao criar jogos, pois o payload enviado pelo portfólio já não correspondia ao schema esperado pela API externa. A correção consistiu em adaptar os formulários para aceitarem vários IDs de consolas e converter o texto introduzido pelo utilizador, por exemplo `1,2,3`, numa lista Python `[1, 2, 3]`.

### Correções Realizadas
- Substituição de `consola_id` por `consolas_ids` no payload enviado para a API.
- Alteração dos formulários para permitir a introdução de vários IDs de consolas.
- Atualização da página de detalhe para apresentar a lista de consolas associadas ao jogo.
- Testes locais ao payload para confirmar que `1,2,3` era convertido corretamente em `[1, 2, 3]`.
- Teste real ao endpoint `GET /api/jogos`, confirmando que a API externa respondia com `200` e devolvia `consolas_ids`.

### Reflexão
Esta integração ajudou a perceber melhor a diferença entre desenvolver uma API e consumir uma API criada por outra pessoa. Quando a API pertence ao próprio projeto, é mais fácil controlar o modelo de dados e prever as alterações. Ao consumir uma API externa, é necessário adaptar a aplicação às decisões de outro programador, lidar com mudanças nos schemas e testar cuidadosamente os formatos enviados e recebidos.

O erro `422` foi particularmente útil para compreender a importância da validação dos dados. A página não estava necessariamente errada na sua estrutura, mas estava desatualizada em relação ao contrato da API. Esta situação mostrou que uma integração entre sistemas depende não só do código funcionar, mas também de existir alinhamento entre quem fornece a API e quem a consome.

No final, a página da API externa tornou o portfólio mais completo, porque demonstra uma competência essencial no desenvolvimento web: integrar dados vindos de outro serviço, tratar respostas JSON, autenticar pedidos com API Key e adaptar a interface quando o modelo de dados evolui.

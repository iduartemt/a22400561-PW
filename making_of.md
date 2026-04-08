## 1. Objetivo
O objetivo desta fase foi modelar e implementar incrementalmente uma aplicação Django para um portfólio académico e profissional, incluindo entidades como Licenciatura, Unidade Curricular, Projetos, Tecnologias, Competências, Formações, TFCs e Making Of.

## 2. Fotografias do DER e apontamentos
- DER inicial: `media/makingof/der_v1.jpg`
- Screenshot admin Licenciatura: `media/makingof/admin_licenciatura.png`
- Screenshot admin Projeto: `media/makingof/admin_projeto.png`
- Screenshot commit Docente: `media/makingof/commit_docente_admin.png`

## 2. Fotografias do DER e apontamentos
- DER inicial: `media/makingof/der_v1.jpg`
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
  - Processa `courseFlatPlan` para criar UCs básicas.
  - Enriquecce UCs com detalhes dos ficheiros individuais.
- Resultado: 1 Licenciatura e 31 Unidades Curriculares importadas com sucesso, incluindo conteúdos detalhados.

### Decisões Não Tomadas
- Não foi criada entidade `Curso` separada de `Licenciatura`, pois o foco é o portfólio pessoal e a entidade existente serve bem.
- Não foi normalizada `programme` em módulos/tópicos, mantendo como texto estruturado para simplicidade.
- Competências não foram extraídas automaticamente dos objetivos/programas, ficando para mapeamento manual posterior.

Esta revisão garante que a aplicação agora reflete fielmente a estrutura e conteúdo do curso da Lusófona, proporcionando uma base sólida para o portfólio académico.
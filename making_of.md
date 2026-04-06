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
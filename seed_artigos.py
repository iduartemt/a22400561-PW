import os
import django

# Configurar o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User, Group
from artigos.models import Artigo

def seed():
    print("A iniciar o povoamento de artigos de teste...")
    
    # 1. Garante que o grupo 'bloggers' existe
    grupo_bloggers, _ = Group.objects.get_or_create(name='bloggers')
    
    # 2. Garante que temos pelo menos um utilizador autor para associar aos artigos
    user, created = User.objects.get_or_create(username='admin')
    if created:
        user.set_password('admin123')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print("Criado utilizador superuser 'admin' com a password 'admin123'")
    
    # Adiciona o user ao grupo bloggers
    user.groups.add(grupo_bloggers)
    
    # 3. Criar os 3 artigos interessantes se ainda não existirem
    artigos_dados = [
        {
            "titulo": "O Poder do Markdown no Desenvolvimento de Software",
            "texto": """O Markdown tornou-se o padrão da indústria para documentação de código. 

Seja no ficheiro README.md do GitHub, na documentação de APIs, ou até nos teus apontamentos diários, o Markdown permite escrever texto formatado de forma extremamente rápida sem tirar as mãos do teclado.

Por que deves aprender?
1. É legível tanto em formato de código como renderizado.
2. É suportado por quase todas as plataformas (GitHub, GitLab, Notion, Discord).
3. Permite adicionar blocos de código com realce de sintaxe facilmente.

Começa hoje mesmo a estruturar os teus READMEs usando cabeçalhos, listas e links para tornar os teus projetos muito mais profissionais!""",
            "link_externo": "https://www.markdownguide.org/"
        },
        {
            "titulo": "Soft Skills: A Arma Secreta de um Engenheiro de Software",
            "texto": """Escrever bom código é apenas metade do trabalho de um desenvolvedor. A outra metade, e muitas vezes a mais desafiante, envolve lidar com pessoas.

As chamadas 'Soft Skills' (competências interpessoais) são o que distingue um programador comum de um líder de equipa excelente.

Principais Soft Skills a desenvolver:
- **Comunicação Clara**: Saber explicar conceitos complexos a pessoas não-técnicas.
- **Empatia**: Entender as dores do cliente e as dificuldades dos teus colegas de equipa.
- **Resolução de Conflitos**: Manter a calma e focar em soluções quando as coisas correm mal.

Não te foques apenas em linguagens de programação; treina a tua capacidade de ouvir e colaborar!""",
            "link_externo": "https://pt.wikipedia.org/wiki/Compet%C3%AAncias_comportamentais"
        },
        {
            "titulo": "Design Responsivo: Tornar Websites Acessíveis a Todos",
            "texto": """Hoje em dia, a maioria das pessoas acede à internet através de telemóveis. Um website que só funciona bem no ecrã de um computador já nasceu desatualizado.

O Design Responsivo é a prática de programar páginas web que se adaptam automaticamente a qualquer tamanho de ecrã (computadores, tablets e telemóveis).

Como funciona?
Usando HTML bem estruturado e CSS moderno, especialmente:
- **Media Queries**: Permitem aplicar estilos diferentes com base na largura do ecrã.
- **Flexbox e CSS Grid**: Facilitam o alinhamento de elementos sem quebras rígidas de layout.
- **Imagens Fluidas**: Imagens que encolhem e aumentam conforme o espaço disponível.

Criar um menu responsivo (hambúrguer) é o primeiro grande passo para garantir que o teu portfólio fica impecável em qualquer dispositivo!""",
            "link_externo": "https://developer.mozilla.org/pt-PT/docs/Learn/CSS/CSS_layout/Responsive_Design"
        }
    ]

    for dados in artigos_dados:
        artigo, criado = Artigo.objects.get_or_create(
            titulo=dados["titulo"],
            defaults={
                "texto": dados["texto"],
                "link_externo": dados["link_externo"],
                "autor": user
            }
        )
        if criado:
            print(f"Artigo criado com sucesso: '{artigo.titulo}'")
        else:
            print(f"O artigo '{artigo.titulo}' já existia.")

    print("Processo de povoamento concluído!")

if __name__ == '__main__':
    seed()

# Quiz HTML Generator

Um aplicativo Python com interface gráfica que permite aos usuários gerar questionários interativos em HTML a partir de entradas de texto estruturadas. Utiliza a biblioteca `ttkbootstrap` para uma interface aprimorada.

## Recursos

- **Interface Intuitiva**: Facilita a entrada de dados de questionários.
- **Títulos Personalizados**: Permite especificar o título do documento HTML gerado.
- **Flexibilidade nas Alternativas**: Escolha a quantidade de alternativas por pergunta (2 a 6).
- **Geração Automática de HTML**: Cria arquivos HTML interativos a partir dos dados fornecidos.
- **Validação de Dados**: Garante que os dados de entrada estejam corretamente formatados e válidos.

## Instalação

### Pré-requisitos

- **Python 3.6+**: Certifique-se de ter o Python instalado. Baixe [aqui](https://www.python.org/downloads/).

### Clonar o Repositório

```bash
git clone https://github.com/seuusuario/quiz-html-generator.git
cd quiz-html-generator


Instalar Dependências
Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto.

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

Windows:
bash
Copiar código
venv\Scripts\activate
macOS/Linux:
bash
Copiar código
source venv/bin/activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Uso
Execute o aplicativo usando Python:

bash
Copiar código
python gerador_questionarios.py
Visão Geral da Interface
Instruções: Fornece diretrizes sobre como formatar os dados de entrada.

Caixa de Texto: Cole seus dados de questionário aqui. Cada linha deve seguir o formato:

mathematica
Copiar código
pergunta ; resposta 1 ; resposta 2 ; ... ; resposta N ; gabarito
N: Número de alternativas (conforme selecionado no spinbox).
gabarito: Identificador da resposta correta (ex.: a, b, c).
Exemplo para 4 Alternativas:

css
Copiar código
Qual a capital da França? ; Berlim ; Madrid ; Paris ; Roma ; c
Qual a soma de 2 + 2? ; 3 ; 4 ; 5 ; 6 ; b
Nome do Arquivo: Insira o nome desejado para o arquivo HTML gerado (sem a extensão .html).

Título do HTML: Especifique o título do documento HTML. Este título aparecerá na aba do navegador e como cabeçalho principal da página.

Quantidade de Alternativas: Selecione a quantidade de alternativas por pergunta (entre 2 e 6).

Gerar HTML: Clique no botão para gerar o arquivo HTML. O arquivo será salvo na sua área de trabalho.

Exemplo
Dados de Entrada:

css
Copiar código
Qual a capital do Brasil? ; Brasília ; São Paulo ; Rio de Janeiro ; Salvador ; a
Quanto é 5 + 7? ; 10 ; 11 ; 12 ; 13 ; c
Configurações:

Nome do Arquivo: meu_questionario
Título do HTML: Quiz de Conhecimentos Gerais
Quantidade de Alternativas: 4
Resultado: Um arquivo chamado meu_questionario.html será criado na sua área de trabalho com o título especificado e as perguntas formatadas.

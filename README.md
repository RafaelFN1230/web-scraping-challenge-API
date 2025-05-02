# web-scraping-challenge-API
# Projeto de Coleta de Dados e Geração de CSV

Este projeto realiza a coleta de dados de usuários e livros utilizando a [API do DemoQA](https://demoqa.com/swagger/), processa as informações e gera um arquivo CSV com os detalhes dos livros. A arquitetura do código foi construída seguindo os princípios da Clean Architecture, onde as responsabilidades estão bem definidas entre as camadas de uso, controle e infraestrutura.

## Arquitetura

A arquitetura foi construída utilizando o padrão Clean Architecture, com a seguinte estrutura:

- Main: A camada de inicialização, que orquestra a execução do fluxo da aplicação.
- Controller: Responsável por orquestrar a execução dos Use Cases e garantir que as interações com as camadas superiores e inferiores aconteçam corretamente.
- Use Cases: Contém a lógica de negócios, realizando ações como gerar usuários, obter tokens, coletar livros e gerar o CSV.
- DTO (Data Transfer Objects): Representa os dados que são trocados entre as camadas.
- Entities: Representa os dados principais que estão sendo manipulados (ex: Livro, Usuário).
- Infrastructure: Onde as interações com a API externa acontecem, incluindo chamadas HTTP e coleta de dados.

## Fluxo do Programa
``` mermaid
sequenceDiagram
    participant Main
    participant Controller
    participant GenerateFakeUserUseCase
    participant CreateUserUseCase
    participant GetTokenUseCase
    participant GetBooksUseCase
    participant GenerateBooksCsvUseCase
    participant Infrastructure

    Main->>Controller: Inicia o workflow
    Controller->>GenerateFakeUserUseCase: Chama GenerateFakeUserUseCase
    GenerateFakeUserUseCase->>Controller: Retorna o usuário gerado
    Controller->>CreateUserUseCase: Chama CreateUserUseCase com usuário gerado
    CreateUserUseCase->>Infrastructure: Cria usuário no sistema
    Infrastructure->>CreateUserUseCase: Confirma criação do usuário
    CreateUserUseCase->>Controller: Retorna confirmação de criação
    Controller->>GetTokenUseCase: Chama GetTokenUseCase com usuário criado
    GetTokenUseCase->>Infrastructure: Solicita token para o usuário criado
    Infrastructure->>GetTokenUseCase: Retorna token
    GetTokenUseCase->>Controller: Retorna o token
    Controller->>GetBooksUseCase: Chama GetBooksUseCase com o token
    GetBooksUseCase->>Infrastructure: Solicita livros com o token
    Infrastructure->>GetBooksUseCase: Retorna lista de livros
    GetBooksUseCase->>Controller: Retorna livros
    Controller->>GenerateBooksCsvUseCase: Chama GenerateBooksCsvUseCase com livros
    GenerateBooksCsvUseCase->>Controller: Gera CSV com as informações de livros
    Controller->>Main: Retorna CSV gerado
```
- GenerateFakeUserUseCase: Gera um usuário fictício.
- CreateUserUseCase: Cria o usuário gerado.
- GetTokenUseCase: Obtém um token de acesso para o usuário criado.
- GetBooksUseCase: Obtém uma lista de livros utilizando o token gerado.
- GenerateBooksCsvUseCase: Gera um arquivo CSV com os dados dos livros (Título, Autor, Editora, Imagem).

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. Para instalar as dependências necessárias, execute o seguinte comando:
```
pip install -r requirements.txt
```

## Executando o Projeto

Para executar o fluxo completo da aplicação, basta rodar o script principal (`main.py`):
```
python main.py
```

Isso irá executar o fluxo completo: gerar o usuário, criar o usuário, obter o token, coletar os livros e gerar o CSV de saída.

### Parâmetros de Entrada

Não há parâmetros de entrada diretos para a execução do fluxo, mas os dados como o usuário gerado e o token obtido são processados internamente.

### Arquivo de Saída

O arquivo de saída, contendo os dados dos livros em formato CSV, será gerado na pasta output. O arquivo terá as seguintes colunas:

- Title: O título do livro.
- Author: O autor do livro.
- Publisher: A editora do livro.
- Image: O link para a imagem da capa do livro. **Nota**: A API não retorna a URL da imagem dos livros, portanto, o valor da coluna `Image` será preenchido com o caractere `" - "`.

## Logs

Durante a execução do programa, logs detalhados sobre o processo serão gravados no arquivo logs. O arquivo pode ser usado para rastrear a execução e identificar possíveis problemas.

## Testes

O projeto inclui testes unitários para todos os Use Cases e Endpoints, bem como para o Controller e Main. Para executar os testes, basta rodar o comando:
```
pytest test/ -v
```
Isso irá rodar todos os testes presentes na pasta test/.

Se você quiser rodar um teste específico, execute o comando com o nome do arquivo de teste desejado:
```
pytest test/nome_do_arquivo.py
```
### Estrutura de Testes
- **API**: Teste para verificar o funcionamento dos endpoints da API.
- **Use Cases**: Testes para verificar a lógica de cada caso de uso (como gerar usuário, criar usuário, obter livros, etc.).
- **Controller**: Testes para garantir que o controller orquestre corretamente a execução dos use cases.
- **Main**: Testes para verificar a execução do fluxo principal.

## Estrutura de Pastas
```
├── .pytest_cache                  # Cache do pytest
├── .venv                          # Ambiente virtual do Python
├── documentation                   # Documentação do projeto
├── input                           # Arquivos de entrada (se houver)
├── logs                            # Logs da execução do projeto
│   └── app.log                    # Log principal da aplicação
├── notebooks                       # Notebooks Jupyter (se houver)
├── output                          # Arquivo de saída gerado
│   └── books_api.csv              # CSV gerado com os dados dos livros
├── src                             # Código-fonte da aplicação
│   ├── _temp                       # Arquivos temporários
│   ├── domain                      # Camada de domínio
│   │   └── entities                # Entidades (ex: Book, User)
│   │       ├── Book.py             # Entidade Livro
│   │       └── User.py             # Entidade Usuário
│   ├── infrastructure              # Camada de infraestrutura (API)
│   │   └── API                     # Interação com a API externa
│   │       ├── create_user.py      # Endpoint para criação de usuário
│   │       ├── get_books.py        # Endpoint para obter livros
│   │       ├── get_token.py        # Endpoint para obter token
│   │       ├── get_user_details.py # Endpoint para obter detalhes do usuário
│   │       └── validate_authorization.py # Endpoint para validação de autorização
│   ├── interface                   # Camada de interface (Controller, DTOs, Schema)
│   │   ├── controller              # Controlador principal
│   │   │   ├── DTOs                # Data Transfer Objects
│   │   │   │   ├── BookDTO.py      # DTO do Livro
│   │   │   │   ├── UserDTO.py      # DTO do Usuário
│   │   │   │   └── mapper.py       # Mapeamento de DTOs
│   │   │   └── main_controller.py  # Controlador principal
│   │   └── schema                  # Esquemas de validação
│   │       └── api                 # Esquemas da API
│   │           └── api_book_schema.py # Esquema para validação de livros
│   ├── use_case                    # Casos de uso
│   │   ├── create_user_use_case.py # Caso de uso para criar usuário
│   │   ├── generate_csv_use_case.py# Caso de uso para gerar CSV
│   │   ├── generate_fake_user.py  # Caso de uso para gerar usuário fictício
│   │   ├── get_books_use_case.py  # Caso de uso para obter livros
│   │   └── get_token_use_case.py  # Caso de uso para obter token
│   └── utils                       # Utilitários
│       ├── logger.py               # Funções de logging
│       └── random_helpers.py       # Funções auxiliares (ex: geração de dados aleatórios)
├── test                            # Testes unitários
├── .env                            # Arquivo de configuração de ambiente
├── .env.example                    # Exemplo de configuração de ambiente
├── .env.test                       # Configuração de ambiente para testes
├── .gitignore                      # Arquivo para ignorar arquivos não rastreados pelo Git
├── pytest.ini                      # Configuração do pytest
├── README.md                       # Documentação do projeto
├── requirements.txt                # Dependências do projeto
```

# Considerações Finais

- A estrutura do código foi organizada com base nos princípios de Clean Architecture, o que facilita a manutenção e evolução do sistema.

- O arquivo CSV gerado conterá as informações mais relevantes sobre os livros, podendo ser utilizado para análise posterior.

- Logs estão disponíveis para rastrear qualquer erro ou problema durante a execução do programa.


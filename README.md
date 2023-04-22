# Library-CRUD
#CRUD de Livros com Flask

Este projeto demonstra um CRUD (Create, Read, Update, Delete) simples de livros usando o microframework Flask em Python. 
O projeto é organizado em uma estrutura de pastas simples e inclui testes unitários para garantir a funcionalidade correta das operações CRUD.


#<b>Estrutura do Projeto</b>
<p>
├── app.py
</p><p>
├── add_books.py
</p><p>
├── routes.py
</p><p>
└── tests
</p>
 


#<b>Requisitos</b>
Python 3.7+
Flask 2.0.1+


#<b>Instalação</b>
Clone este repositório.
Crie um ambiente virtual e ative-o.
Instale as bibliotecas necessárias.


#<b>Execução</b>
Execute o aplicativo Flask com o comando:

python app.py
O aplicativo será iniciado na porta 5000. Para testar as rotas, você pode usar um navegador, cURL ou um aplicativo como o Postman.


#<b>Funcionalidades</b>
Este CRUD de livros possui as seguintes rotas e funcionalidades:

GET /books: Lista todos os livros.
POST /books: Adiciona um novo livro.
GET /books/<int:book_id>: Recupera um livro específico por ID.
PUT /books/<int:book_id>: Atualiza um livro específico por ID.
DELETE /books/<int:book_id>: Remove um livro específico por ID.


#<b>Testes</b>
O arquivo test_app.py contém testes unitários para todas as operações CRUD. Para executar os testes, navegue até a pasta raiz do projeto e execute:

python -m unittest tests/test_app.py

Os testes unitários incluem:

Adicionar um novo livro (test_add_book).

Listar todos os livros (test_get_books).

Recuperar um livro específico por ID (test_get_book_by_id).

Atualizar um livro específico por ID (test_update_book).

Remover um livro específico por ID (test_delete_book).

Os testes garantem que todas as operações CRUD estão funcionando corretamente e que as respostas HTTP esperadas são retornadas.

#<b>Conclusão</b>
Este projeto fornece um exemplo básico de um CRUD de livros usando Flask, demonstrando a criação, leitura, atualização e exclusão de registros de livros. Com testes unitários e uma organização de pastas simples, o projeto é fácil de entender e pode ser usado como base para projetos futuros ou como um exemplo de aprendizado para trabalhar com o Flask.

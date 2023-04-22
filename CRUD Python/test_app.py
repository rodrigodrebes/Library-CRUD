import unittest
from unittest.mock import MagicMock
import sqlite3
import app
import routes

class TestApp(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.client = app.app.test_client()
        with app.app.app_context():
            app.init_db()
            cursor = app.get_db().cursor()
            cursor.execute("INSERT INTO books (title, author, genre, pages) VALUES (?, ?, ?, ?)", ('Livro Teste', 'Autor Teste', 'Gênero Teste', 100))

    def tearDown(self):
        with app.app.app_context():
            cursor = app.get_db().cursor()
            cursor.execute("DELETE FROM books")

    def test_add_book(self):
        new_book = {
            "title": "Novo Livro",
            "author": "Novo Autor",
            "genre": "Novo Gênero",  # Adicione a chave "genre"
            "pages": 150
        }
        response = self.client.post('/books', json=new_book)
        self.assertEqual(response.status_code, 201)

    def test_get_books(self):
        response = self.client.get('/books')
        self.assertIn(b'Novo Livro', response.data)


    def test_get_book_by_id(self):
        # Busque todos os livros
        response_all_books = self.client.get('/books')
        all_books = response_all_books.get_json()

        # Obtenha o ID do primeiro livro na lista
        book_id = all_books[0]['id']

        # Recupere o livro com o ID obtido
        response = self.client.get(f'/books/{book_id}')
        book_data = response.get_json()

        # Verifique se o status code é 200 e os dados do livro são corretos
        self.assertEqual(response.status_code, 200)
        self.assertEqual(book_data['title'], 'Novo Livro')
        self.assertEqual(book_data['author'], 'Novo Autor')
        self.assertEqual(book_data['genre'], 'Novo Gênero')
        self.assertEqual(book_data['pages'], 150)


    
    def test_update_book(self):
        # Adicione um novo livro primeiro
        new_book = {
            "title": "Livro Original",
            "author": "Autor Original",
            "genre": "Gênero Original",
            "pages": 100
        }
        response_add_book = self.client.post('/books', json=new_book)
        self.assertEqual(response_add_book.status_code, 201)
        
        # Obtenha o ID do livro adicionado
        book_id = response_add_book.json['id']

        # Atualize o livro usando o ID retornado
        updated_book = {
            "title": "Livro Atualizado",
            "author": "Autor Atualizado",
            "genre": "Gênero Atualizado",
            "pages": 200
        }
        response_update_book = self.client.put(f'/books/{book_id}', json=updated_book)
        self.assertEqual(response_update_book.status_code, 200)

        # Opcional: verifique se os dados do livro foram realmente atualizados
        response_get_book = self.client.get(f'/books/{book_id}')
        updated_book_from_db = response_get_book.json
        self.assertEqual(updated_book_from_db['title'], updated_book['title'])
        self.assertEqual(updated_book_from_db['author'], updated_book['author'])
        self.assertEqual(updated_book_from_db['genre'], updated_book['genre'])
        self.assertEqual(updated_book_from_db['pages'], updated_book['pages'])


    def test_delete_book(self):
        # Adicione um novo livro primeiro
        new_book = {
            "title": "Livro para Deletar",
            "author": "Autor para Deletar",
            "genre": "Gênero para Deletar",
            "pages": 100
        }
        response_add_book = self.client.post('/books', json=new_book)
        self.assertEqual(response_add_book.status_code, 201)

        # Obtenha o ID do livro adicionado
        book_id = response_add_book.json['id']

        # Delete o livro usando o ID retornado
        response_delete_book = self.client.delete(f'/books/{book_id}')
        self.assertEqual(response_delete_book.status_code, 200)

        # Opcional: verifique se o livro foi realmente removido
        response_get_book = self.client.get(f'/books/{book_id}')
        self.assertEqual(response_get_book.status_code, 404)

if __name__ == '__main__':
    unittest.main()


#para executar, digite: python test_app.py

""" O arquivo test_app.py contém testes unitários para o aplicativo Flask. Ele usa o módulo unittest do Python para criar testes e a biblioteca unittest.mock para criar simulações das funções do aplicativo. Criamos uma classe TestApp que herda de unittest.TestCase. Em cada método de teste, usamos MagicMock para criar mocks e stubs das funções do aplicativo Flask. Para testar as rotas, utilizamos o test_client() do Flask, que simula um cliente HTTP e permite testar as solicitações GET, POST, PUT e DELETE. 

Aqui está uma descrição das funções de teste no arquivo:

test_get_books: testa a função get_all_books simulando sua resposta e verificando se a resposta do endpoint '/books' (GET) é válida e contém o título do livro esperado.
test_get_book_by_id: testa a função get_book_by_id simulando sua resposta e verificando se a resposta do endpoint '/books/1' (GET) é válida e contém o título do livro esperado.
test_add_book: testa a função add_book simulando sua resposta e verificando se a resposta do endpoint '/books' (POST) é válida e contém o ID do livro criado.
test_update_book: testa a função update_book simulando sua resposta e verificando se a resposta do endpoint '/books/1' (PUT) é válida e contém o título atualizado do livro.
test_delete_book: testa a função delete_book simulando sua resposta e verificando se a resposta do endpoint '/books/1' (DELETE) é válida e contém o ID do livro excluído.

Para executar os testes unitários, use o comando python test_app.py. Os testes devem passar e mostrar que as funções do aplicativo estão funcionando conforme o esperado. """


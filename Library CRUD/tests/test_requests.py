import requests

base_url = "http://localhost:5000"

# Testando POST para adicionar um novo livro
new_book = {"title": "Animal Farm", "author": "George Orwell", "genre": "Fiction", "pages": 112}
response = requests.post(f"{base_url}/books", json=new_book)
print("POST /books:", response.json())

# Testando GET para obter todos os livros
response = requests.get(f"{base_url}/books")
print("GET /books:", response.json())

""" # Testando GET para obter um livro específico
book_id = response.json()["id"]
response = requests.get(f"{base_url}/books/{book_id}")
print(f"GET /books/{book_id}:", response.json())

# Testando UPDATE para atualizar um livro
updated_book = {"title": "Animal Farm", "author": "George Orwell", "genre": "Political Fiction", "pages": 112}
response = requests.put(f"{base_url}/books/{book_id}", json=updated_book)
print(f"PUT /books/{book_id}:", response.json())

# Testando DELETE para remover um livro
response = requests.delete(f"{base_url}/books/{book_id}")
print(f"DELETE /books/{book_id}:", response.json())

# Testando GET novamente para verificar se o livro foi removido
response = requests.get(f"{base_url}/books")
print("GET /books (after DELETE):", response.json())

#imprime todos os livros
response = requests.get(f"{base_url}/books")
books = response.json()
for book in books:
    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Pages: {book['pages']}")
   
#deleta todos os livros
def delete_all_books():
    response = requests.delete(f"{base_url}/books")
    print("DELETE /books:", response.json())
delete_all_books()

#imprime somente uma coluna
titles = [book["title"] for book in books]
print("Book Titles:", titles)
"""

""" Este script enviará solicitações HTTP para o aplicativo Flask, testando todas as operações CRUD: GET (listar todos os livros e um livro específico), POST (adicionar um novo livro), PUT (atualizar um livro) e DELETE (remover um livro). 

Aqui estão as ações que o arquivo test_request.py executa:

Recupera todos os livros usando GET /books.
Adiciona um novo livro usando POST /books.
Recupera o livro específico que foi adicionado usando GET /books/<int:book_id>.
Atualiza o livro específico usando PUT /books/<int:book_id>.
Remove o livro específico usando DELETE /books/<int:book_id>.
Recupera todos os livros novamente usando GET /books para verificar se o livro foi removido.
Imprime todos os livros em um formato legível.
Imprime somente os títulos dos livros.
Certifique-se de que o aplicativo Flask (app.py) esteja em execução antes de executar o arquivo test_request.py. Dessa forma, as solicitações HTTP serão processadas corretamente pelo aplicativo Flask. """
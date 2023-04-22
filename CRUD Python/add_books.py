""" as funções que criamos até agora são para interagir diretamente com o banco de dados local usando SQLite. """

import sqlite3

def create_connection():
    conn = sqlite3.connect('library.db')
    return conn

def add_book(conn, title, author, genre, pages):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, genre, pages) VALUES (?, ?, ?, ?)", (title, author, genre, pages))
    conn.commit()

def check_book(conn, title):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
    book = cursor.fetchone()
    return book

def delete_book(conn, title):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE title = ?", (title,))
    conn.commit()

def main():
    conn = create_connection()

    # Exemplos de livros para adicionar ao banco de dados
    books = [
        ("To Kill a Mockingbird", "Harper Lee", "Fiction", 281),
        ("1984", "George Orwell", "Dystopian", 328),
        ("Pride and Prejudice", "Jane Austen", "Romance", 279),
        ("The Catcher in the Rye", "J.D. Salinger", "Fiction", 277),
    ]

    # Adiciona os livros ao banco de dados
    for book in books:
        add_book(conn, *book)

    # Verifica se o livro está no banco de dados
    title = "1984"
    book = check_book(conn, title)

    if book:
        print("O livro está no banco de dados:")
        print("ID:", book[0])
        print("Título:", book[1])
        print("Autor:", book[2])
        print("Gênero:", book[3])
        print("Páginas:", book[4])
    else:
        print("O livro não está no banco de dados.")


# Exclui um livro do banco de dados
    title_to_delete = "The Catcher in the Rye"
    delete_book(conn, title_to_delete)
    print(f"O livro '{title_to_delete}' foi removido do banco de dados.")


    conn.close()

if __name__ == '__main__':
    main()




#python add_books.py



""" O arquivo add_books.py também está correto. Ele define funções para interagir diretamente com o banco de dados local usando SQLite. Aqui estão as funções que você definiu:

create_connection(): cria uma conexão com o banco de dados.
add_book(conn, title, author, genre, pages): adiciona um livro ao banco de dados.
check_book(conn, title): verifica se um livro está no banco de dados.
delete_book(conn, title): remove um livro do banco de dados.
No método main(), você adiciona alguns livros de exemplo, verifica se um livro específico está no banco de dados, imprime os detalhes do livro e exclui outro livro do banco de dados.

Para executar este arquivo, use o comando python add_books.py. Ele interagirá diretamente com o banco de dados local, e não fará solicitações HTTP ao aplicativo Flask. Lembre-se de que os métodos de app.py e test_request.py são baseados em solicitações HTTP e comunicação com o servidor Flask, enquanto os métodos em add_books.py são baseados em interação direta com o banco de dados SQLite. """
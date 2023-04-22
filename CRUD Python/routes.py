from flask import request, jsonify
from app import app
import sqlite3

@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, genre, pages) VALUES (?, ?, ?, ?)", (data["title"], data["author"], data["genre"], data["pages"]))
    conn.commit()
    book_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": book_id, "message": "Book created"}), 201

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    conn.close()

    if book is None:
        return jsonify({"message": "Book not found"}), 404

    book_dict = dict(zip([column[0] for column in cursor.description], book))
    return jsonify(book_dict)

@app.route("/books", methods=["GET"])
def get_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
    conn.close()

    return jsonify(books)

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    conn = sqlite3.connect("library.db")
    cursor = conn.execute("UPDATE books SET title = ?, author = ?, genre = ?, pages = ? WHERE id = ?", (data["title"], data["author"], data["genre"], data["pages"], book_id))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"message": "Book not found"}), 404

    return jsonify({"message": "Book updated"})

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"message": "Book not found"}), 404

    return jsonify({"id": book_id, "message": "Book deleted"})

@app.route("/books", methods=["DELETE"])
def delete_all_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.execute("DELETE FROM books")
    conn.commit()
    conn.close()

    return jsonify({"message": "All books deleted"})


""" 
POST /books - Para criar um novo livro.
GET /books/<int:book_id> - Para recuperar um livro específico com base no ID do livro.
GET /books - Para recuperar todos os livros no banco de dados.
PUT /books/<int:book_id> - Para atualizar um livro específico com base no ID do livro.
DELETE /books/<int:book_id> - Para excluir um livro específico com base no ID do livro.
DELETE /books/ - Para deletar todos os livros.
"""
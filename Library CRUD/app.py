from flask import Flask
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("library.db")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT NOT NULL,
        pages INTEGER NOT NULL
    );
    """)
    conn.close()

init_db()

def get_db():
    return sqlite3.connect("library.db")

# Importa as rotas do arquivo routes.py
from routes import *

if __name__ == "__main__":
    app.run(debug=True)



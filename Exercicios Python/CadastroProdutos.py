import sqlite3

class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

class BancoDeDados:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            preco REAL NOT NULL
        );
        """)

    def inserir_produto(self, produto):
        self.cursor.execute("""
        INSERT INTO produtos (id, nome, descricao, preco) VALUES (?, ?, ?, ?)
        """, (produto.id, produto.nome, produto.descricao, produto.preco))
        self.conn.commit()

    def listar_produtos(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

    def atualizar_produto(self, produto):
        self.cursor.execute("""
        UPDATE produtos SET nome = ?, descricao = ?, preco = ? WHERE id = ?
        """, (produto.nome, produto.descricao, produto.preco, produto.id))
        self.conn.commit()

    def remover_produto(self, produto_id):
        self.cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()


# Instancie o banco de dados
db = BancoDeDados("produtos.db")

# Insira um novo produto
produto1 = Produto(1, "Camiseta", "Camiseta branca", 25.0)
db.inserir_produto(produto1)

# Liste todos os produtos
produtos = db.listar_produtos()
for produto in produtos:
    print(produto)

# Atualize um produto existente
produto1.descricao = "Camiseta branca com estampa"
produto1.preco = 30.0
db.atualizar_produto(produto1)

# Remova um produto do banco de dados
db.remover_produto(1)

# Feche a conexão com o banco de dados
db.close()

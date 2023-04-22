class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        return f'ID: {self.id}, Nome: {self.nome}, Descricao: {self.descricao}, Preco: {self.preco}'


class CadastroDeProdutos:
    def __init__(self):
        self.produtos = {}

    def inserir_produto(self, produto):
        self.produtos[produto.id] = produto

    def listar_produtos(self):
        for produto in self.produtos.values():
            print(produto)

    def atualizar_produto(self, produto):
        if produto.id in self.produtos:
            self.produtos[produto.id] = produto
        else:
            print("Produto não encontrado")

    def remover_produto(self, produto_id):
        if produto_id in self.produtos:
            del self.produtos[produto_id]
        else:
            print("Produto não encontrado")


# Exemplo de uso da classe CadastroDeProdutos
cadastro = CadastroDeProdutos()

# Inserir um produto
produto1 = Produto(1, "Camiseta", "Camiseta branca", 25.0)
cadastro.inserir_produto(produto1)

# Listar produtos
cadastro.listar_produtos()

# Atualizar produto
produto1.descricao = "Camiseta branca com estampa"
produto1.preco = 30.0
cadastro.atualizar_produto(produto1)

# Remover produto
cadastro.remover_produto(1)


#DADOS NÃO PERSISTEM E DESAPARECEM QUANDO O PROGRAMA É FECHADO, ao contrário do CadastroProdutos.py, que utiliza SQLite
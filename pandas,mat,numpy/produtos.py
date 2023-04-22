
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Dados de exemplo
dados = [['Produto A', 120], ['Produto B', 100], ['Produto C', 400]]
df = pd.DataFrame(dados, columns=['Produto', 'Vendas'])

produtos = df['Produto']
itensvendidos = df['Vendas']


mediaprecoprodutos = np.mean(itensvendidos)

plt.bar(produtos, itensvendidos)
plt.xlabel('Produtos vendidos')
plt.ylabel('Quantidade de itens vendidos por Produto')
plt.show()

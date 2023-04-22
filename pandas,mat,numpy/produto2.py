import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
dados = [['Janeiro', 'Produto A', 120], ['Fevereiro', 'Produto A', 100], ['Março', 'Produto A', 400], 
         ['Janeiro', 'Produto B', 80], ['Fevereiro', 'Produto B', 200], ['Março', 'Produto B', 300],
         ['Janeiro', 'Produto C', 150], ['Fevereiro', 'Produto C', 250], ['Março', 'Produto C', 100]]

df = pd.DataFrame(dados, columns=['Mes', 'Produto', 'Vendas'])

# Filtra apenas as vendas do Produto A
df_produto_a = df[df['Produto'] == 'Produto A']

# Agrupa as vendas por mês e calcula a soma das quantidades vendidas
vendas_por_mes = df_produto_a.groupby('Mes')['Vendas'].sum()

# Plota um gráfico de barras com as vendas por mês
meses = ['Janeiro', 'Fevereiro', 'Março']
plt.bar(meses, vendas_por_mes)
plt.xlabel('Mês')
plt.ylabel('Quantidade de itens vendidos')
plt.title('Vendas do Produto A por mês')
plt.show()
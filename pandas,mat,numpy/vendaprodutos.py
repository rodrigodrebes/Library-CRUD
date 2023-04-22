import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
dados = [['Produto A', 120], ['Produto B', 100], ['Produto C', 400]]
df = pd.DataFrame(dados, columns=['Produto', 'Vendas'])

# Cálculo da média e do desvio padrão das vendas
media_vendas = np.mean(df['Vendas'])
desvio_padrao_vendas = np.std(df['Vendas'])

print(f"Média das vendas: {media_vendas}")
print(f"Desvio padrão das vendas: {desvio_padrao_vendas}")

# Gráfico de barras com as vendas de cada produto
plt.bar(df['Produto'], df['Vendas'])
plt.xlabel('Produto')
plt.ylabel('Vendas')
plt.title('Vendas por Produto')
plt.show()
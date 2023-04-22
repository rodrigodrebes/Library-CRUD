""" Questão 1 (50 pontos): Manipulação e visualização de dados com Pandas, Numpy e Matplotlib

Suponha que você recebeu um conjunto de dados em formato CSV contendo informações sobre as vendas de produtos de uma empresa. O arquivo CSV possui as seguintes colunas: 'Data', 'Produto', 'Quantidade' e 'Preço Unitário'. Sua tarefa é analisar e visualizar esses dados usando as bibliotecas Pandas, Numpy e Matplotlib.

a) Leia o arquivo CSV e armazene os dados em um DataFrame do Pandas (10 pontos);
b) Calcule e exiba a média, mediana e desvio padrão da quantidade vendida e do preço unitário dos produtos (10 pontos);
c) Crie um gráfico de barras mostrando o total de vendas de cada produto (15 pontos);
d) Crie um gráfico de linha mostrando a evolução das vendas ao longo do tempo (15 pontos). """


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analisar_vendas(df):
    quantidade = df['Quantidade']
    data = pd.to_datetime(df['Data'])
    produto = df['Produto']
    precoUnitario = df['Preço Unitário']

    mediaqt = np.mean(quantidade)
    medianaqt = np.median(quantidade)
    desvioqt = np.std(quantidade)

    mediapc = np.mean(precoUnitario)
    medianapc = np.median(precoUnitario)
    desviopc = np.std(precoUnitario)

    print(f'Média de quantidade: {mediaqt}\n'
          f'Mediana de quantidade: {medianaqt}\n'
          f'Desvio padrão de quantidade: {desvioqt}\n'
          f'Média de preço unitário: {mediapc}\n'
          f'Mediana de preço unitário: {medianapc}\n'
          f'Desvio padrão de preço unitário: {desviopc}\n')

    plt.ylabel("Total de vendas")
    plt.xlabel("Produtos")
    plt.bar(produto, quantidade)
    plt.show()

    vendas_por_data = df.groupby('Data')['Quantidade'].sum().reset_index()
    vendas_por_data['Data'] = pd.to_datetime(vendas_por_data['Data'])

    plt.ylabel("Quantidade de vendas")
    plt.xlabel("Vendas ao longo do tempo")
    plt.plot(vendas_por_data['Data'], vendas_por_data['Quantidade'])
    plt.show()

# Exemplo de DataFrame fictício
data = {'Produto': ['A', 'B', 'C', 'A', 'B', 'C'],
        'Quantidade': [10, 15, 12, 8, 20, 18],
        'Data': ['2023-04-01', '2023-04-01', '2023-04-01', '2023-04-02', '2023-04-02', '2023-04-02'],
        'Preço Unitário': [100, 150, 120, 100, 150, 120]}

df_teste = pd.DataFrame(data)
analisar_vendas(df_teste)


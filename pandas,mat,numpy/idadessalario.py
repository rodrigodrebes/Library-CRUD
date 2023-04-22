import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leitura e manipulação dos dados
#dados = pd.read_csv('arquivo.csv')

# Listas de idades e salários adicionais
idades_adicionais = [35, 40, 42, 28, 50]
salarios_adicionais = [50000, 55000, 60000, 45000, 70000]

# Adicionando novas idades e salários ao DataFrame
dados = pd.DataFrame({'coluna 1': idades_adicionais, 'coluna 2': salarios_adicionais})


# Extraindo colunas de idade e salário
idade = dados['coluna 1']
salario = dados['coluna 2']

# Cálculo da média e desvio padrão utilizando NumPy
media_idade = np.mean(idade)
media_salario = np.mean(salario)
desvio_padrao_idade = np.std(idade)
desvio_padrao_salario = np.std(salario)

# Informações de médias e desvios padrões
info_media = f'Média Salário: {media_salario:.2f} | Média Idade: {media_idade:.2f}'
info_desvio_padrao = f'Desvio Padrão Salário: {desvio_padrao_salario:.2f} | Desvio Padrão Idade: {desvio_padrao_idade:.2f}'

# Criação do gráfico de dispersão
plt.scatter(salario, idade)
plt.xlabel('Salário')
plt.ylabel('Idade')

# Adiciona as informações das médias e desvios padrões ao gráfico
plt.title(f'{info_media}\n{info_desvio_padrao}')

# Exibir o gráfico
plt.show()


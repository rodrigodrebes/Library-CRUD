import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
salarios_profissao1 = [2000, 2500, 3000, 3500, 4000]
salarios_profissao2 = [2500, 3000, 3500, 4000, 4500]

# Cria DataFrame para cada profissão
df_profissao1 = pd.DataFrame(salarios_profissao1, columns=['Salário'])
df_profissao2 = pd.DataFrame(salarios_profissao2, columns=['Salário'])

# Calcula as medidas estatísticas para cada profissão
media1 = np.mean(df_profissao1['Salário'])
mediana1 = np.median(df_profissao1['Salário'])
std1 = np.std(df_profissao1['Salário'])

media2 = np.mean(df_profissao2['Salário'])
mediana2 = np.median(df_profissao2['Salário'])
std2 = np.std(df_profissao2['Salário'])

# Plota um gráfico de barras para comparar os salários médios de cada profissão
salarios_medios = [media1, media2]
profissoes = ['Profissão 1', 'Profissão 2']

plt.bar(profissoes, salarios_medios)
plt.ylabel('Salário médio')
plt.title('Comparação de salários entre duas profissões')
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
data = {'Aluno': ['Ana', 'Bruno', 'Carla', 'David', 'Eva'],
        'Nota': [80, 90, 75, 85, 95]}

df = pd.DataFrame(data)

# Cálculo da média e mediana das notas
media_notas = np.mean(df['Nota'])
mediana_notas = np.median(df['Nota'])

print(f"Média das notas: {round(media_notas, 2)}")
print(f"Mediana das notas: {mediana_notas}")

# Gráfico de barras com as notas de cada aluno
plt.bar(df['Aluno'], df['Nota'])
plt.xlabel('Aluno')
plt.ylabel('Nota')
plt.title('Notas por Aluno')
plt.show()

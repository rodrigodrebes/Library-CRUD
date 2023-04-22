import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

# Carregando os dados
dados = pd.DataFrame({'idade': [20, 30, 40, 50, 60, 70],
                      'salario': [2000, 5000, 6000, 8000, 9000, 12000]})

# Separando as variáveis independentes e dependentes
X = dados["idade"].values.reshape(-1, 1)
y = dados["salario"]

# Dividindo os dados em conjuntos de treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando o modelo de regressão linear
modelo = LinearRegression()

# Treinando o modelo
modelo.fit(X_treino, y_treino)

# Visualizando a reta de regressão
plt.plot(X, y, color="blue")

# Criando um conjunto de pontos de idade que cobre todo o intervalo de idades
idades_completas = np.linspace(X.min(), X.max(), num=300).reshape(-1, 1)

# Prevendo os salários para todas as idades
salarios_previstos = modelo.predict(idades_completas)

# Plotando a linha de regressão
plt.plot(idades_completas, salarios_previstos, color="red", linewidth=2)
plt.xlabel("Idade")
plt.ylabel("Salário")
plt.show()
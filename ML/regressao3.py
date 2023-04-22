import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Dados fictícios de área e preço de casas
data = {
    "area": [50, 70, 80, 100, 120, 150, 200],
    "preco": [100000, 150000, 180000, 240000, 300000, 350000, 420000],
}

# Carregando os dados
dados = pd.DataFrame(data)

# Separando as variáveis independentes e dependentes
X = dados["area"].values.reshape(-1, 1)
y = dados["preco"]

# Dividindo os dados em conjuntos de treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando o modelo de regressão linear
modelo = LinearRegression()

# Treinando o modelo
modelo.fit(X_treino, y_treino)

# Prevendo os preços com base no conjunto de teste
y_pred = modelo.predict(X_teste)

# Avaliando o modelo
mse = mean_squared_error(y_teste, y_pred)
r2 = r2_score(y_teste, y_pred)

print("MSE: ", mse)
print("R2: ", r2)

# Visualizando a reta de regressão
plt.scatter(X, y, color="blue")

# Criando um conjunto de pontos de área que cobre todo o intervalo de áreas
areas_completas = np.linspace(X.min(), X.max(), num=300).reshape(-1, 1)

# Prevendo os preços para todas as áreas
precos_previstos = modelo.predict(areas_completas)

# Plotando a linha de regressão
plt.plot(areas_completas, precos_previstos, color="red", linewidth=2)
plt.xlabel("Área (m²)")
plt.ylabel("Preço")
plt.show()
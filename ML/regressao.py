#Nesse código, a linha de regressão só está atingindo o conjunto de testes

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

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

# Prevendo os salários com base no conjunto de teste
y_pred = modelo.predict(X_teste)

# Avaliando o modelo
mse = mean_squared_error(y_teste, y_pred)
r2 = r2_score(y_teste, y_pred)

print("MSE: ", mse)
print("R2: ", r2)

# Visualizando a reta de regressão
plt.scatter(X, y, color="blue")
plt.plot(X_teste, y_pred, color="red", linewidth=2)
plt.xlabel("Idade")
plt.ylabel("Salário")
plt.show()

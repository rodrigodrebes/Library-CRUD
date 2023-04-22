import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Exemplo de dados
horas_estudadas = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
notas = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Redimensionando os dados
X = horas_estudadas.reshape(-1, 1)
y = notas.reshape(-1, 1)

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Previsão
y_pred = modelo.predict(X_test)

# Plotando os dados e a reta de regressão
plt.scatter(X_test, y_test, label='Dados de Teste')
plt.plot(X_test, y_pred, color='red', label='Reta de Regressão')
plt.xlabel('Horas Estudadas')
plt.ylabel('Notas')
plt.legend()
plt.show()
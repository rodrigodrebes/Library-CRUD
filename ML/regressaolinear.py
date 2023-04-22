from sklearn import datasets
from sklearn.model_selection import train_test_split #Faz o split de dados
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from sklearn.metrics import accuracy_score

diabetes = datasets.load_diabetes()

X=diabetes.data
y=diabetes.target

#dados de teste e dados target
X_train, X_test, y_train, y_test = train_test_split (X,y,test_size=0.2)

#printa a dimensão dos dados, para vermos o tamanho
print(diabetes.feature_names)
print("X")
print(X.shape)
print("y")
print(y.shape)

#define-se o modelo de regressão
modelo = linear_model.LinearRegression()

#constroi-se o modelo
modelo.fit(X_train, y_train)

predicao = modelo.predict(X_test)

print(f"coeficientes {modelo.coef_}")
print(f"intercept {modelo.intercept_}")
print('Erro quadrático médio: %.2f' % mean_squared_error(y_test, predicao))

#plota o gráfico
plt.scatter(y_test, predicao)
plt.plot([0, 350], [0, 350], linestyle='--', color='red')
plt.xlabel('Valores reais')
plt.ylabel('Valores previstos')
plt.show()
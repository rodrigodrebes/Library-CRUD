from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import svm
import pandas as pd
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
classes = ['Iris Setosa', 'Iris Versicolour', 'Iris Virginica']

X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split (X,y,test_size=0.2)

modelo = svm.SVC()
modelo.fit(X_train, y_train)

predicao = modelo.predict(X_test)
acuracia = accuracy_score(y_test, predicao)

print(f"predição: {predicao}")
print(f"valor real: {y_test}")
print(f"acuracia: {acuracia}")

for i in range(len(predicao)):
    print(classes[predicao[i]])
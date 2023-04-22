
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import neighbors, metrics
import pandas as pd
from sklearn.preprocessing import LabelEncoder

dados = pd.read_csv('python\ML\car.data')

X = dados[['buying', 'maint', 'safety']].values
y= dados[['class']]

#print(X,y)

#conversão de dados para números
Le = LabelEncoder()
for i in range(len(X[0])):
    X[:, i] = Le.fit_transform(X[:, i])
#print(X)

#transforma as colunas em valores
label_maping = {'unacc': 0, 'acc': 1, 'good':2, 'vgood': 3}
y['class']= y['class'].map(label_maping)
y = np.array(y)
print(y)

#define o K e o peso
knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights='uniform')

#TREINA o modelo
#20% (0.2) dos nossos dados servirão de teste
X_train, X_test, y_train, y_test = train_test_split (X,y,test_size=0.2)
knn.fit(X_train, y_train)

prediction = knn.predict(X_test)

accuracy = metrics.accuracy_score(y_test, prediction)

print(f"predição: {prediction}")
print(f"acurácia: {accuracy}")

print(f"valor real: {y[20]}")
print(f"valor predito: {knn.predict(X)[20]}")



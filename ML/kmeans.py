from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import scale
import pandas as pd

bc = load_breast_cancer()
print(bc)

X=scale(bc.data)
y=bc.target

#dados de teste e dados target
X_train, X_test, y_train, y_test = train_test_split (X,y,test_size=0.2)

modelo = KMeans(n_clusters=2, random_state=0)

modelo.fit(X_train)

predicao = modelo.predict(X_test)

labels = modelo.labels_

acuracia = accuracy_score(y_test, predicao)

print(f"labels {labels}")
print(f"predição {predicao}")

print(f"valor atual {y_test}")
print(f"acurácia {acuracia}")





import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# reduzindo a dimensionalidade dos dados para duas dimensões
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# plotando os pontos com as cores indicando a classe verdadeira dos dados
plt.scatter(X_reduced[:,0], X_reduced[:,1], c=y, cmap='viridis')
plt.title('Dados do Breast Cancer Wisconsin')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')

# adicionando a legenda das classes
handles, labels = plt.gca().get_legend_handles_labels()
unique_labels = set(labels)
colors = plt.cm.viridis.colors[:len(unique_labels)]
plt.legend(handles, unique_labels, loc='best', bbox_to_anchor=(1, 0.5),
           title='Classes', labels=unique_labels)
           
plt.show()
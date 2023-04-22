import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.datasets import make_blobs

# Criação de um conjunto de dados fictício com 3 clusters
np.random.seed(42)
X, y = make_blobs(n_samples=300, centers=3, random_state=42)

# Aplicando o PCA para reduzir a dimensionalidade dos dados
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Aplicando o K-Means com diferentes números de clusters
clusters = n_clusters=3
kmeans = KMeans(clusters, random_state=42)
kmeans.fit(X_pca)

 # Visualização dos resultados
plt.figure()
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X', label='Centroides')
plt.title(f'K-Means com {clusters}')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend()
plt.show()

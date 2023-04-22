import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Exemplo de dados
pontos = np.array([[1, 2], [2, 3], [3, 4],
                   [10, 11], [11, 12], [12, 13],
                   [20, 21], [21, 22], [22, 23],
                   [2, 8], [3, 9], [4, 10]])

# Criando o modelo K-Means e ajustando aos dados
modelo = KMeans(n_clusters=4, random_state=42)
modelo.fit(pontos)

# Previsão dos clusters
clusters = modelo.predict(pontos)

# Plotando os pontos e seus respectivos clusters
plt.scatter(pontos[:, 0], pontos[:, 1], c=clusters, cmap='viridis')

# Plotando os centróides
plt.scatter(modelo.cluster_centers_[:, 0], modelo.cluster_centers_[:, 1], c='red', marker='X', label='Centroides')

plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('K-Means Clustering')
plt.legend()
plt.show()

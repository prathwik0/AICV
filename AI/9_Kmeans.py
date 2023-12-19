import numpy as np
from sklearn.cluster import KMeans

np.random.seed(0)
X = np.random.rand(100, 2)

k = 3
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)

cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_

import matplotlib.pyplot as plt
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', s=200, color='red')
plt.title(f'K-Means Clustering (k={k})')
plt.show()

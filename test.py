import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Create synthetic data
X, _ = make_blobs(n_samples=300, centers=5, random_state=42)

# Calculate WCSS for different k values
wcss = []
k_values = range(1, 15)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)  # Fit the model
    wcss.append(kmeans.inertia_)  # WCSS is stored in inertia_

# Plot WCSS against k
plt.plot(k_values, wcss, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.title('Elbow Method for Optimal k')
plt.show()

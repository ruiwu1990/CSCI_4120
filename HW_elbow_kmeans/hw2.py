from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

from sklearn.datasets.samples_generator import make_blobs

X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)


# TODO determine the best k for k-means
# TODO calculate accuracy for best K
# TODO draw a confusion matrix
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# generate Dataset
X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    class_sep=5.0,
    random_state=42
)

# Plot
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Linear separierbarer Datensatz")
plt.show()

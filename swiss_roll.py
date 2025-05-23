from sklearn.datasets import make_swiss_roll
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate 3D Swiss roll with p points
p = 1000
X, t = make_swiss_roll(n_samples=p, noise=0.0, random_state=42)

# X has shape (p, 3), representing 3D coordinates
print("Shape of Swiss roll data:", X.shape)  # Should be (1000, 3)

# Optional: visualize the 3D Swiss roll
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=t, cmap=plt.cm.viridis, s=10)
ax.set_title("3D Swiss Roll")
plt.show()

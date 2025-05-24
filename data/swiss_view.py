import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the data from the .txt file
data = np.loadtxt("swiss_roll_labeled.txt")
X = data[:, :3]       # x, y, z coordinates
labels = data[:, 3]   # 1 or -1

# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot external points (label = 1) in red
ax.scatter(X[labels == 1, 0], X[labels == 1, 1], X[labels == 1, 2],
           c='red', label='External (1)', s=10, alpha=0.6)

# Plot interior points (label = -1) in blue
ax.scatter(X[labels == -1, 0], X[labels == -1, 1], X[labels == -1, 2],
           c='blue', label='Interior (-1)', s=10, alpha=0.6)

# Labels and legend
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Labeled Swiss Roll")
ax.legend()

plt.tight_layout()
plt.show()

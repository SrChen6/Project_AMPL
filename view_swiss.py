import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401, needed for 3D plots

# Load the data from the text file
data = np.loadtxt("swiss_roll_labeled.txt")

# Separate features and labels
X = data[:, :3]
y = data[:, 3]

# Create a 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the center points (+1) in green, external points (-1) in red
ax.scatter(X[y == 1, 0], X[y == 1, 1], X[y == 1, 2], c='green', label='Center (+1)', s=10)
ax.scatter(X[y == -1, 0], X[y == -1, 1], X[y == -1, 2], c='red', label='External (-1)', s=10)

ax.set_title("Swiss Roll with Labeled Categories")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
plt.tight_layout()
plt.show()
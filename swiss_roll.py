from sklearn.datasets import make_swiss_roll
import numpy as np
import matplotlib.pyplot as plt

# Generate Swiss roll data
p = 500
X, t = make_swiss_roll(n_samples=p, noise=0.0, random_state=42)

# Normalize t to find center/external threshold
t_mean = np.mean(t)
t_std = np.std(t)

# Assign labels based on distance from mean
# +1: points near center (within 1 std), -1: outer
y = np.where(np.abs(t - t_mean) < t_std, 1, -1)

# Combine X and y
data = np.hstack((X, y.reshape(-1, 1)))

# Save to txt file
np.savetxt("swiss_roll_labeled.txt", data, fmt="%.5f %.5f %.5f %d")
print("Data written to 'swiss_roll_labeled.txt'")

# Optional: visualize the 3D Swiss roll
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=t, cmap=plt.cm.viridis, s=10)
ax.set_title("3D Swiss Roll")
plt.show()
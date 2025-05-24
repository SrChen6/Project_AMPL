import numpy as np
from sklearn.datasets import make_swiss_roll

# Generate Swiss roll data
n_samples = 2000
X, t = make_swiss_roll(n_samples=n_samples, noise=0.0)

# Define the threshold to separate "external" and "interior"
# The 't' variable from make_swiss_roll is the unrolled distance, which spirals from low (inner) to high (outer)
threshold = np.percentile(t, 65)  # top 35% as "external", rest as "interior"
labels = np.where(t > threshold, 1, -1)

# Combine into a single array: x, y, z, label
data = np.hstack((X, labels.reshape(-1, 1)))

# Save to .txt
np.savetxt("swiss_roll_labeled.txt", data, fmt="%.5f %.5f %.5f %d")

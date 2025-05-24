import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report

# Load the data from file (assuming 4 columns: x, y, z, label)
data = np.loadtxt("swiss_roll_labeled.txt")
X = data[:, :3]       # Features: 3D coordinates
y = data[:, 3]        # Labels: 1 or -1

# Optional: split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define parameter grid
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': [0.001, 0.01, 0.1, 1],
    'kernel': ['rbf']
}

# Create the SVM model
svm = SVC()

# Perform grid search with 5-fold cross-validation
grid = GridSearchCV(svm, param_grid, cv=5, scoring='accuracy', verbose=1)
grid.fit(X_train, y_train)

# Print best parameters and performance
print("Best parameters found:", grid.best_params_)
print("Best cross-validation accuracy:", grid.best_score_)

# Evaluate on the test set
y_pred = grid.best_estimator_.predict(X_test)
print("\nTest set performance:")
print(classification_report(y_test, y_pred))

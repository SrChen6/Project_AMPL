set N;                    # Features (1..N)
set M;                    # Samples (1..M)

param nu > 0;             # Regularization parameter
param y{M};        # Class labels (1 or -1)
param X{M, N};            # Feature matrix


var w{N};                 # Weights
var gamma;                # Bias
var s{M} >= 0;            # Slack 


minimize Obj:
    0.5 * sum{j in N} w[j]^2 + nu * sum{i in M} s[i];


s.t. Margin_Constraints{i in M}:
    y[i] * (sum{j in N} w[j] * X[i, j] + gamma) + s[i] >= 1;


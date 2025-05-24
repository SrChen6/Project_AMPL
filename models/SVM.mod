param N;                    # Features
param M;                    # Samples 

param nu > 0;             # Regularization parameter
param y{1..M};        # Class labels (1 or -1)
param X{1..M, 1..N};            # Feature matrix



var w{1..N};                 # Weights
var gamma;                # Bias
var s{1..M} >= 0;            # Slack 


minimize Obj:
    0.5 * sum{j in 1..N} w[j]^2 + nu * sum{i in 1..M} s[i];


s.t. Margin_Constraints{i in 1..M}:
    y[i] * (sum{j in 1..N} w[j] * X[i, j] + gamma) + s[i] >= 1;


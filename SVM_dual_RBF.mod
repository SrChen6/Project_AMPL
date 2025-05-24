param N;                    # Features
param M;                    # Samples 

param nu > 0;             # Regularization parameter
param y{1..M};        # Class labels (1 or -1)
param X{1..M, 1..N};            # Feature matrix
param sigma;
param K{i in 1..M, k in 1..M} := exp(- sum{j in 1..N} (X[i,j] - X[k,j])^2/(2 * sigma^2)); # Gaussian kernel
param w{1..4};
param gamma;


var la{1..M} >= 0, <= nu;


maximize Obj:
	sum{i in 1..M} la[i] - 0.5 * (sum{i in 1..M, j in 1..M} la[i]*y[i]*la[j]*y[j]*K[i,j]);

s.t. Constrain:
	sum{i in 1..M} la[i]*y[i] =0;
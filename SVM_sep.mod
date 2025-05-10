set OBS;

param x {OBS};
param y {OBS};

param nu;   # regulation

var w {OBS};
var gamma;
var s {OBS} >= 0;

minimize fobj: 1/2*sum {j in OBS} w[j]**2 + nu*sum {i in OBS} s[i];

subject to margain:
	y[i]*(sum {j in OBS} w[j]*x[j] + gamma) + sum {i in OBS} s[i] >= 1;
	
 




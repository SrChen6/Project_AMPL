#parameters
param ca > 0;
param cb > 0;
param ta > 0;
param tb > 0;
param ua > 0;
param ub > 0;

#variables
var xa >=0, <= ua;
var xb >=0, <= ub;

#objective function
maximize fobj : ca*xa+cb*xb;
#constraints
subject to c1 : ta*xa + tb*xb <= 40;

# Per executar: a la consola model transp_wo_sets.mod
# data transp_wo_sets.dat
# 
# option solver cplex
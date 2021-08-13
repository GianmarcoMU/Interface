import numpy as np
from numpy.lib.function_base import percentile

# Firstly, we define the variables needed to implement the lattice discretization
steps = 2
T = 1
S = 10
K = 10
delta_time = T/steps
sigma = 0.3
rate = 0.1
u = np.exp(sigma*np.sqrt(delta_time))
d = 1/u
q_rn = (1/(u-d))*(np.exp(rate*delta_time)-d)
qq = 1-q_rn
dis = 1/(1+rate)

row = steps+1
col = steps+1

# We initialize an empty matrix that will be populated recursively

lattice = np.zeros((row, col))
payoff = np.zeros((row, col))
price = np.zeros((row, col))
lattice[0, 0] = S

for i in range(1, row, 1):
    for j in range(1, col, 1):
        lattice[0, j] = S*(u**j)
        lattice[i, j] = lattice[i-1, j-1]*d

for i in range(0, row, 1):
    for j in range(0, col, 1):
        if lattice[i, j] == 0:
            payoff[i, j] = 0
        else:
            payoff[i, j] = max(K-lattice[i, j], 0)

for i in range(row-1, -1, -1):
    for j in range(col-1, -1, -1):
        if lattice[i, j] ==0:
            price[i, j] = 0
        else:
            if j == col-1:
                price[i, j] = payoff[i, j]
            else:
                price[i, j] = max(payoff[i, j], dis*(q_rn*price[i, j+1]+qq*price[i+1, j+1]))
                    
print(price)

lattice = np.zeros((row, col))
payoff = np.zeros((row, col))
price = np.zeros((row, col))
lattice[0, 0] = S

for i in range(1, row, 1):
    for j in range(1, col, 1):
        lattice[0, j] = S*(u**j)
        lattice[i, j] = lattice[i-1, j-1]*d

for i in range(0, row, 1):
    for j in range(0, col, 1):
        if lattice[i, j] == 0:
            payoff[i, j] = 0
        else:
            payoff[i, j] = max(K-lattice[i, j], 0)

for i in range(row-1, -1, -1):
    for j in range(col-1, -1, -1):
        if lattice[i, j] == 0:
            price[i, j] = 0
        else:
            if j == col-1:
                price[i, j] = payoff[i, j]
            else:
                price[i, j] = max(payoff[i, j], dis*(q_rn*price[i, j+1]+qq*price[i+1, j+1]))
c0 = price[0, 0]

print(c0)


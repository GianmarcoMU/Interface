import tkinter as ttk
from tkinter import *
import scipy as sp
from scipy import stats
from scipy.stats import norm
import numpy as np

# Firstly, we define the variables needed to implement the lattice discretization
steps = 500
#delta_time = T/steps
#u = np.exp(sigma*np.sqrt(delta_time))
#d = 1/u
#q = (1/(u-d))*(np.exp(r*delta_time)-d)

S = 10
K = 10
u = 1.2
d = 0.8
q = 0.75
rate = 0.1

row = 3
col = 3

# We initialize an empty matrix that will be populated recursively
lattice_S = np.zeros((row, col))
value_process = np.zeros((row, col))
CV_process = np.zeros((row, col))
lattice_S[0, 0] = S

for i in range(1, row, 1):
    for j in range(1, col, 1):
        lattice_S[0, j] = S*(u**j)
        lattice_S[i, j] = lattice_S[i-1, j-1]*d

for r in range(0, row, 1):
    for c in range(0, col, 1):
        value_process[r, c] = max(K-lattice_S[r, c], 0)

# Check this process, something goes wrong
for r in range(row-1, -1, -1):
    for c in range(col-1, -1, -1):
        CV_process[r-1, c-1] = (1/(1+rate))*(q*value_process[r, c+1]+(0.25)*value_process[r+1,c+1])
        
    
print(lattice_S)
print(value_process)
print(CV_process)


import tkinter as ttk
from tkinter import *
import scipy as sp
from scipy import stats
from scipy.stats import norm
import numpy as np

# We try to create two functions that use Entry and Checkbutton widgets in tkinter. 
# This is just a useless example to retrieve the values that the user has inserted in the Entries and Checkbuttons
# widgets introduced in the interface. In particular, for the Checkbutton we need to specify a boolean value that takes vlaue 1 if the cell is checked
# and 0 otherwise. For the Entry widget it is simpler but it is important to pay attention to some details. 

# The model implemented below is Black-Scholes for plain vanilla European derivatives.

root = ttk.Tk()

st_price = ttk.Entry()
str_price = ttk.Entry()
mat = ttk.Entry()
vol = ttk.Entry()
rate = ttk.Entry()
div = ttk.Entry()

var1 = ttk.BooleanVar()
var1.set(FALSE)

put = ttk.Checkbutton(text = "PUT", variable = var1)
put.grid(row = 9, column = 0)

st_price.grid(row = 0, column = 0)
str_price.grid(row = 1, column = 0)
mat.grid(row = 2, column = 0)
vol.grid(row = 3, column = 0)
rate.grid(row = 4, column = 0)
div.grid(row = 5, column = 0)

def prova():
    S = float(st_price.get())
    K = float(str_price.get())
    T = float(mat.get())
    sigma = float(vol.get())
    r = float(rate.get())
    q = float(div.get())

    d1 = (np.log(S/K)+(r-q+(sigma**2)/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - (sigma*(np.sqrt(T)))

    if var1.get() == FALSE:
        N_d1 = norm.cdf(d1)
        N_d2 = norm.cdf(d2)
        c0 = (S*np.exp(-q*T)*N_d1)-(K*np.exp(-r*T)*N_d2)
    else:
        N_d1 = norm.cdf(-d1)
        N_d2 = norm.cdf(-d2)
        c0 = (K*np.exp(-r*T)*N_d2)-(S*np.exp(-q*T)*N_d1)

    res = ttk.Entry()
    res.insert(0, str(c0))
    res.grid(row = 7, column = 0, pady = 5)

def check():
    print_put = ttk.Entry()
    if var1.get() == TRUE:
        print_put.insert(0, "You choose PUT")
    else:
        print_put.insert(0, "You choose a CALL")
    print_put.grid(row = 10, column = 0)

calcola = ttk.Button(text = "CALCOLA", command = prova)
calcola.grid(row = 6, column = 0)

controlla = ttk.Button(text = "CHECK", command = check).grid(row = 8, column = 0)

root.mainloop()

### Here we try to create an interface starting from the original documentation about tkinter

# Firstly, import the required library. Namely, tkinter
import tkinter as ttk
from tkinter import font, mainloop
import tkinter as ttk
from tkinter import *
import scipy as sp
from scipy import stats
from scipy.stats import norm
import numpy as np
from tkinter import messagebox

# Following the underlying hierarchist approach of tkinter, create the main building block: root
root = ttk.Tk()

# Start adding some features to it
root.title("Option Calculator")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight = 1)

# Create the second-level objects, called frames, to organise better the interface
# See the pdf file to understand the graphical structure
mainframe = ttk.Frame(root) 
frame1 = ttk.Frame(mainframe, borderwidth = 5, relief = 'groove')
frame2 = ttk.Frame(mainframe, borderwidth = 5, relief = "groove")
frame3 = ttk.Frame(mainframe, borderwidth = 5, relief = "groove")
frame4 = ttk.Frame(mainframe, borderwidth = 5, relief = "groove")

# Create a Welcome text in the first frame to explain the functionalities of the application
welcome = ttk.Label(frame1, text = "Welcome to the Option Calculator! This application has been developed to compute the theoretical price of option\
derivatives using different methods \nfor given various inputs. Before using it make sure to use the british\
notation (dot) for decimals and specify the dates in the following format.").grid(row = 0, columnspan = 4, sticky = "W")

# Create some labels and buttons for the inputs
opt_type = ttk.Label(frame2, text = "Option Type:", font = ('Helvetica', 10, 'bold')).grid(row = 0, column = 0, sticky = "W", padx = 5, pady = 5)
ex_style = ttk.Label(frame2, text = "Exercise Style:", font = ('Helvetica', 10, 'bold')).grid(row = 1, column = 0, sticky = "W", padx = 5, pady = 5)
meth = ttk.Label(frame2, text = "Methodology:", font = ('Helvetica', 10, 'bold')).grid(row = 2, column = 0, sticky = "W", padx = 5, pady = 5)
str_pr_l = ttk.Label(frame2, text = "Strike Price", font = ('Helvetica', 10, 'bold')).grid(row = 3, column = 0, sticky = "W", padx = 5, pady = 5)
st_pr_l = ttk.Label(frame2, text = "Stock Price", font = ('Helvetica', 10, 'bold')).grid(row = 3, column = 2, sticky = "W", padx = 5, pady = 5)
maturity_l = ttk.Label(frame2, text = "Maturity", font = ('Helvetica', 10, 'bold')).grid(row = 4, column = 0, sticky = "W", padx = 5, pady = 5)
vol_l = ttk.Label(frame2, text = "Volatility", font = ('Helvetica', 10, 'bold')).grid(row = 4, column = 2, sticky = "W", padx = 5, pady = 5)
rate_l = ttk.Label(frame2, text = "Interest Rate", font = ('Helvetica', 10, 'bold')).grid(row = 5, column = 0, sticky = "W", padx = 5, pady = 5)
div_l = ttk.Label(frame2, text = "Dividend Yield", font = ('Helvetica', 10, 'bold')).grid(row = 5, column = 2, sticky = "W", padx = 5, pady = 5)

# We create this auxiliary variable to be able to retrieve if the user has selected PUT or CALL
put_check = ttk.BooleanVar()
put_check.set(FALSE)
call_check = ttk.BooleanVar()
call_check.set(FALSE)
american_check = ttk.BooleanVar()
american_check.set(FALSE)
european_check = ttk.BooleanVar()
european_check.set(FALSE)

put = ttk.Checkbutton(frame2, text = "Put",variable = put_check)
call = ttk.Checkbutton(frame2, text = "Call", variable = call_check)
american = ttk.Checkbutton(frame2, text = "American", variable = american_check)
european = ttk.Checkbutton(frame2, text = "European", variable = european_check)
bs = ttk.Checkbutton(frame2, text = "Black-Scholes").grid(row = 2, column = 1, sticky = "W")
bin = ttk.Checkbutton(frame2, text = "Binomial Tree").grid(row = 2, column = 2, sticky = "W")
jdm = ttk.Checkbutton(frame2, text = "Jump Diffusion").grid(row = 2, column = 3, sticky = "W")

put.grid(row = 0, column = 1, sticky = "W")
call.grid(row = 0, column = 2, sticky = "W")
american.grid(row = 1, column = 1, sticky = "W")
european.grid(row = 1, column = 2, sticky = "W")

str_pr = ttk.Entry(frame2)
st_pr = ttk.Entry(frame2)
maturity = ttk.Entry(frame2)
vol = ttk.Entry(frame2)
rate = ttk.Entry(frame2)
div = ttk.Entry(frame2)

str_pr.grid(row = 3, column = 1)
st_pr.grid(row = 3, column = 3)
maturity.grid(row = 4, column = 1)
vol.grid(row = 4, column = 3)
rate.grid(row = 5, column = 1)
div.grid(row = 5, column = 3)

# We now define a first function for the Black-Scholes model
def BS():
    S = float(st_pr.get())
    K = float(str_pr.get())
    T = float(maturity.get())
    sigma = float(vol.get())
    r = float(rate.get())
    q = float(div.get())

    d1 = (np.log(S/K)+(r-q+(sigma**2)/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - (sigma*(np.sqrt(T)))

    if put_check.get() == FALSE and call_check.get() == TRUE and european_check.get() == TRUE:
        N_d1 = norm.cdf(d1)
        N_d2 = norm.cdf(d2)
        c0 = (S*np.exp(-q*T)*N_d1)-(K*np.exp(-r*T)*N_d2)
        D = np.exp(-q*T)*N_d1
        V = K*np.exp(-r*T)*np.sqrt(T)*np.exp((-d2**2)/2)/(100*np.sqrt(2*np.pi))
        R = T*K*np.exp(-r*T)*N_d2/100
        TH = ((q*S*np.exp(-q*T)*N_d1) - (r*K*np.exp(-r*T)*N_d2) - (((sigma/np.sqrt(T*8*np.pi))*K*np.exp(-r*T)*np.exp((-d2**2)/2))))/365
        G = (1/(sigma*S*np.sqrt(T)))*np.exp(-q*T)*np.exp((-d1**2)/2)/np.sqrt(2*np.pi)

    elif put_check.get() == TRUE and call_check.get() == FALSE and european_check.get() == TRUE:
        N_d1 = norm.cdf(-d1)
        N_d2 = norm.cdf(-d2)
        c0 = (K*np.exp(-r*T)*N_d2)-(S*np.exp(-q*T)*N_d1)
        D = -np.exp(-q*T)*N_d1
        V = K*np.exp(-r*T)*np.sqrt(T)*np.exp((-d2**2)/2)/(100*np.sqrt(2*np.pi))
        R = -T*K*np.exp(-r*T)*N_d2/100
        TH = (-(q*S*np.exp(-q*T)*N_d1) + (r*K*np.exp(-r*T)*N_d2) - (((sigma/np.sqrt(T*8*np.pi))*K*np.exp(-r*T)*np.exp((-d2**2)/2))))/365
        G = (1/(sigma*S*np.sqrt(T)))*np.exp(-q*T)*np.exp((-d1**2)/2)/np.sqrt(2*np.pi)

    else:
        messagebox.showerror("ERROR", "Check that you have correctly specify both Option Type and Exercise Style. Note that Black and Scholes Model can only be used with European Options.")


    th_price.delete(0, len(str(th_price.get())))
    delta.delete(0, len(str(delta.get())))
    vega.delete(0, len(str(vega.get())))
    rho.delete(0, len(str(rho.get())))
    theta.delete(0, len(str(theta.get())))
    gamma.delete(0, len(str(gamma.get())))
    th_price.insert(0, str(c0))
    delta.insert(0, str(D))
    vega.insert(0, str(V))
    rho.insert(0, str(R))
    theta.insert(0,str(TH))
    gamma.insert(0,str(G))

# The following function is the one associated to Reset button, to clear everything
def cancel():
    str_pr.delete(0, len(str(str_pr.get())))
    st_pr.delete(0, len(str(st_pr.get())))
    maturity.delete(0, len(str(maturity.get())))
    div.delete(0, len(str(div.get())))
    th_price.delete(0, len(str(th_price.get())))
    rate.delete(0, len(str(rate.get())))
    vol.delete(0, len(str(vol.get())))
    delta.delete(0, len(str(delta.get())))
    vega.delete(0, len(str(vega.get())))
    rho.delete(0, len(str(rho.get())))
    theta.delete(0, len(str(theta.get())))
    gamma.delete(0, len(str(gamma.get())))
    put.deselect()
    call.deselect()
    american.deselect()
    european.deselect()  

# Create two buttons that calculate outputs and reset inputs
calc = ttk.Button(frame3, text = "CALCULATE",command = BS).grid(row = 0, column = 0, padx = 160, pady = 5)
reset = ttk.Button(frame3, text = "RESET", command = cancel).grid(row = 1, column = 0)
plot = ttk.Button(frame3, text = "PLOT").grid(row = 2, column = 0, pady = 5)

# Define outputs: both labels and entries
th_price_l = ttk.Label(frame4, text = "Theoretical Price").grid(row = 0, column = 0, sticky = "W", pady = 5)
delta_l = ttk.Label(frame4, text = "Delta").grid(row = 0, column = 2, sticky = "W")
rho_l = ttk.Label(frame4, text = "Rho").grid(row = 1, column = 0, sticky = "W", pady = 5)
gamma_l = ttk.Label(frame4, text = "Gamma").grid(row = 1, column = 2, sticky = "W", pady = 5)
theta_l = ttk.Label(frame4, text = "Theta").grid(row = 2, column = 0, sticky = "W")
vega_l = ttk.Label(frame4, text = "Vega").grid(row = 2, column = 2, sticky = "W", pady = 5)

th_price = ttk.Entry(frame4)
delta = ttk.Entry(frame4)
rho = ttk.Entry(frame4)
gamma = ttk.Entry(frame4)
theta = ttk.Entry(frame4)
vega = ttk.Entry(frame4)

th_price.grid(row = 0, column = 1, pady = 5)
delta.grid(row = 0, column = 3, pady = 5)
vega.grid(row = 2, column = 3, pady = 5)
rho.grid(row = 1, column = 1, pady = 5)
theta.grid(row = 2, column = 1, pady = 5)
gamma.grid(row = 1, column = 3, pady = 5)

mainframe.grid(row = 0, column = 0)
frame1.grid(row = 0, columnspan = 2, sticky = "EW")
frame2.grid(row = 1, columnspan = 2, sticky = "EW")
frame3.grid(row = 2, column = 0, sticky = "EW")
frame4.grid(row = 2, column = 1,  sticky = "NSEW")

# This line of code open the window created
root.mainloop()

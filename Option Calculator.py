### This Pyhton code has been created using tkinter, to produce an user-friendly interface for option pricing
### Gianmarco Mulazzani - 3026084 ###########################################################################

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
opt_type = ttk.Label(frame2, text = "Option Type:", font = ('Helvetica', 10, 'bold')).grid(row = 0, column = 0, sticky = "W", padx = 5, pady = 5) # Option type: put or call
ex_style = ttk.Label(frame2, text = "Exercise Style:", font = ('Helvetica', 10, 'bold')).grid(row = 1, column = 0, sticky = "W", padx = 5, pady = 5) # Exercise style: american vs european
meth = ttk.Label(frame2, text = "Methodology:", font = ('Helvetica', 10, 'bold')).grid(row = 2, column = 0, sticky = "W", padx = 5, pady = 5) # Methodology: BS, Binomial Tree or JD Model
str_pr_l = ttk.Label(frame2, text = "Strike Price", font = ('Helvetica', 10, 'bold')).grid(row = 3, column = 0, sticky = "W", padx = 5, pady = 5) # Label for the strike price K
st_pr_l = ttk.Label(frame2, text = "Stock Price", font = ('Helvetica', 10, 'bold')).grid(row = 3, column = 2, sticky = "W", padx = 5, pady = 5) # Label for the stock price S
maturity_l = ttk.Label(frame2, text = "Maturity", font = ('Helvetica', 10, 'bold')).grid(row = 4, column = 0, sticky = "W", padx = 5, pady = 5) # Label for the maturity T
vol_l = ttk.Label(frame2, text = "Volatility", font = ('Helvetica', 10, 'bold')).grid(row = 4, column = 2, sticky = "W", padx = 5, pady = 5) # Label for volatility: sigma
rate_l = ttk.Label(frame2, text = "Interest Rate", font = ('Helvetica', 10, 'bold')).grid(row = 5, column = 0, sticky = "W", padx = 5, pady = 5) # Label for the interest rate: r
div_l = ttk.Label(frame2, text = "Dividend Yield", font = ('Helvetica', 10, 'bold')).grid(row = 5, column = 2, sticky = "W", padx = 5, pady = 5) # Label for the dividend yield: q

# Create these auxiliary variables to be able to retrieve if the user has selected certain features
# Note that we define boolean variables that will tell us if a certain characterist has been selected (TRUE or 1) or not (FALSE or 0)
put_check = ttk.BooleanVar()
put_check.set(FALSE)
call_check = ttk.BooleanVar()
call_check.set(FALSE)
american_check = ttk.BooleanVar()
american_check.set(FALSE)
european_check = ttk.BooleanVar()
european_check.set(FALSE)
binomial_check = ttk.BooleanVar()
binomial_check.set(FALSE)

# Create the checkbuttons that will constitute some of the inputs required for the computation
put = ttk.Checkbutton(frame2, text = "Put", variable = put_check)
call = ttk.Checkbutton(frame2, text = "Call", variable = call_check)
american = ttk.Checkbutton(frame2, text = "American", variable = american_check)
european = ttk.Checkbutton(frame2, text = "European", variable = european_check)
bs = ttk.Checkbutton(frame2, text = "Black-Scholes").grid(row = 2, column = 1, sticky = "W")
bin = ttk.Checkbutton(frame2, text = "Binomial Tree", variable = binomial_check).grid(row = 2, column = 2, sticky = "W")
jdm = ttk.Checkbutton(frame2, text = "Jump Diffusion").grid(row = 2, column = 3, sticky = "W")

# These lines are used to position in the grid the above buttons.
# As a general rule, note that we cannot directly specify these on the variables (lines 61-67) because then methods cannot be applied
put.grid(row = 0, column = 1, sticky = "W")
call.grid(row = 0, column = 2, sticky = "W")
american.grid(row = 1, column = 1, sticky = "W")
european.grid(row = 1, column = 2, sticky = "W")

# Define other varibles and their position in the grid
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

# Define the function for the option pricing calculation
# This is along function because all the scenarios are included in a single function
def OptionPricing():

    S = float(st_pr.get())
    K = float(str_pr.get())
    T = float(maturity.get())
    sigma = float(vol.get())
    r = float(rate.get())
    q = float(div.get())
    steps = 2
    delta_time = T/steps
    u = np.exp(sigma*np.sqrt(delta_time))
    d = 1/u
    q_rn = (1/(u-d))*(np.exp(r*delta_time)-d)
    qq = 1-q_rn
    dis = 1/(1+r)
    row = steps+1
    col = steps+1   

    d1 = (np.log(S/K)+(r-q+(sigma**2)/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - (sigma*(np.sqrt(T)))

    if put_check.get() == FALSE and call_check.get() == TRUE and european_check.get() == TRUE and binomial_check.get() == FALSE:
        N_d1 = norm.cdf(d1)
        N_d2 = norm.cdf(d2)
        c0 = (S*np.exp(-q*T)*N_d1)-(K*np.exp(-r*T)*N_d2)
        D = np.exp(-q*T)*N_d1
        V = K*np.exp(-r*T)*np.sqrt(T)*np.exp((-d2**2)/2)/(100*np.sqrt(2*np.pi))
        R = T*K*np.exp(-r*T)*N_d2/100
        TH = ((q*S*np.exp(-q*T)*N_d1) - (r*K*np.exp(-r*T)*N_d2) - (((sigma/np.sqrt(T*8*np.pi))*K*np.exp(-r*T)*np.exp((-d2**2)/2))))/365
        G = (1/(sigma*S*np.sqrt(T)))*np.exp(-q*T)*np.exp((-d1**2)/2)/np.sqrt(2*np.pi)

    elif put_check.get() == TRUE and call_check.get() == FALSE and european_check.get() == TRUE and binomial_check.get() == FALSE:
        N_d1 = norm.cdf(-d1)
        N_d2 = norm.cdf(-d2)
        c0 = (K*np.exp(-r*T)*N_d2)-(S*np.exp(-q*T)*N_d1)
        D = -np.exp(-q*T)*N_d1
        V = K*np.exp(-r*T)*np.sqrt(T)*np.exp((-d2**2)/2)/(100*np.sqrt(2*np.pi))
        R = -T*K*np.exp(-r*T)*N_d2/100
        TH = (-(q*S*np.exp(-q*T)*N_d1) + (r*K*np.exp(-r*T)*N_d2) - (((sigma/np.sqrt(T*8*np.pi))*K*np.exp(-r*T)*np.exp((-d2**2)/2))))/365
        G = (1/(sigma*S*np.sqrt(T)))*np.exp(-q*T)*np.exp((-d1**2)/2)/np.sqrt(2*np.pi)

    elif binomial_check.get() == TRUE and european_check.get() == FALSE:
        
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
                    if put_check.get() == TRUE and call_check.get() == FALSE:
                        payoff[i, j] = max(K-lattice[i, j], 0)
                    elif put_check.get() == FALSE and call_check.get() == TRUE:
                        payoff[i, j] = max(lattice[i, j]-K, 0)
                    else:
                        messagebox.showerror("ERROR", "You must select the Option Type")
                        return

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
calc = ttk.Button(frame3, text = "CALCULATE",command = OptionPricing).grid(row = 0, column = 0, padx = 160, pady = 5)
reset = ttk.Button(frame3, text = "RESET", command = cancel).grid(row = 1, column = 0)
plot = ttk.Button(frame3, text = "PLOT").grid(row = 2, column = 0, pady = 5)

# Define outputs: both labels and entries. Specify also their position in the grid
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

# Here all the frames are positioned within the main root
mainframe.grid(row = 0, column = 0)
frame1.grid(row = 0, columnspan = 2, sticky = "EW")
frame2.grid(row = 1, columnspan = 2, sticky = "EW")
frame3.grid(row = 2, column = 0, sticky = "EW")
frame4.grid(row = 2, column = 1,  sticky = "NSEW")

# This line of code open the window created
root.mainloop()

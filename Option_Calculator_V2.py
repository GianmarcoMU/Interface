### Creation of a GUI using tkinter for option pricing
### Gianmarco Mulazzani 2021

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
from Options import BinomialTree, BlackScholes, GreeksBinomial


# Following the underlying hierarchist approach of tkinter, create the main building block: root
root = ttk.Tk()

# Start adding some features to it
root.title("Option Calculator")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight = 1)

# Create the second-level objects, called frames, to organise better the interface
# See the pdf file to understand the graphical structure
mainframe = ttk.Frame(root) 
frame1 = ttk.Frame(mainframe, borderwidth = 5, relief = 'groove', bg = "white")
frame2 = ttk.Frame(mainframe, borderwidth = 5, relief = "groove")
frame3 = ttk.Frame(mainframe, borderwidth = 5, relief = "groove")
frame4 = ttk.Frame(mainframe, borderwidth = 5, relief = "groove")
frame5 = ttk.Frame(mainframe, borderwidth = 5, relief = "groove")
frame6 = ttk.Frame(mainframe, borderwidth = 5, relief = "groove", bg = "royalblue")
frame7 = ttk.Frame(mainframe, borderwidth = 5, relief = "groove", bg = "royalblue") 

# Create a Welcome text in the first frame to explain the functionalities of the application
welcome = ttk.Label(frame1, text = "Welcome to the Option Calculator! This application has been developed to compute the theoretical price of an option\
 derivatives using two different models. \nBefore using it make sure to use the dot notation for numbers and specify the maturity in terms\
 of years (i.e. 0.5 = 6 months and 1/365 = 1 day). Moreover, the \napplication has been made such that the Black-Scholes model is allowed only\
 for european options while the binomial tree is implemented for both styles.", justify = LEFT, relief = GROOVE, bg = "white", font = ('Helvetica', 8, 'bold', 'italic')).grid(row = 0, columnspan = 4, sticky = "W")

# Create some labels and buttons for the inputs. Note that the grid method is used to position them in the frame
opt_type = ttk.Label(frame2, text = "Option Type:", font = ('Helvetica', 8, 'bold')).grid(row = 0, column = 0, sticky = "W", padx = 5, pady = 5)
ex_style = ttk.Label(frame2, text = "Exercise Style:", font = ('Helvetica', 8, 'bold')).grid(row = 1, column = 0, sticky = "W", padx = 5, pady = 5)
str_pr_l = ttk.Label(frame2, text = "Strike Price", font = ('Helvetica', 8, 'bold')).grid(row = 3, column = 0, sticky = "W", padx = 5, pady = 5)
st_pr_l = ttk.Label(frame2, text = "Stock Price", font = ('Helvetica', 8, 'bold')).grid(row = 3, column = 2, sticky = "W", padx = 5, pady = 5)
maturity_l = ttk.Label(frame2, text = "Maturity", font = ('Helvetica', 8, 'bold')).grid(row = 4, column = 0, sticky = "W", padx = 5, pady = 5)
vol_l = ttk.Label(frame2, text = "Volatility", font = ('Helvetica', 8, 'bold')).grid(row = 4, column = 2, sticky = "W", padx = 5, pady = 5)
rate_l = ttk.Label(frame2, text = "Interest Rate", font = ('Helvetica', 8, 'bold')).grid(row = 5, column = 0, sticky = "W", padx = 5, pady = 5)
div_l = ttk.Label(frame2, text = "Dividend Yield", font = ('Helvetica', 8, 'bold')).grid(row = 5, column = 2, sticky = "W", padx = 5, pady = 5)

# Create auxiliary variables associated to check buttons, that allow to assign a boolean vectors to check boxes
put_check = ttk.BooleanVar()
put_check.set(FALSE)
call_check = ttk.BooleanVar()
call_check.set(FALSE)
american_check = ttk.BooleanVar()
american_check.set(FALSE)
european_check = ttk.BooleanVar()
european_check.set(FALSE)

# Other inputs are created in the form of check buttons, namely for the option type, exercise style and methodology
put = ttk.Checkbutton(frame2, text = "Put", variable = put_check)
call = ttk.Checkbutton(frame2, text = "Call", variable = call_check)
american = ttk.Checkbutton(frame2, text = "American", variable = american_check)
european = ttk.Checkbutton(frame2, text = "European", variable = european_check)

# The above check boxes have been positioned into the grid
put.grid(row = 0, column = 1, sticky = "W")
call.grid(row = 0, column = 2, sticky = "W")
american.grid(row = 1, column = 1, sticky = "W")
european.grid(row = 1, column = 2, sticky = "W")

# Define the output variables and their position. Note that it is necessary to specify the grid position in a separate
# line of code since otherwise it could not be possible to use certain methods with these vars.
strike_pr = ttk.Entry(frame2)
stock_pr = ttk.Entry(frame2)
maturity = ttk.Entry(frame2)
vol = ttk.Entry(frame2)
rate = ttk.Entry(frame2)
div = ttk.Entry(frame2)

strike_pr.grid(row = 3, column = 1)
stock_pr.grid(row = 3, column = 3)
maturity.grid(row = 4, column = 1)
vol.grid(row = 4, column = 3)
rate.grid(row = 5, column = 1)
div.grid(row = 5, column = 3)

# Define the Option Pricing function that using a concatanation of ifs to apply Black-Scholes or binomial model according to
# the choice of the user. Moreover, different conditions are set to allow for different exercise styles and option types.
def OptionPricing():

    # Transform the inputs into numbers since they are saved as strings
    S = float(stock_pr.get())
    K = float(strike_pr.get())
    T = float(maturity.get())
    sigma = float(vol.get())
    r = float(rate.get())
    q = float(div.get())

    if american_check.get() == TRUE and call_check.get() == TRUE and european_check.get() == FALSE and put_check.get() == FALSE:

        results_bin = BinomialTree(150, S, K, T, sigma, r, q, "american", "call")
        greeks_bin = GreeksBinomial(150, S, K, T, sigma, r, q, "american", "call")
   
    elif american_check.get() == TRUE and put_check.get() == TRUE and european_check.get() == FALSE and call_check.get() == FALSE:

        results_bin = BinomialTree(150, S, K, T, sigma, r, q, "american", "put")
        greeks_bin = GreeksBinomial(150, S, K, T, sigma, r, q, "american", "put")

    elif european_check.get() == TRUE and call_check.get() == TRUE and american_check.get() == FALSE and put_check.get() == FALSE:

        results_bin = BinomialTree(150, S, K, T, sigma, r, q, "european", "call")
        greeks_bin = GreeksBinomial(150, S, K, T, sigma, r, q, "european", "call")
        results_bs = BlackScholes(S, K, T, sigma, r, q, "european", "call")
  
    elif european_check.get() == TRUE and put_check.get() == TRUE and american_check.get() == FALSE and call_check.get() == FALSE:

        results_bin = BinomialTree(150, S, K, T, sigma, r, q, "european", "put")
        greeks_bin = GreeksBinomial(150, S, K, T, sigma, r, q, "european", "put")
        results_bs = BlackScholes(S, K, T, sigma, r, q, "european", "put")
   
    else:

        messagebox.showerror("ERROR", "Check that you have correctly specify all the inputs.")

    # These lines of code are needed to delete the content of the entry boxes and insert the new values converted in strings
    th_price_bin.delete(0, len(str(th_price_bin.get())))
    delta_bin.delete(0, len(str(delta_bin.get())))
    vega_bin.delete(0, len(str(vega_bin.get())))
    rho_bin.delete(0, len(str(rho_bin.get())))
    theta_bin.delete(0, len(str(theta_bin.get())))
    gamma_bin.delete(0, len(str(gamma_bin.get())))
    th_price_bs.delete(0, len(str(th_price_bs.get())))
    delta_bs.delete(0, len(str(delta_bs.get())))
    vega_bs.delete(0, len(str(vega_bs.get())))
    rho_bs.delete(0, len(str(rho_bs.get())))
    theta_bs.delete(0, len(str(theta_bs.get())))
    gamma_bs.delete(0, len(str(gamma_bs.get())))  
    
    th_price_bin.insert(0, str(results_bin['Option_Price']))
    delta_bin.insert(0, str(results_bin['Delta']))
    vega_bin.insert(0, str(greeks_bin['Vega']))
    rho_bin.insert(0, str(greeks_bin['Rho']))
    theta_bin.insert(0,str(results_bin['Theta']))
    gamma_bin.insert(0,str(results_bin['Gamma']))   
    th_price_bs.insert(0, str(results_bs['Option_Price']))
    delta_bs.insert(0, str(results_bs['Delta']))
    vega_bs.insert(0, str(results_bs['Vega']))
    rho_bs.insert(0, str(results_bs['Rho']))
    theta_bs.insert(0,str(results_bs['Theta']))
    gamma_bs.insert(0,str(results_bs['Gamma']))

# The following function is the one associated to Reset button, to clear everything
def cancel():
    strike_pr.delete(0, len(str(strike_pr.get())))
    stock_pr.delete(0, len(str(stock_pr.get())))
    maturity.delete(0, len(str(maturity.get())))
    rate.delete(0, len(str(rate.get())))
    vol.delete(0, len(str(vol.get())))
    div.delete(0, len(str(div.get())))
    th_price_bin.delete(0, len(str(th_price_bin.get())))
    delta_bin.delete(0, len(str(delta_bin.get())))
    vega_bin.delete(0, len(str(vega_bin.get())))
    rho_bin.delete(0, len(str(rho_bin.get())))
    theta_bin.delete(0, len(str(theta_bin.get())))
    gamma_bin.delete(0, len(str(gamma_bin.get())))
    th_price_bs.delete(0, len(str(th_price_bs.get())))
    delta_bs.delete(0, len(str(delta_bs.get())))
    vega_bs.delete(0, len(str(vega_bs.get())))
    rho_bs.delete(0, len(str(rho_bs.get())))
    theta_bs.delete(0, len(str(theta_bs.get())))
    gamma_bs.delete(0, len(str(gamma_bs.get())))
    put.deselect()
    call.deselect()
    american.deselect()
    european.deselect()
      

# Create two buttons that calculate outputs and reset everything
calc = ttk.Button(frame3, text = "CALCULATE",command = OptionPricing, height = 1, width = 15, fg = "green", bg = "#bded9b", font = ('Helvetica', 10, 'bold')).grid(row = 0, column = 0, padx = 130, pady = 23.4)
reset = ttk.Button(frame3, text = "RESET", command = cancel, height = 1, width = 15, fg = "red", bg = "#ff8989", font = ('Helvetica', 10, 'bold')).grid(row = 1, column = 0, pady = 23.3)

# Define outputs: both labels and entries and their position using grid
method_bin = ttk.Label(frame6, text = "Binomial Tree (CRR Model)", font = ('Helvetica', 10, 'bold'), bg = "royalblue", fg = "white").grid(row = 0, column = 0, padx = 125, pady = 2)
th_price_l_bin = ttk.Label(frame4, text = "Theoretical Price", font = ('Helvetica', 8, 'bold')).grid(row = 1, column = 0, sticky = "W", pady = 5)
delta_l_bin = ttk.Label(frame4, text = "Delta", font = ('Helvetica', 8, 'bold')).grid(row = 1, column = 2, sticky = "W", padx = 20)
rho_l_bin = ttk.Label(frame4, text = "Rho", font = ('Helvetica', 8, 'bold')).grid(row = 2, column = 0, sticky = "W", pady = 5)
gamma_l_bin = ttk.Label(frame4, text = "Gamma", font = ('Helvetica', 8, 'bold')).grid(row = 2, column = 2, sticky = "W", pady = 5, padx = 20)
theta_l_bin = ttk.Label(frame4, text = "Theta", font = ('Helvetica', 8, 'bold')).grid(row = 3, column = 0, sticky = "W")
vega_l_bin = ttk.Label(frame4, text = "Vega", font = ('Helvetica', 8, 'bold')).grid(row = 3, column = 2, sticky = "W", pady = 5, padx = 20)

th_price_bin = ttk.Entry(frame4)
delta_bin = ttk.Entry(frame4)
rho_bin = ttk.Entry(frame4)
gamma_bin = ttk.Entry(frame4)
theta_bin = ttk.Entry(frame4)
vega_bin = ttk.Entry(frame4)

method_bs = ttk.Label(frame7, text = "Black-Scholes Model", font = ('Helvetica', 10, 'bold'), bg = "royalblue", fg = "white").grid(row = 0, column = 0, padx = 125, pady = 2)
th_price_l_bs = ttk.Label(frame5, text = "Theoretical Price", font = ('Helvetica', 8, 'bold')).grid(row = 1, column = 0, sticky = "W", pady = 5)
delta_l_bs = ttk.Label(frame5, text = "Delta", font = ('Helvetica', 8, 'bold')).grid(row = 1, column = 2, sticky = "W")
rho_l_bs = ttk.Label(frame5, text = "Rho", font = ('Helvetica', 8, 'bold')).grid(row = 2, column = 0, sticky = "W", pady = 5)
gamma_l_bs= ttk.Label(frame5, text = "Gamma", font = ('Helvetica', 8, 'bold')).grid(row = 2, column = 2, sticky = "W", pady = 5)
theta_l_bs = ttk.Label(frame5, text = "Theta", font = ('Helvetica', 8, 'bold')).grid(row = 3, column = 0, sticky = "W")
vega_l_bs= ttk.Label(frame5, text = "Vega", font = ('Helvetica', 8, 'bold')).grid(row = 3, column = 2, sticky = "W", pady = 5)

th_price_bs= ttk.Entry(frame5)
delta_bs = ttk.Entry(frame5)
rho_bs = ttk.Entry(frame5)
gamma_bs = ttk.Entry(frame5)
theta_bs = ttk.Entry(frame5)
vega_bs = ttk.Entry(frame5)

th_price_bin.grid(row = 1, column = 1, pady = 5)
delta_bin.grid(row = 1, column = 3, pady = 5)
gamma_bin.grid(row = 2, column = 3, pady = 5)
rho_bin.grid(row = 2, column = 1, pady = 5)
theta_bin.grid(row = 3, column = 1, pady = 5)
vega_bin.grid(row = 3, column = 3, pady = 5)

th_price_bs.grid(row = 1, column = 1, pady = 5)
delta_bs.grid(row = 1, column = 3, pady = 5)
gamma_bs.grid(row = 2, column = 3, pady = 5)
rho_bs.grid(row = 2, column = 1, pady = 5)
theta_bs.grid(row = 3, column = 1, pady = 5)
vega_bs.grid(row = 3, column = 3, pady = 5)


# The final step is to position the four frames defined
mainframe.grid(row = 0, column = 0)
frame1.grid(row = 0, columnspan = 2, sticky = "EW")
frame2.grid(row = 1, column = 0, sticky = "EW")
frame3.grid(row = 1, column = 1, sticky = "EW")
frame4.grid(row = 3, column = 0,  sticky = "NSEW")
frame5.grid(row = 3, column = 1, sticky = "NSEW")
frame6.grid(row = 2, column = 0, sticky = "NSEW")
frame7.grid(row = 2, column = 1, sticky = "NSEW")


# This line of code open the window created
root.mainloop()
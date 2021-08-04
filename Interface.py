### Here we try to create an interface starting from the original documentation about tkinter

# Firstly, import the required library. Namely, tkinter
import tkinter as ttk
from tkinter import font, mainloop

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
start_l = ttk.Label(frame2, text = "Start Date", font = ('Helvetica', 10, 'bold')).grid(row = 4, column = 0, sticky = "W", padx = 5, pady = 5)
exp_l = ttk.Label(frame2, text = "Expiration Date", font = ('Helvetica', 10, 'bold')).grid(row = 4, column = 2, sticky = "W", padx = 5, pady = 5)
vol_l = ttk.Label(frame2, text = "Volatility", font = ('Helvetica', 10, 'bold')).grid(row = 5, column = 0, sticky = "W", padx = 5, pady = 5)
rate_l = ttk.Label(frame2, text = "Interest Rate", font = ('Helvetica', 10, 'bold')).grid(row = 5, column = 2, sticky = "W", padx = 5, pady = 5)
div_l = ttk.Label(frame2, text = "Dividend Yield", font = ('Helvetica', 10, 'bold')).grid(row = 5, column = 4, sticky = "W", padx = 5, pady = 5)

put = ttk.Checkbutton(frame2, text = "Put").grid(row = 0, column = 1, sticky = "W")
call = ttk.Checkbutton(frame2, text = "Call").grid(row = 0, column = 2, sticky = "W")
american = ttk.Checkbutton(frame2, text = "American").grid(row = 1, column = 1, sticky = "W")
european = ttk.Checkbutton(frame2, text = "European").grid(row = 1, column = 2, sticky = "W")
bs = ttk.Checkbutton(frame2, text = "Black-Scholes").grid(row = 2, column = 1, sticky = "W")
bin = ttk.Checkbutton(frame2, text = "Binomial Tree").grid(row = 2, column = 2, sticky = "W")
jdm = ttk.Checkbutton(frame2, text = "Jump Diffusion").grid(row = 2, column = 3, sticky = "W")

str_pr = ttk.Entry(frame2).grid(row = 3, column = 1)
st_pr = ttk.Entry(frame2).grid(row = 3, column = 3)
start = ttk.Entry(frame2).grid(row = 4, column = 1)
exp = ttk.Entry(frame2).grid(row = 4, column = 3)
vol = ttk.Entry(frame2).grid(row = 5, column = 1)
rate = ttk.Entry(frame2).grid(row = 5, column = 3)
div = ttk.Entry(frame2).grid(row = 5, column = 5)

# Create two buttons that calculate outputs and reset inputs
calc = ttk.Button(frame3, text = "CALCULATE").grid(row = 0, column = 0, padx = 160, pady = 5)
reset = ttk.Button(frame3, text = "RESET").grid(row = 1, column = 0)
plot = ttk.Button(frame3, text = "PLOT").grid(row = 2, column = 0, pady = 5)

# Define outputs: both labels and entries
th_price_l = ttk.Label(frame4, text = "Theoretical Price").grid(row = 0, column = 0, sticky = "W", pady = 5)
delta_l = ttk.Label(frame4, text = "Delta").grid(row = 0, column = 2, sticky = "W")
rho_l = ttk.Label(frame4, text = "Rho").grid(row = 1, column = 0, sticky = "W", pady = 5)
gamma_l = ttk.Label(frame4, text = "Gamma").grid(row = 1, column = 2, sticky = "W", pady = 5)
theta_l = ttk.Label(frame4, text = "Theta").grid(row = 2, column = 0, sticky = "W")
vega_l = ttk.Label(frame4, text = "Vega").grid(row = 2, column = 2, sticky = "W", pady = 5)

th_price = ttk.Entry(frame4).grid(row = 0, column = 1, pady = 5)
delta = ttk.Entry(frame4).grid(row = 0, column = 3, pady = 5)
rho = ttk.Entry(frame4).grid(row = 1, column = 1, pady = 5)
gamma = ttk.Entry(frame4).grid(row = 1, column = 3, pady = 5)
theta = ttk.Entry(frame4).grid(row = 2, column = 1, pady = 5)
vega = ttk.Entry(frame4).grid(row = 2, column = 3, pady = 5)

mainframe.grid(row = 0, column = 0)
frame1.grid(row = 0, columnspan = 2, sticky = "EW")
frame2.grid(row = 1, columnspan = 2, sticky = "EW")
frame3.grid(row = 2, column = 0, sticky = "EW")
frame4.grid(row = 2, column = 1,  sticky = "NSEW")

# This line of code open the window created
root.mainloop()

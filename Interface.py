### Here we try to create an interface starting from the original documentation about tkinter

# Firstly, import the required library. Namely, tkinter
import tkinter as ttk
from tkinter import font, mainloop

# Following the underlying hierarchist approach of tkinter, create the main building block: root
root = ttk.Tk()

# Start adding some features to it
root.title("Option Calculator")
root.geometry("800x700")
root.grid_columnconfigure(0, weight=1)

#Create frames to organise better the interface
mainframe = ttk.Frame(root)
frame2 = ttk.Frame(mainframe, borderwidth = 5, relief = "ridge")
frame3 = ttk.Frame(mainframe, borderwidth = 5, relief = "ridge")
frame4 = ttk.Frame(mainframe, borderwidth = 5, relief = "ridge")

#Create some labels to make the interface clearer
opt_type = ttk.Label(frame2, text = "Option Type:", font = ('Helvetica', 10, 'bold'))
ex_style = ttk.Label(frame2, text = "Exercise Style:", font = ('Helvetica', 10, 'bold'))
meth = ttk.Label(frame2, text = "Methodology:", font = ('Helvetica', 10, 'bold'))
str_pr_l = ttk.Label(frame3, text = "Strike Price", font = ('Helvetica', 10, 'bold'))
st_pr_l = ttk.Label(frame3, text = "Stock Price", font = ('Helvetica', 10, 'bold'))
div_l = ttk.Label(frame3, text = "Dividend Yield", font = ('Helvetica', 10, 'bold'))
start_l = ttk.Label(frame3, text = "Start Date", font = ('Helvetica', 10, 'bold'))
exp_l = ttk.Label(frame3, text = "Expiration Date", font = ('Helvetica', 10, 'bold'))
vol_l = ttk.Label(frame3, text = "Volatility", font = ('Helvetica', 10, 'bold'))
rate_l = ttk.Label(frame3, text = "Interest Rate", font = ('Helvetica', 10, 'bold'))

# Create some useful buttons
put = ttk.Checkbutton(frame2, text = "Put")
call = ttk.Checkbutton(frame2, text = "Call")
american = ttk.Checkbutton(frame2, text = "American")
european = ttk.Checkbutton(frame2, text = "European")
bs = ttk.Checkbutton(frame2, text = "Black-Scholes")
bin = ttk.Checkbutton(frame2, text = "Binomial Tree")
jdm = ttk.Checkbutton(frame2, text = "Jump Diffusion")

#Position labels and buttons accordingly
opt_type.grid(row = 0, column = 0, sticky = "W", padx = 5, pady = 5)
put.grid(row = 0, column = 1, sticky = "W")
call.grid(row = 0, column = 2, sticky = "W")

ex_style.grid(row = 1, column = 0, sticky = "W", padx = 5, pady = 5)
american.grid(row = 1, column = 1, sticky = "W")
european.grid(row = 1, column = 2, sticky = "W")

meth.grid(row = 2, column = 0, sticky = "W", padx = 5, pady = 5)
bs.grid(row = 2, column = 1, sticky = "W")
bin.grid(row = 2, column = 2, sticky = "W")
jdm.grid(row = 2, column = 3, sticky = "W")

# Define variables that must be inserted manually
str_pr = ttk.Entry(frame3)
st_pr = ttk.Entry(frame3)
start = ttk.Entry(frame3)
exp = ttk.Entry(frame3)
vol = ttk.Entry(frame3)
rate = ttk.Entry(frame3)
div = ttk.Entry(frame3)

#Let organise the second frame with other entry variables
str_pr_l.grid(row = 3, column = 0, sticky = "W", padx = 5, pady = 5)
str_pr.grid(row = 3, column = 1)

st_pr_l.grid(row = 3, column = 2, sticky = "W", padx = 5, pady = 5)
st_pr.grid(row = 3, column = 3)

start_l.grid(row = 4, column = 0, sticky = "W", padx = 5, pady = 5)
start.grid(row = 4, column = 1)

exp_l.grid(row = 4, column = 2, sticky = "W", padx = 5, pady = 5)
exp.grid(row = 4, column = 3)

vol_l.grid(row = 5, column = 0, sticky = "W", padx = 5, pady = 5)
vol.grid(row = 5, column = 1)

rate_l.grid(row = 5, column = 2, sticky = "W", padx = 5, pady = 5)
rate.grid(row = 5, column = 3)

div_l.grid(row = 5, column = 4, sticky = "W", padx = 5, pady = 5)
div.grid(row = 5, column = 5)

#Create two buttons that calculate outputs and reset inputs
calc = ttk.Button(frame4, text = "CALCULATE")
reset = ttk.Button(frame4, text = "RESET")

calc.grid(row = 0, column = 2, padx = 150)
reset.grid(row = 0, column = 3)


#Organise frames in the root
mainframe.grid(row = 0, column = 0)
frame2.grid(row = 0, sticky = "EW")
frame3.grid(row = 1, sticky = "EW")
frame4.grid(row = 2, sticky = "EW")

# This line of code open the window created
root.mainloop()
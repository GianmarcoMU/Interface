import tkinter as ttk
from tkinter import *

# We try to create two functions that use Entry and Checkbutton widgets in tkinter. 
# This is just a useless example to retrieve the values that the user has inserted in the Entries and Checkbuttons
# widgets introduced in the interface. In particular, for the Checkbutton we need to specify a boolean value that takes vlaue 1 if the cell is checked
# and 0 otherwise. For the Entry widget it is simpler but it is important to pay attention to some details. 

root = ttk.Tk()

st_price = ttk.Entry()
str_price = ttk.Entry()
var1 = ttk.BooleanVar()
var1.set(FALSE)
put = ttk.Checkbutton(text = "PUT", variable = var1)
put.grid(row = 5, column = 0)

st_price.grid(row = 0, column = 0)
str_price.grid(row = 1, column = 0)

def prova():
    p1 = st_price.get()
    p2 = str_price.get()
    res = int(p1) + int(p2)
    res_dis = ttk.Entry()
    res_dis.insert(0, str(res))
    res_dis.grid(row = 4, column = 0, pady = 5)

def check():
    print_put = ttk.Entry()
    if var1.get() == TRUE:
        print_put.insert(0, "You choose PUT")
    else:
        print_put.insert(0, "You choose a CALL")
    print_put.grid(row = 7, column = 0)

calcola = ttk.Button(text = "CALCOLA", command = prova)
calcola.grid(row = 3, column = 0)

controlla = ttk.Button(text = "CHECK", command = check).grid(row = 6, column = 0)

root.mainloop()




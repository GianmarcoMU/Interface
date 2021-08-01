import tkinter as tk

# Create a window box
window = tk.Tk() #Richiama il modulo Tk per creare una finestra
window.geometry("700x600") #Definiamo la geometria della finestra
window.title("Automated Computation Option Pricing")
window.grid_columnconfigure(0, weight=1) #Adatta il contenuto della finestra quando si cambiano le dimensioni
#window.resizable(False, False) #Rende impossibile modificare le dimensioni della finestra
#window.configure(background="grey") Def colore finestra

#Add a label under the title of the window
# sticky serve per rendere la scritta fissa rispetto un punto cardinale
welcome_label = tk.Label(window,
                         text="Welcome to the program for automatically compute option metrics",
                         font=("Helvetica", 10))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

#Inseriamo un campo testuale
text_input = tk.Entry()
text_input.grid(row=1, column=1, sticky="E")

# Here we define a function that will be executed when 
# pushing on the button "Strike"
def first_print():
    text = "Specify the strike price"
    text_output = tk.Label(window, text=text)
    text_output.grid(row=1, column=1)

# This lines create a button that generates what the above function does
#first_button = tk.Button(text="Strike", command=first_print)
#first_button.grid(row=1, column=1, sticky="W", padx=5, pady=5)

if __name__ == "__main__":
    window.mainloop()

from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)


# Label

my_label = Label(text="Unit converter", font=("Arial", 24, "bold"))
my_label.pack()

# Button

def button_listener():
    my_label.config(text=input.get())

button = Button(text="Click me", command=button_listener)
button.pack()

# Entry

input = Entry(width=10)
input.pack()

window.mainloop()



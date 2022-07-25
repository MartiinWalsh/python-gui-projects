from tkinter import *

window = Tk()
window.title("Unit Converter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles_to_km_conversion = float(miles_input.get()) * 1.609
    km_value_label.config(text=f"{miles_to_km_conversion}")

miles_input = Entry(width=7)
miles_input.grid(column=0, row=0)

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=1, row=0)

km_value_label = Label(text="0", font=("Arial", 24, "bold"))
km_value_label.grid(column=0, row=1)

km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=0, row=2)


window.mainloop()



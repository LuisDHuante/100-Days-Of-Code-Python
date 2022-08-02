from cProfile import label
from os import kill
from tkinter import *

def miles_to_km():
    miles = float(miles_entry.get())
    kms = round(miles * 1.609344, 3)
    result.config(text=f"{kms}")


window = Tk()
window.title("Miles to Kilometers Calculator")
window.config(padx=20, pady=20)


miles_entry = Entry()
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_to_label.grid(column=0, row=1)

result = Label()
result.grid(column=1, row=1)


km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)


calculate_button = Button(text="Calculate", font=("Arial", 12, "bold"), command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()

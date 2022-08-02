from tkinter import *


window = Tk()
window.title("My Grid based GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


label = Label(text="I am a Label", font=("Arial", 12, "bold"))
label.grid(column=0, row=0)


button = Button(text="I am a Button", font=("Arial", 12, "bold"))
button.grid(column=2, row=0)


button = Button(text="I am another Button", font=("Arial", 12, "bold"))
button.grid(column=1, row=1)

entry = Entry()
entry.grid(column=3, row=2)
window.mainloop()

from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- IS CARD KNOWN?------------------------------- #

def is_known():
    to_learn.remove(card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    random_word()

# ---------------------------- FIPPING CARDS------------------------------- #

def flip_card():
    window.after(1000)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=card["English"])

    #Configuring new background image
    canvas.itemconfig(card_image, image=card_back_img)

    #Configuring title and word cards to white
    canvas.itemconfig(card_title, fill="white")
    canvas.itemconfig(card_word, fill="white")

# ---------------------------- READING DATA ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

    
# ---------------------------- CHOOSING RANDOM WORD ------------------------------- #
def random_word():
    global card
    card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French")
    canvas.itemconfig(card_word, text=card["French"])

    #Configuring new background image
    canvas.itemconfig(card_image, image=card_front_img)

    #Configuring title and word cards to white
    canvas.itemconfig(card_title, fill="black")
    canvas.itemconfig(card_word, fill="black")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Learning")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150,text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


#Images
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

#Buttons
right_button = Button(image=right_image, highlightthickness=0, border=0, command=is_known)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, border=0, command=flip_card)
wrong_button.grid(row=1, column=0)

random_word()

window.mainloop()

from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
#import pyperclip

# ---------------------------- PASSWORD FINDER ------------------------------- #
def find_password():
    global website_input
    website= website_input.get()



    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(
            title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title="Data", message=f"Username: {email}\n Password: {password}")
        else:
            messagebox.showinfo(
                title="Error", message="No details for this website exist ")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(END, f"{password}")
    #pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    global website_input
    global email_input
    global password_input

    website_name = website_input.get()
    username_data = email_input.get()
    password = password_input.get()

    new_data = {
        website_name: {
        "email": username_data,
        "password": password
        }
    }

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_correct = messagebox.askokcancel(title=website_name, message=f"These are the details entered \n\n Email: {username_data} \n\nPassword: {password} \n\n Are you sure you want to save?" )
        
        if is_correct:
            try:

                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:

                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
                    
            else:
                #Updating old data with new data
                data.update(new_data)

                #Saving updated data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)


            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

#Entries
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(END, "luisdhuante@gmail.com")
password_input = Entry(width=21)
password_input.grid(row=3, column=1)


#Buttons
password_button = Button(text="Generate password", command=generate_password)
password_button.grid(row=3, column=2)
entry_button = Button(text="Add data", width=44, command=save_data)
entry_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()

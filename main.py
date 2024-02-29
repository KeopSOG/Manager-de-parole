from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- GENERARE PAROLA ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SALVARE PAROLA ------------------------------- #
def save():

    web = web_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    new_data = {
        web: {
            "user": user,
            "password": password,
        }
    }


    if len(web) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showerror(title="Eroare", message="Completați toate spațiile!")
    else:
        try:

            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            user_entry.delete(0, END)
            pass_entry.delete(0, END)

def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Eroare", message="Fișierul nu există!")
    else:
        if website in data:
            user = data[website]["user"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"User: {user}\nParola: {password}")
        else:
            messagebox.showerror(title="Eroare", message=f"Nu există informații pentru: {website}")


# ---------------------------- CONFIGURARE UI ------------------------------- #
window = Tk()
window.title("Manager Parole")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

web_label = Label(text="Aplicatie/Site:")
web_label.grid(column=0, row=1)
web_entry = Entry(width=25)
web_entry.grid(column=1, row=1, sticky=EW)
web_entry.focus()

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
user_entry = Entry(width=52)
user_entry.grid(column=1, row=2, columnspan=2, sticky=EW)

pass_label = Label(text="Parola:")
pass_label.grid(column=0, row=3)
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3, sticky=EW)

search_button = Button(text="Caută", width=15, command=find_password)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generare Parola", width=15, command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Adaugă", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
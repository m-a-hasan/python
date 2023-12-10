import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ------------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    site = site_input.get()
    user = user_input.get()

    if len(site) == 0 and len(user) == 0:
        messagebox.showinfo("Oops", "Please don't leave website and username fields empty!")
    elif len(site) == 0:
        messagebox.showinfo("Oops", "Please don't leave website name field empty!")
    elif len(user) == 0:
        messagebox.showinfo("Oops", "Please don't leave user name field empty!")
    else:
        try:
            with open("data.json", "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            messagebox.showinfo("Oops", "That website username combination doesn't exist in "
                                        "password manager!")
        else:
            try:
                username = data[site]["username"]
                password = data[site]["password"]
            except KeyError:
                messagebox.showinfo("Oops", "That website username combination doesn't exist in "
                                            "password manager!")
            else:
                if username == user:
                    messagebox.showinfo(site, f"Email: {user}\nPassword: {password}")
                    pyperclip.copy(password)
                else:
                    messagebox.showinfo("Oops", "Username doesn't match")
        finally:
            site_input.focus()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = site_input.get()
    user = user_input.get()
    password = pass_input.get()

    new_data = {
        site: {
            "username": user,
            "password": password
        }
    }

    if len(site) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please don't leave any fields empty!")
        if len(site) == 0:
            site_input.focus()
        elif len(user) == 0:
            user_input.focus()
        else:
            pass_input.focus()
    else:
        user_reply = messagebox.askokcancel(title=site, message=f"You have entered below information:\nWebsite: "
                                                                f"{site}\nUsername: {user}\nPassword: {password}"
                                                                f"\n\nAre they correct?")

        if user_reply:
            try:
                with open("data.json", "r") as my_file:
                    data = json.load(my_file)
            except FileNotFoundError:
                with open("data.json", "w") as my_file:
                    json.dump(new_data, my_file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as my_file:
                    json.dump(data, my_file, indent=4)
            finally:
                site_input.delete(0, "end")
                pass_input.delete(0, "end")
                site_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
img_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_file)
canvas.grid(row=0, column=1)

site_label = Label(text="Website:")
site_label.grid(row=1, column=0)

site_input = Entry(width=18)
site_input.grid(row=1, column=1)
site_input.focus()

search_button = Button(text="Search", width=12, command=search)
search_button.grid(row=1, column=2)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

user_input = Entry(width=35)
user_input.grid(row=2, column=1, columnspan=2)
user_input.insert(0, "abidhasan@email.com")

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

pass_input = Entry(width=18)
pass_input.grid(row=3, column=1)

pass_button = Button(text="Generate Password", width=12, command=generate_password)
pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

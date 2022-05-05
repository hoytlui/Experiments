import tkinter as tk
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    num_letters = 8
    num_numbers = 4
    num_symbols = 2

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    # create lists of letters, numbers and symbols
    pw_letter = [random.choice(letters) for _ in range(num_letters)]
    pw_number = [random.choice(numbers) for _ in range(num_numbers)]
    pw_symbol = [random.choice(symbols) for _ in range(num_symbols)]

    # combine list, shuffle elements in list
    password_list = pw_letter + pw_number + pw_symbol
    random.shuffle(password_list)

    # convert list into str
    password = "".join(password_list)

    # delete existing password and generate new password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().lower()
    username = username_entry.get()
    password = password_entry.get()

    # create dict for json format
    new_data_dict = {
        website: {
            'username': username,
            'password': password
        }
    }

    # if any field left blank, pop up message box
    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title='Error', message='Fields required.')
    else:
        try:
            # read data
            with open('password.json', 'r') as password_file:
                password_dict = json.load(password_file)
        except FileNotFoundError:
            # write new data to create new file
            with open('password.json', 'w') as password_file:
                json.dump(new_data_dict, password_file, indent=4)
        else:
            # continue to update data
            password_dict.update(new_data_dict)
            # save updated data
            with open('password.json', 'w') as password_file:
                json.dump(password_dict, password_file, indent=4)
        finally:    
            # clear entry field
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get().lower()
    try:
        with open("password.json") as password_file:
            data_dict = json.load(password_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found.")
    else:
        # if website already exists, show username and password
        if website in data_dict:
            username = data_dict[website]["username"]
            password = data_dict[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
        # otherwise, show error message
        else:
            messagebox.showinfo(title="Error", message="No password saved for this website.")


# ---------------------------- UI SETUP ------------------------------- #
# set up window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create canvas
canvas = tk.Canvas(width=200, height=200)
# add image
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(140, 100, image=logo_img)

# create labels
website_label = tk.Label(text="Website:")
username_label = tk.Label(text="Username:")
password_label = tk.Label(text="Password:")

# create entries
website_entry = tk.Entry(width=22)
website_entry.focus()   # focus cursor on field
username_entry = tk.Entry(width=38)
username_entry.insert(0, 'name@email.com')   # insert predetermined value
password_entry = tk.Entry(width=22)

# create buttons
password_button = tk.Button(text="Generate Password", width=12, command=generate_password)
save_button = tk.Button(text="Save", width=36, command=save_password)
search_button = tk.Button(text="Search", width=12, command=search_password)

# position
canvas.grid(row=1, column=2)
website_label.grid(row=2, column=1)
website_entry.grid(row=2, column=2)
username_label.grid(row=3, column=1)
username_entry.grid(row=3, column=2, columnspan=2)
password_label.grid(row=4, column=1)
password_entry.grid(row=4, column=2)
password_button.grid(row=4, column=3)
save_button.grid(row=5, column=2, columnspan=2)
search_button.grid(row=2, column=3)

window.mainloop()
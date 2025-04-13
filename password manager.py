from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


def open_new_window(results):
    new_window = Toplevel(window)
    new_window.title("Save Info")

    label = Label(new_window, text=results)
    label.pack(padx=50, pady=50)

# ----------------------------FIND PASSWORD------------------------------- #
def find_password():
  try:
     with open("info.json", "r") as info:
        data = json.load(info)
        website = website_entry.get().title()
        if website in data:
           results = f"Website: {website}\nEmail: {data[website]["Username"]}\nPassword: {data[website]["Password"]}"
           open_new_window(results)
        else:
           messagebox.showinfo(title="Not Found", message=f"No website found with the name: {website}")
  except FileNotFoundError:
     messagebox.showinfo(title="Error", message=f"There are no websites saved.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '?', '@', '*', '+']
    password_list = ([choice(letters) for _ in range(randint(8,10))]
                     + [choice(numbers) for _ in range(randint(1,3))]
                 +[choice(symbols) for _ in range(randint(1,3))])
    shuffle(password_list)
    created_password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.insert(0, created_password)
    pyperclip.copy(created_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "Username": username,
            "Password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
         messagebox.showinfo(title="Missing info.", message="Please don't leave any boxes blank.")
    else:
       try:
          with open("info.json", "r") as data_file:
             data = json.load(data_file)
             data.update(new_data)
       except FileNotFoundError:
          with open("info.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
       else:
          with open("info.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
       finally:
           website_entry.delete(0, "end")
           password_entry.delete(0, "end")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2, )

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=46)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

username_entry = Entry(width=65)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "angela@gmail.com")

password_entry = Entry(width=46)
password_entry.grid(column=1, row=3)

create_password = Button(text="Generate Password", command=generate_password)
create_password.grid(column=2,row=3)

add_button = Button(text="Add",width=55, command=save)
add_button.grid(column=1,row=4, columnspan=2)

search_button = Button(text="Search", width=15, relief=GROOVE, command=find_password)
search_button.grid(column=2, row=1)








window.mainloop()
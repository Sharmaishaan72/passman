import tkinter as tk
import os

#local imports
from .addpass import open_add_password_form
from .deletepass import open_delete_password_form
from .findpass import open_search_password_form

#handling buttons (events where the buttons are clicked)
def search_passwords():
    open_search_password_form()
    

def delete_data():
    open_delete_password_form()

def add_new_password():
    open_add_password_form()
    

#main menu window
def open_main_menu():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("537x326")


    label_welcome = tk.Label(root, text="Welcome To main menu\nChoose What You Want to do:", font=("Arial", 16, "italic", "bold"))
    label_welcome.pack(pady=20)

    button_search = tk.Button(root, text="Click Here To Search for Stored Passwords", width=40, command=search_passwords)
    button_search.pack(pady=10)

    button_delete_data = tk.Button(root, text="Click Here To Delete Data", width=40, command=delete_data)
    button_delete_data.pack(pady=10)

    button_add_password = tk.Button(root, text="Click Here To Add New Passwords", width=40, command=add_new_password)
    button_add_password.pack(pady=10)

    #this returns the login of the device
    username = os.getlogin()


    label_username = tk.Label(root, text=f"Username: {username}", font=("Arial", 16))
    label_username.pack(pady=20)

    root.mainloop()

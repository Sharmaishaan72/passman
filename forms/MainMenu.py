import tkinter as tk
import os

from .addpass import open_add_password_form
from .deletepass import open_delete_password_form
from .findpass import open_search_password_form

# Function to handle button clicks
def search_passwords():
    open_search_password_form()
    

def delete_data():
    open_delete_password_form()
    print(f"Attempting to delete entry for application: ")

def add_new_password():
    open_add_password_form()
    

# Create the main window
def open_main_menu():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("537x326")

    # Create a welcome label
    label_welcome = tk.Label(root, text="Welcome To main menu\nChoose What You Want to do:", font=("Arial", 16, "italic", "bold"))
    label_welcome.pack(pady=20)

    # Create buttons for various actions
    button_search = tk.Button(root, text="Click Here To Search for Stored Passwords", width=40, command=search_passwords)
    button_search.pack(pady=10)

    button_delete_data = tk.Button(root, text="Click Here To Delete Data", width=40, command=delete_data)
    button_delete_data.pack(pady=10)

    button_add_password = tk.Button(root, text="Click Here To Add New Passwords", width=40, command=add_new_password)
    button_add_password.pack(pady=10)

    # Get the username using os.getlogin()
    username = os.getlogin()

    # Create a label to display the username
    label_username = tk.Label(root, text=f"Username: {username}", font=("Arial", 16))
    label_username.pack(pady=20)

    # Run the Tkinter event loop
    root.mainloop()

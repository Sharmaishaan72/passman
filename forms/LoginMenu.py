import tkinter as tk
import os

from .MainMenu import open_main_menu  


def open_login_window():
    #nested func to get login info
    def login():
        entered_username = entry_username.get()
        entered_password = entry_password.get()

        #checking if the username and password match 
        if entered_username == os.getlogin() and entered_password == "Ishaan12345":
            root.destroy()  #closes the window
            open_main_menu()  #opens a new form
        else:
            error_label.config(text="Invalid username or password.", fg="red")
            #config for the error label defined on line 46


    root = tk.Tk()
    root.title("Login")
    root.geometry("512x375")


    label_title = tk.Label(root, text="Python Password Manager", font=("Arial", 28, "italic", "bold"))
    label_title.pack(pady=20)

    label_username = tk.Label(root, text="Username:", font=("Arial", 16))
    label_username.pack(pady=5)

    entry_username = tk.Entry(root, width=30)
    entry_username.pack(pady=5)

    label_password = tk.Label(root, text="Password:", font=("Arial", 16))
    label_password.pack(pady=5)

    entry_password = tk.Entry(root, show="*", width=30)
    entry_password.pack(pady=5)

    login_button = tk.Button(root, text="Log in", command=login)
    login_button.pack(pady=20)


    error_label = tk.Label(root, text="", font=("Arial", 12))
    error_label.pack(pady=5)


    root.mainloop()



import tkinter as tk
from tkinter import messagebox
import string,random

from data.dbfunc import write,returnapps


def open_add_password_form():
    
    add_password_window = tk.Tk()
    add_password_window.title("Add Password")
    add_password_window.geometry("540x350")

   
    label_title = tk.Label(add_password_window, text="Add Password", font=("Arial", 12, "italic", "bold"))
    label_title.place(x=150, y=30, width=200, height=150)

 
    label_login = tk.Label(add_password_window, text="Login:", font=("Arial", 16))
    label_login.place(x=50, y=160, width=111, height=41)

    label_password = tk.Label(add_password_window, text="Password:", font=("Arial", 16))
    label_password.place(x=50, y=200, width=101, height=51)

    label_application = tk.Label(add_password_window, text="Application:", font=("Arial", 16))
    label_application.place(x=50, y=250, width=111, height=31)

  
    entry_login = tk.Entry(add_password_window, font=("Arial", 12))
    entry_login.place(x=190, y=170, width=181, height=31)

    entry_password = tk.Entry(add_password_window, font=("Arial", 12), show="*")
    entry_password.place(x=190, y=210, width=181, height=31)

    entry_application = tk.Entry(add_password_window, font=("Arial", 12))
    entry_application.place(x=190, y=250, width=181, height=31)

    def toggle_password_visibility():
        if entry_password.cget('show') == '*':
            entry_password.config(show="")
            button_toggle_password.config(text="🙈")
        else:
            entry_password.config(show="*")
            button_toggle_password.config(text="👁")
        
    def generate_password(length):
        """this functions creates a random string which is suggested as password"""
        characters = string.ascii_letters + string.digits + string.punctuation #: is removed to prevent any issues in password encryption , however , it should not cause any issues
        characters = characters.replace(":","")
        password = "".join(random.choice(characters) for _ in range(length))
        return password
    
    def enter_pass(length):
        """this function enters the password into the text box"""
        password = generate_password(length)
        entry_password.delete(0,tk.END) #delete from 1st to last character to put in new password
        entry_password.insert(0,password) #inserts a new password
        return

    
    def add_to_database():
        login = entry_login.get()
        password = entry_password.get()
        application = entry_application.get()

        #place to run function for adding to db
        if application not in returnapps() and not login.strip()=="" and not password.strip() =="" and not application.strip()=="": #checks if the passwords and app is valid and then adds it to database
            write(application,login,password)
            messagebox.showinfo("Info", f"Added Login: {login}\nApplication: {application}")
        else:
            messagebox.showerror("Couldn't Add Data","The application already exists in the database or is not a valid entry")

    button_toggle_password = tk.Button(add_password_window, text="👁", font=("Arial", 10), command=toggle_password_visibility)
    button_toggle_password.place(x=380, y=210, width=20, height=30)

    button_gen_password = tk.Button(add_password_window, text="Suggest", font=("Arial", 10), command=lambda: enter_pass(12))
    button_gen_password.place(x=410, y=210, width=80, height=30)

    button_add = tk.Button(add_password_window, text="Save", font=("Arial", 12), command=add_to_database)
    button_add.place(x=400, y=280, width=100, height=40)


    add_password_window.mainloop()



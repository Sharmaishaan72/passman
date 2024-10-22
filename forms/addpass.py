import tkinter as tk
from tkinter import messagebox
from data.dbfunc import write,returnapps

def open_add_password_form():
    
    add_password_window = tk.Tk()
    add_password_window.title("Add Password")
    add_password_window.geometry("540x350")

   
    label_title = tk.Label(add_password_window, text="Add Password", font=("Arial", 12, "italic", "bold"))
    label_title.place(x=70, y=30, width=161, height=81)

 
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

    
    def add_to_database():
        login = entry_login.get()
        password = entry_password.get()
        application = entry_application.get()

        #place to run function for adding to db
        if application not in returnapps():
            write(application,login,password)
            messagebox.showinfo("Info", f"Added Login: {login}\nApplication: {application}")
        else:
            messagebox.showerror("Application already exists","The application already exists in the database , \nplease try again with a new application name\n\n\nNote: Each application name should be unique and represents a unique key")


    button_add = tk.Button(add_password_window, text="Add To Database", font=("Arial", 12), command=add_to_database)
    button_add.place(x=400, y=180, width=130, height=80)


    add_password_window.mainloop()



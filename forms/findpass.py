import tkinter as tk
from tkinter import Listbox, Scrollbar, messagebox
from data.dbfunc import returnapps,returnpass


#to create and run the search password form
def open_search_password_form():
    
    def find_password():
        app_name = entry.get()
        selected_app = listbox.get(tk.ACTIVE)

        
        if app_name:
            data = returnpass(app_name)
            messagebox.showinfo("Info", f"Searching Data for: {app_name}\n\nApp:{data['App Name']}\nLogin:{data['Login']}\nPassword:{data['Password']}")
        else:
            data = returnpass(selected_app)
            print(selected_app)
            messagebox.showinfo("Info", f"Searching Data for: {app_name}\n\nApp:{data['App Name']}\nLogin:{data['Login']}\nPassword:{data['Password']}")

    
    def switch_mode(mode):
        if mode == "entry":
            entry_frame.pack(fill=tk.X, padx=20, pady=20)
            listbox_frame.pack_forget()
        elif mode == "list":
            listbox_frame.pack(fill=tk.X, padx=20, pady=20)
            entry_frame.pack_forget()

    
    search_window = tk.Tk()
    search_window.title("Search Passwords")
    search_window.geometry("483x318")

    
    label_title = tk.Label(search_window, text="Search Passwords", font=("Arial", 16, "italic", "bold"))
    label_title.pack(pady=20)

    label_app = tk.Label(search_window, text="Choose Your Desired App:", font=("Arial", 12))
    label_app.pack()

    
    entry_frame = tk.Frame(search_window)
    entry = tk.Entry(entry_frame, font=("Arial", 12))
    entry.pack(side=tk.LEFT, padx=10)

    listbox_frame = tk.Frame(search_window)
    scrollbar = Scrollbar(listbox_frame, orient=tk.VERTICAL)
    listbox = Listbox(listbox_frame, font=("Arial", 12), yscrollcommand=scrollbar.set, height=4)

    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    for app in returnapps():
        listbox.insert(tk.END, app)

    entry_frame.pack(fill=tk.X, padx=20, pady=20)

    tool_button = tk.Button(search_window, text="Find", font=("Arial", 12), command=find_password)
    tool_button.pack(pady=20)

    button_entry_mode = tk.Button(search_window, text="Switch to Search Mode", command=lambda: switch_mode("entry"))
    button_entry_mode.pack(side=tk.LEFT, padx=20, pady=10)

    button_list_mode = tk.Button(search_window, text="Switch to List Mode", command=lambda: switch_mode("list"))
    button_list_mode.pack(side=tk.LEFT, padx=20, pady=10)

    search_window.mainloop()



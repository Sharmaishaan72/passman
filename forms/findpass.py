import tkinter as tk
from tkinter import Listbox, Scrollbar, messagebox
from data.dbfunc import returnapps,returnpass


#to create and run the search password form
def open_search_password_form():
    #handle the 'Find' button click
    def find_password():
        app_name = entry.get()
        selected_app = listbox.get(tk.ACTIVE)

        #message box with the selected app or entered app 
        if app_name:
            data = returnpass(app_name)
            messagebox.showinfo("Info", f"Searching Data for: {app_name}\n\nApp:{data['App Name']}\nLogin:{data['Login']}\nPassword:{data['Password']}")
        else:
            data = returnpass(selected_app)
            print(selected_app)
            messagebox.showinfo("Info", f"Searching Data for: {app_name}\n\nApp:{data['App Name']}\nLogin:{data['Login']}\nPassword:{data['Password']}")

    #switch between entry and listbox
    def switch_mode(mode):
        if mode == "entry":
            entry_frame.pack(fill=tk.X, padx=20, pady=20)
            listbox_frame.pack_forget()
        elif mode == "list":
            listbox_frame.pack(fill=tk.X, padx=20, pady=20)
            entry_frame.pack_forget()

    #main window
    search_window = tk.Tk()
    search_window.title("Search Passwords")
    search_window.geometry("483x318")

    #label for the form title
    label_title = tk.Label(search_window, text="Search Passwords", font=("Arial", 16, "italic", "bold"))
    label_title.pack(pady=20)

    #label and frames for app search
    label_app = tk.Label(search_window, text="Choose Your Desired App:", font=("Arial", 12))
    label_app.pack()

    #frame for the entry (app name search)
    entry_frame = tk.Frame(search_window)
    entry = tk.Entry(entry_frame, font=("Arial", 12))
    entry.pack(side=tk.LEFT, padx=10)

    #Frame for the listbox (app selection) and scrollbar
    listbox_frame = tk.Frame(search_window)
    scrollbar = Scrollbar(listbox_frame, orient=tk.VERTICAL)
    listbox = Listbox(listbox_frame, font=("Arial", 12), yscrollcommand=scrollbar.set, height=4)

    #Attach the scrollbar to the listbox
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    #Populate the listbox with dynamic app names
    for app in returnapps():
        listbox.insert(tk.END, app)

    #Initially show the entry widget
    entry_frame.pack(fill=tk.X, padx=20, pady=20)

    #Create the button to switch between search modes
    tool_button = tk.Button(search_window, text="Find", font=("Arial", 12), command=find_password)
    tool_button.pack(pady=20)

    #Create buttons to switch between entry and list modes
    button_entry_mode = tk.Button(search_window, text="Switch to Search Mode", command=lambda: switch_mode("entry"))
    button_entry_mode.pack(side=tk.LEFT, padx=20, pady=10)

    button_list_mode = tk.Button(search_window, text="Switch to List Mode", command=lambda: switch_mode("list"))
    button_list_mode.pack(side=tk.LEFT, padx=20, pady=10)

    #Start the Tkinter event loop for this window
    search_window.mainloop()



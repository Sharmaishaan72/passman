import tkinter as tk
from tkinter import Listbox, Scrollbar, messagebox
from data.dbfunc import returnapps,deletedata



def open_delete_password_form():

    def delete_password():
        selected_index = listbox.curselection()  
        if selected_index:
            selected_app = listbox.get(selected_index)
            
            messagebox.showinfo("Info", f"Deleting password for: {selected_app}")
            deletedata(selected_app)
            listbox.delete(selected_index)  
        else:
            messagebox.showwarning("Warning", "Please select an application to delete.")


    delete_window = tk.Tk()
    delete_window.title("Delete Password")
    delete_window.geometry("500x400")


    label_title = tk.Label(delete_window, text="Delete Password", font=("Arial", 16, "italic", "bold"))
    label_title.pack(pady=20)


    label_app = tk.Label(delete_window, text="Choose Your Desired App to Delete:", font=("Arial", 12))
    label_app.pack(pady=10)

    listbox_frame = tk.Frame(delete_window)
    listbox_frame.pack(pady=10)

    scrollbar = Scrollbar(listbox_frame, orient=tk.VERTICAL)
    listbox = Listbox(listbox_frame, font=("Arial", 12), yscrollcommand=scrollbar.set, height=10)


    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


    for app in returnapps():
        listbox.insert(tk.END, app)


    button_delete = tk.Button(delete_window, text="Delete", font=("Arial", 12), command=delete_password)
    button_delete.pack(pady=20)

    delete_window.mainloop()

from tkinter import *
from tkinter import messagebox
import sqlite3
from datab import *


def check_credentials():
    username = entry_username.get()
    password = entry_password.get()
    
    print(check_unm)
    if username==check_unm:
        messagebox.showinfo("app1","successful")    
    else:
        messagebox.showerror("app1","invalid username or password")
         
    
    

# Create main window
root = Tk()
root.title("Login Page")
root.attributes('-toolwindow',True)
root.resizable(0,0)


# Create username label and entry
label_username = Label(root, text="Username:")
label_username.grid(row=0,column=0,padx=20,pady=10)
entry_username = Entry(root)
entry_username.grid(row=0,column=1,padx=15,pady=10)

# Create password label and entry
label_password = Label(root, text="Password:")
label_password.grid(row=1,column=0,padx=20,pady=20)
entry_password = Entry(root, show='*')
entry_password.grid(row=1,column=1,padx=15,pady=20)

# Create login button
btn_login = Button(root, text="Login", width=10, command=check_credentials)
btn_login.grid(rowspan=1,columnspan=2)

# Start the GUI application
root.mainloop()

from tkinter import *
from tkinter import messagebox
user_credentials = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

def check_credentials():
    username = entry_username.get()
    password = entry_password.get()
    
    if username in user_credentials and user_credentials[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        entry_password.delete(0, END)  # Clear the password entry field

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

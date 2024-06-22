import tkinter as tk
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
        entry_password.delete(0, tk.END)  # Clear the password entry field

# Create main window
root = tk.Tk()
root.title("Login Page")

# Create username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=10)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Create password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=10)
entry_password = tk.Entry(root, show='*')
entry_password.pack(pady=5)

# Create login button
btn_login = tk.Button(root, text="Login", width=10, command=check_credentials)
btn_login.pack(pady=20)

# Start the GUI application
root.mainloop()
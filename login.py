from customtkinter import *
from tkinter import messagebox
import mysql.connector

# sql
mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="lmsproject"
        )
mycur=mydb.cursor()
# Define the function for the login button
def show_pass():
    if chk_password.get():
        entry_password.configure(show="")
    else:
        entry_password.configure(show="*")
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Perform login validation here
    if username=="" and password=="":
        messagebox.showwarning("LMS","please fulfill the details")
    elif len(password)>=9 or len(password)<=7:
        messagebox.showwarning("LMS","password must contains 8 letters")
        entry_password.delete(0,END)
    else:
        sql="select * from log_in_tbl where Username=%s and Password=%s"
        val=(username,password)
        mycur.execute(sql,val)
        myres=mycur.fetchone()
        if myres:
            import home
            app.destroy
            
           
            
            
        else:
            messagebox.showwarning("LMS","error")
      
        
    
    
        

# Create the main window
app = CTk()
app.title("Library Management System")
app.geometry("600x330")
app.resizable(0,0)

# Create and place the widgets
label_title = CTkLabel(app, text="Login", font=("Arial", 24))
label_title.pack(pady=10)

label_username = CTkLabel(app, text="Username:",font=("calibri",15))
label_username.pack(pady=(10, 5))
entry_username = CTkEntry(app,placeholder_text="enter the username")
entry_username.pack(pady=(0, 10), padx=20, fill="x")

label_password = CTkLabel(app, text="Password:",font=("calibri",15))
label_password.pack(pady=(10, 5))
entry_password = CTkEntry(app, show="*",placeholder_text="enter the password")
entry_password.pack(pady=(0, 20), padx=20, fill="x")
chk_password=CTkCheckBox(app,text="show Password",command=show_pass)
chk_password.pack(pady=(0, 20), padx=20)

button_login = CTkButton(app, text="Login", command=login)
button_login.pack(pady=10)

# Run the application
app.mainloop()


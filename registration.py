from customtkinter import *
from tkinter import messagebox

# Function to handle the registration submission
def register():
    firstname = entry_firstname.get()
    lastname = entry_lastname.get()
    address = entry_address.get()
    mobile_no = entry_mobile_no.get()
    email = entry_email.get()
    username = entry_username.get()
    password = entry_password.get()

    # Perform registration validation and processing here
def clear_all():
    entry_firstname.delete(0,END)
    entry_lastname.delete(0,END)
    entry_address.delete(0,END)
    entry_mobile_no.delete(0,END)
    entry_email.delete(0,END)
    entry_username.delete(0,END)
    entry_password.delete(0,END)

# Create the main window
app = CTk()
app.title("Registration Form")


# Create and place the widgets
label_title = CTkLabel(app, text="Register", font=("Arial", 24))
label_title.pack(pady=20)

label_firstname = CTkLabel(app, text="First Name:", )
label_firstname.pack(pady=(8, 5))
entry_firstname = CTkEntry(app)
entry_firstname.pack(pady=(0, 10), padx=20, fill="x")

label_lastname = CTkLabel(app, text="Last Name:")
label_lastname.pack(pady=(8, 5))
entry_lastname = CTkEntry(app)
entry_lastname.pack(pady=(0, 10), padx=20, fill="x")

label_address = CTkLabel(app, text="Address:")
label_address.pack(pady=(8, 5))
entry_address = CTkEntry(app)
entry_address.pack(pady=(0, 10), padx=20, fill="x")

label_mobile_no = CTkLabel(app, text="Mobile No:")
label_mobile_no.pack(pady=(8, 5))
entry_mobile_no = CTkEntry(app)
entry_mobile_no.pack(pady=(0, 10), padx=20, fill="x")

label_email = CTkLabel(app, text="Email:")
label_email.pack(pady=(8, 5))
entry_email = CTkEntry(app)
entry_email.pack(pady=(0, 10), padx=20, fill="x")

label_username = CTkLabel(app, text="Username:")
label_username.pack(pady=(8, 5))
entry_username = CTkEntry(app)
entry_username.pack(pady=(0, 10), padx=20, fill="x")

label_password = CTkLabel(app, text="Password:")
label_password.pack(pady=(8, 5))
entry_password = CTkEntry(app, show="*")
entry_password.pack(pady=(0, 20), padx=20, fill="x")

button_frame = CTkFrame(app)
button_frame.pack(pady=20,)

button_register = CTkButton(button_frame, text="Register", command=register)
button_register.grid(row=0, column=0, padx=10)

# Clear button
button_clear = CTkButton(button_frame, text="Clear", command=clear_all)
button_clear.grid(row=0, column=1, padx=10)

# Run the application
app.mainloop()

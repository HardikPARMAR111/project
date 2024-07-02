from tkinter import *
from tkinter import messagebox

def submit_form():
    # Retrieve the values from the entry fields
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    address = entry_address.get()
    email = entry_email.get()
    phone_number = entry_phone_number.get()
    
    # Validate if required fields are not empty
    if first_name == '' or last_name == '' or email == '':
        messagebox.showerror('Error', 'Please fill in all required fields.')
        return
    
    # Display the submitted information (for demonstration)
    messagebox.showinfo('Submitted', f'First Name: {first_name}\nLast Name: {last_name}\nAddress: {address}\nEmail: {email}\nPhone Number: {phone_number}')

# Create the main window
root = Tk()
root.title('Registration Form')
root.resizable(0,0)

# Create labels and entry fields
label_first_name = Label(root, text='First Name', fg="blue")
label_first_name.grid(row=0, column=0, padx=10, pady=5)
entry_first_name = Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)

label_last_name = Label(root, text='Last Name', fg="blue")
label_last_name.grid(row=1, column=0, padx=10, pady=5)
entry_last_name = Entry(root)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)

label_address = Label(root, text='Address', fg="blue")
label_address.grid(row=2, column=0, padx=10, pady=5)
entry_address = Entry(root)
entry_address.grid(row=2, column=1, padx=10, pady=5)

label_email = Label(root, text='Email', fg="blue")
label_email.grid(row=3, column=0, padx=10, pady=5)
entry_email = Entry(root)
entry_email.grid(row=3, column=1, padx=10, pady=5)

label_phone_number = Label(root, text='Phone Number', fg="blue")
label_phone_number.grid(row=4, column=0, padx=10, pady=5)
entry_phone_number = Entry(root)
entry_phone_number.grid(row=4, column=1, padx=10, pady=5)

label_User_name = Label(root, text='User name', fg="blue")
label_User_name.grid(row=5, column=0, padx=10, pady=5)
entry_User_name = Entry(root)
entry_User_name.grid(row=5, column=1, padx=10, pady=5)

label_password = Label(root, text='Password', fg="blue")
label_password.grid(row=6, column=0, padx=10, pady=5)
entry_password = Entry(root,show="*")
entry_password.grid(row=6, column=1, padx=10, pady=5)

# Submit button
submit_button = Button(root, text='Submit', command=submit_form, width=30, fg="white", bg="blue")
submit_button.grid(row=7, column=0, columnspan=2, pady=10)


# Start the main loop
root.mainloop()





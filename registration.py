import tkinter as tk
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
root = tk.Tk()
root.title('Registration Form')
# Create labels and entry fields
label_first_name = tk.Label(root, text='First Name')
label_first_name.grid(row=0, column=0, padx=10, pady=5)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)

label_last_name = tk.Label(root, text='Last Name')
label_last_name.grid(row=1, column=0, padx=10, pady=5)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)

label_address = tk.Label(root, text='Address')
label_address.grid(row=2, column=0, padx=10, pady=5)
entry_address = tk.Entry(root)
entry_address.grid(row=2, column=1, padx=10, pady=5)

label_email = tk.Label(root, text='Email')
label_email.grid(row=3, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1, padx=10, pady=5)

label_phone_number = tk.Label(root, text='Phone Number')
label_phone_number.grid(row=4, column=0, padx=10, pady=5)
entry_phone_number = tk.Entry(root)
entry_phone_number.grid(row=4, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text='Submit', command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)


# Start the main loop
root.mainloop()





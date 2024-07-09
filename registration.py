from tkinter import *
from tkinter import messagebox
from sqlite3 import *
from datab import sqlcon

sqlcur=sqlcon.cursor()

def submit_form():
    # Retrieve the values from the entry fields
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    address = entry_address.get()
    email = entry_email.get()
    phone_number = entry_phone_number.get()
    username=entry_User_name.get()
    password=entry_password.get()
    
    # Validate if required fields are not empty
    if first_name == '' or last_name == '' or email == '' or address=='' or phone_number=='' or username=='' or password=='':
        messagebox.showerror('Error', 'Please fill in all required fields.')
        return
    else:
        sqlcur.execute('''insert into reg_table(First_name, Last_name, Address, email, mobile_no, User_Id, Pwd) values (?,?,?,?,?,?,?)''',(first_name,last_name,address,email,phone_number,username,password))
        sqlcon.commit()
        messagebox.showinfo('App1',"data entered successfully")
    
    

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





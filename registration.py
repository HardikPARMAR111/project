from tkinter import *
from tkinter import messagebox
from datab import *

def submit_form():
    # Retrieve the values from the entry fields
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    address = entry_address.get()
    email = entry_email.get()
    phone_number = entry_phone_number.get()
    username=entry_username.get()
    password=entry_password.get()
    
    # Validate if required fields are not empty
    if first_name == '' or last_name == '' or email == '' or phone_number=='' or address=='' or username=='' or password=='':
        messagebox.showerror('Error', 'Please fill in all required fields.')
        return
    else:
        #cur.execute('''insert into reg_table(First_name, Last_name, Address, email, mobile_no, User_Id, Pwd) values(?,?,?,?,?,?,?)''',(first_name,last_name,address,email,phone_number,username,password))
        messagebox.showinfo("app1","data entered successfully")
    
    

# Create the main window
root = Tk()
root.title('Registration Form')
# Create labels and entry fields
label_first_name = Label(root, text='First Name')
label_first_name.grid(row=0, column=0, padx=10, pady=5)
entry_first_name = Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)

label_last_name = Label(root, text='Last Name')
label_last_name.grid(row=1, column=0, padx=10, pady=5)
entry_last_name = Entry(root)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)

label_address = Label(root, text='Address')
label_address.grid(row=2, column=0, padx=10, pady=5)
entry_address = Entry(root)
entry_address.grid(row=2, column=1, padx=10, pady=5)

label_email = Label(root, text='Email')
label_email.grid(row=3, column=0, padx=10, pady=5)
entry_email = Entry(root)
entry_email.grid(row=3, column=1, padx=10, pady=5)

label_phone_number = Label(root, text='Phone Number')
label_phone_number.grid(row=4, column=0, padx=10, pady=5)
entry_phone_number = Entry(root)
entry_phone_number.grid(row=4, column=1, padx=10, pady=5)

label_username= Label(root,text="username")
entry_username=Entry(root)
label_username.grid(row=5, column=0, padx=10, pady=5)
entry_username.grid(row=5, column=1, padx=10, pady=5)

label_password= Label(root,text="password")
entry_password=Entry(root)
label_password.grid(row=6, column=0, padx=10, pady=5)
entry_password.grid(row=6, column=1, padx=10, pady=5)
# Submit button
submit_button = Button(root, text='Submit', command=submit_form)
submit_button.grid(row=7, column=0, columnspan=2, pady=10)


# Start the main loop
root.mainloop()



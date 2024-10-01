import customtkinter as ctk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

# SQL connection setup
def connect_to_database():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Set your MySQL password here
            database="LMS"
        )
    except Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

# Function to fetch user profile information
# Function to fetch user profile information
# Function to fetch user profile information
# Function to fetch user profile information
def fetch_user_profile(user_id):
    db = connect_to_database()
    if db:
        mycur = db.cursor()
        mycur.execute("SELECT id, username, first_name, last_name, email, address, mobile_no FROM reg_table WHERE id = %s", (user_id,))
        profile = mycur.fetchone()
        mycur.close()
        db.close()
        return profile
    return None

# Function to display user profile
def show_user_profile(user_id):
    profile = fetch_user_profile(user_id)
    if profile:
        profile_window = ctk.CTkToplevel()
        profile_window.title("User Profile")
        profile_window.geometry("400x400")
        profile_window.configure(bg="#f0f0f0")  # Set background color

        label_title = ctk.CTkLabel(profile_window, text="User Profile", font=("Arial", 24), fg_color="#0078D4")
        label_title.pack(pady=20)

        # Create a frame for profile details
        profile_frame = ctk.CTkFrame(profile_window)
        profile_frame.pack(padx=20, pady=10, fill="both", expand=True)

        fields = ["ID", "Username", "First Name", "Last Name", "Email", "Address", "Mobile No"]
        for i, info in enumerate(profile):
            label_info = ctk.CTkLabel(profile_frame, text=f"{fields[i]}:", font=("Arial", 12, "bold"))
            label_info.grid(row=i, column=0, sticky="w", padx=5, pady=5)
            
            label_value = ctk.CTkLabel(profile_frame, text=str(info), font=("Arial", 12))
            label_value.grid(row=i, column=1, sticky="w", padx=5, pady=5)

        ctk.CTkButton(profile_window, text="Close", command=profile_window.destroy, fg_color="#FF4C4C").pack(pady=20)
    else:
        messagebox.showwarning("Profile Error", "Unable to fetch user profile information.")




# Function to fetch and display user's added books
def show_my_books(user_id):
    my_books_window = ctk.CTkToplevel()
    my_books_window.title("My Books")
    my_books_window.geometry("600x400")

    label_title = ctk.CTkLabel(my_books_window, text="My Books", font=("Arial", 24))
    label_title.pack(pady=20)

    tree = ttk.Treeview(my_books_window, columns=("ID", "Title", "Author", "Genre"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.heading("Genre", text="Genre")

    # Set column widths
    tree.column("ID", width=50)
    tree.column("Title", width=200)
    tree.column("Author", width=150)
    tree.column("Genre", width=100)

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(my_books_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(side="left", fill="both", expand=True)

    # Fetch and display books from the user's collection
    db = connect_to_database()
    if db:
        mycur = db.cursor()
        mycur.execute("SELECT b.id, b.title, b.author, b.genre FROM user_collections uc JOIN books b ON uc.book_id = b.id WHERE uc.user_id = %s", (user_id,))
        books = mycur.fetchall()

        for book in books:
            tree.insert("", "end", values=book)

        mycur.close()
        db.close()

# Function to create and display the home page
def open_home_page(user_id):
    home_app = ctk.CTk()
    home_app.title("Library Management System - Home")
    home_app.geometry("600x400")

    label_title = ctk.CTkLabel(home_app, text="Books List", font=("Arial", 24))
    label_title.pack(pady=20)

    frame = ctk.CTkFrame(home_app)
    frame.pack(fill="both", expand=True)

    button_frame = ctk.CTkFrame(frame)
    button_frame.pack(side="left", padx=10, pady=10)

    ctk.CTkButton(button_frame, text="User Profile", command=lambda: show_user_profile(user_id)).pack(pady=5)
    ctk.CTkButton(button_frame, text="My Books", command=lambda: show_my_books(user_id)).pack(pady=5)
    ctk.CTkButton(button_frame, text="Add to Collection", command=lambda: add_to_collection(user_id)).pack(pady=5)

    tree = ttk.Treeview(frame, columns=("ID", "Title", "Author", "Genre", "Available"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.heading("Genre", text="Genre")
    tree.heading("Available", text="Available")

    # Set column widths
    tree.column("ID", width=50)
    tree.column("Title", width=200)
    tree.column("Author", width=150)
    tree.column("Genre", width=100)
    tree.column("Available", width=100)

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(side="left", fill="both", expand=True)

    # Fetch and display books from the database
    db = connect_to_database()
    if db:
        mycur = db.cursor()
        mycur.execute("SELECT id, title, author, genre, available FROM books")
        books = mycur.fetchall()
        
        for book in books:
            # Map available status to "Yes" or "No"
            available_status = "Yes" if book[4] == 1 else "No"
            tree.insert("", "end", values=(book[0], book[1], book[2], book[3], available_status))

        mycur.close()
        db.close()

    # Button to add selected book to collection
# Button to add selected book to collection
    def add_to_collection(user_id):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a book to add to your collection.")
            return
        
        book_id = tree.item(selected_item)["values"][0]
        book_available = tree.item(selected_item)["values"][4]

        if book_available == 'No':
            messagebox.showwarning("Availability Error", "This book is not available.")
            return

        # Check if the book is already in the user's collection
        db = connect_to_database()
        if db:
            mycur = db.cursor()
            mycur.execute("SELECT * FROM user_collections WHERE user_id = %s AND book_id = %s", (user_id, book_id))
            exists = mycur.fetchone()
            
            if exists:
                messagebox.showwarning("Already Added", "This book is already in your collection.")
                mycur.close()
                db.close()
                return
            
            # Add the book to user's collection
            try:
                mycur.execute("INSERT INTO user_collections (user_id, book_id) VALUES (%s, %s)", (user_id, book_id))
                db.commit()

                # Update book availability
                mycur.execute("UPDATE books SET available = 0 WHERE id = %s", (book_id,))
                db.commit()

                messagebox.showinfo("Success", "Book added to your collection.")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
                db.rollback()
            finally:
                mycur.close()
                db.close()


    home_app.mainloop()

# Function for login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Input Error", "Please enter both username and password.")
        return

    db = connect_to_database()
    if db:
        mycur = db.cursor()
        mycur.execute("SELECT id, password FROM reg_table WHERE username = %s", (username,))
        result = mycur.fetchone()

        if result:
            user_id, stored_password = result
            if password == stored_password:
                app.destroy()
                open_home_page(user_id)
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

        mycur.close()
        db.close()

# Create the main login window
app = ctk.CTk()
app.title("Library Management System - Login")
app.geometry("600x330")
app.resizable(0, 0)

# Create and place the widgets for login
ctk.CTkLabel(app, text="Login", font=("Arial", 24)).pack(pady=10)
ctk.CTkLabel(app, text="Username:").pack(pady=(10, 5))
entry_username = ctk.CTkEntry(app)
entry_username.pack(pady=(0, 10), padx=20, fill="x")
ctk.CTkLabel(app, text="Password:").pack(pady=(10, 5))
entry_password = ctk.CTkEntry(app, show="*")
entry_password.pack(pady=(0, 20), padx=20, fill="x")
show_password = ctk.BooleanVar(value=False)

# Function to toggle password visibility
def toggle_password():
    if show_password.get():
        entry_password.configure(show="")
        checkbutton_show_password.configure(text="Hide Password")
    else:
        entry_password.configure(show="*")
        checkbutton_show_password.configure(text="Show Password")

# Checkbox for showing password
checkbutton_show_password = ctk.CTkCheckBox(app, text="Show Password", command=toggle_password, variable=show_password)
checkbutton_show_password.pack(pady=(0, 10))

ctk.CTkButton(app, text="Login", command=login).pack(pady=10)

# Run the application
app.mainloop()

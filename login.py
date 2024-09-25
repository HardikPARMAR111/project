import customtkinter as ctk
from tkinter import ttk, messagebox
import mysql.connector

# SQL connection setup
def connect_to_database():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Set your MySQL password here
            database="LMS"
        )
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

# Function to create and display the home page
def open_home_page(user_id):
    home_app = ctk.CTk()  # Create a new instance for the home page
    home_app.title("Library Management System - Home")
    home_app.geometry("600x400")

    label_title = ctk.CTkLabel(home_app, text="Books List", font=("Arial", 24))
    label_title.pack(pady=20)

    # Create a frame for the treeview
    frame = ctk.CTkFrame(home_app)
    frame.pack(fill="both", expand=True)

    # Create Treeview to display books
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

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(side="left", fill="both", expand=True)

    # Fetch and display books from the database
    db = connect_to_database()
    if db:
        mycur = db.cursor()
        mycur.execute("SELECT * FROM books")  # Ensure the query includes the availability status
        books = mycur.fetchall()
        
        for book in books:
            tree.insert("", "end", values=book)

        mycur.close()
        db.close()

    # Button to add selected book to collection
    def add_to_collection():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a book to add to your collection.")
            return
        
        book_id = tree.item(selected_item)["values"][0]  # Get the selected book ID

        # Add the book to user's collection
        db = connect_to_database()
        if db:
            mycur = db.cursor()
            mycur.execute("INSERT INTO user_collections (user_id, book_id) VALUES (%s, %s)", (user_id, book_id))
            db.commit()
            mycur.execute("UPDATE books SET available = 'No' WHERE id = %s", (book_id,))
            db.commit()
            messagebox.showinfo("Success", "Book added to your collection.")
            mycur.close()
            db.close()

    ctk.CTkButton(home_app, text="Add to Collection", command=add_to_collection).pack(pady=10)

    home_app.mainloop()  # Start the home page application

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
            if password == stored_password:  # Direct comparison of plain text passwords
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

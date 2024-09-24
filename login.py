from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

# SQL connection setup
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Set your MySQL password here
    database="LMS"
)
mycur = mydb.cursor()

# Function to create and display the home page
def open_home_page():
    home_app = Tk()  # Create a new instance for the home page
    home_app.title("Library Management System - Home")
    home_app.geometry("600x400")

    label_title = Label(home_app, text="Books List", font=("Arial", 24))
    label_title.pack(pady=20)

    # Create a frame for the treeview
    frame = Frame(home_app)
    frame.pack(fill="both", expand=True)

    # Create Treeview to display books
    tree = ttk.Treeview(frame, columns=("ID", "Title", "Author", "Genre"), show='headings')
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
    scrollbar = Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(side="left", fill="both", expand=True)

    # Fetch and display books from the database
    mycur.execute("SELECT * FROM books")
    books = mycur.fetchall()
    
    for book in books:
        book_id, title, author, genre = book  # Adjust according to your table structure
        tree.insert("", "end", values=(book_id, title, author, genre))

    home_app.mainloop()  # Start the home page application

# Function for login (example)
def login():
    # Placeholder for login logic
    pass

# Create the main login window (example)
app = Tk()
app.title("Library Management System - Login")
app.geometry("600x330")
app.resizable(0, 0)

# Create and place the widgets for login
Label(app, text="Login", font=("Arial", 24)).pack(pady=10)
Label(app, text="Username:").pack(pady=(10, 5))
entry_username = Entry(app)
entry_username.pack(pady=(0, 10), padx=20, fill="x")
Label(app, text="Password:").pack(pady=(10, 5))
entry_password = Entry(app, show="*")
entry_password.pack(pady=(0, 20), padx=20, fill="x")

Button(app, text="Login", command=lambda: [app.destroy(), open_home_page()]).pack(pady=10)

# Run the application
app.mainloop()

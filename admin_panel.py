import customtkinter as ctk
import mysql.connector
from tkinter import messagebox

# MySQL connection setup
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'yourpassword',  # Update this with your MySQL password
    'database': 'lms'
}

def connect_db():
    return mysql.connector.connect(**db_config)

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()

    if not title or not author or not year:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)", (title, author, int(year)))
        conn.commit()
        messagebox.showinfo("Success", "Book added successfully!")
        conn.close()
        clear_fields()
        list_books()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def delete_book():
    book_id = id_entry.get()

    if not book_id:
        messagebox.showerror("Input Error", "Please enter the book ID.")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
        conn.commit()
        messagebox.showinfo("Success", "Book deleted successfully!")
        conn.close()
        clear_fields()
        list_books()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def update_book():
    book_id = id_entry.get()
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()

    if not book_id or not title or not author or not year:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET title = %s, author = %s, year = %s WHERE id = %s", (title, author, int(year), book_id))
        conn.commit()
        messagebox.showinfo("Success", "Book updated successfully!")
        conn.close()
        clear_fields()
        list_books()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def list_books():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        conn.close()

        for row in book_list_box.get_children():
            book_list_box.delete(row)

        for row in rows:
            book_list_box.insert("", "end", values=row)
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def clear_fields():
    id_entry.delete(0, 'end')
    title_entry.delete(0, 'end')
    author_entry.delete(0, 'end')
    year_entry.delete(0, 'end')

# Create the main application window
app = ctk.CTk()
app.title("Library Management System")
app.geometry("600x400")

# Create UI components
id_label = ctk.CTkLabel(app, text="Book ID:")
id_label.pack(pady=5)
id_entry = ctk.CTkEntry(app)
id_entry.pack(pady=5)

title_label = ctk.CTkLabel(app, text="Title:")
title_label.pack(pady=5)
title_entry = ctk.CTkEntry(app)
title_entry.pack(pady=5)

author_label = ctk.CTkLabel(app, text="Author:")
author_label.pack(pady=5)
author_entry = ctk.CTkEntry(app)
author_entry.pack(pady=5)

year_label = ctk.CTkLabel(app, text="Year:")
year_label.pack(pady=5)
year_entry = ctk.CTkEntry(app)
year_entry.pack(pady=5)

add_button = ctk.CTkButton(app, text="Add Book", command=add_book)
add_button.pack(pady=5)

delete_button = ctk.CTkButton(app, text="Delete Book", command=delete_book)
delete_button.pack(pady=5)

update_button = ctk.CTkButton(app, text="Update Book", command=update_book)
update_button.pack(pady=5)

list_button = ctk.CTkButton(app, text="List Books", command=list_books)
list_button.pack(pady=5)

# Create a Treeview to display books
book_list_box = ctk.CTkScrollableFrame(app)
book_list_box.pack(pady=5, fill="both", expand=True)

tree = ctk.CTkTreeview(book_list_box, columns=("ID", "Title", "Author", "Year"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Title", text="Title")
tree.heading("Author", text="Author")
tree.heading("Year", text="Year")
tree.pack(fill="both", expand=True)

# Run the application
app.mainloop()

import mysql.connector
import customtkinter as ctk
from tkinter import messagebox, ttk

# Connect to MySQL
def create_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="lms"
    )

# Check login credentials
def authenticate(username, password):
    conn = create_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM log_in_tbl WHERE username = %s AND password = %s", 
                   (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Main Application Class
class LibraryAdminPanel(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.geometry("600x400")
        
        self.login_frame = ctk.CTkFrame(self)
        self.login_frame.pack(pady=20, fill="both", expand=True)
        
        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Username")
        self.username_entry.pack(pady=5, padx=20, fill="x")
        
        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=5, padx=20, fill="x")
        
        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.login)
        self.login_button.pack(pady=20)

        self.tree = None  # Initialize tree as None

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = authenticate(username, password)
        
        if user:
            self.login_frame.pack_forget()
            self.show_admin_panel()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    
    def show_admin_panel(self):
        self.admin_frame = ctk.CTkFrame(self)
        self.admin_frame.pack(pady=20, fill="both", expand=True)
        
        self.add_book_button = ctk.CTkButton(self.admin_frame, text="Add Book", command=self.add_book)
        self.add_book_button.pack(pady=10)
        
        self.view_books_button = ctk.CTkButton(self.admin_frame, text="View Books", command=self.view_books)
        self.view_books_button.pack(pady=10)

    def add_book(self):
        form_window = ctk.CTkToplevel(self)
        form_window.title("Add Book")
        form_window.geometry("300x250")

        form_frame = ctk.CTkFrame(form_window)
        form_frame.pack(pady=20, padx=20, fill="both", expand=True)

        title_entry = ctk.CTkEntry(form_frame, placeholder_text="Book Title")
        title_entry.pack(pady=5)

        author_entry = ctk.CTkEntry(form_frame, placeholder_text="Book Author")
        author_entry.pack(pady=5)

        genre_entry = ctk.CTkEntry(form_frame, placeholder_text="Book Genre")
        genre_entry.pack(pady=5)

        def submit_form():
            title = title_entry.get()
            author = author_entry.get()
            genre = genre_entry.get()

            if title and author and genre:
                try:
                    conn = create_db_connection()
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)", 
                                   (title, author, genre))
                    conn.commit()
                    messagebox.showinfo("Success", "Book added successfully")
                    form_window.destroy()  # Close the form window
                    if self.tree:  # Check if tree exists before refreshing
                        self.refresh_treeview()  # Refresh the book list
                except mysql.connector.Error as err:
                    messagebox.showerror("Database Error", f"Error: {err}")
                finally:
                    conn.close()
            else:
                messagebox.showwarning("Input Error", "Please fill out all fields")

        submit_button = ctk.CTkButton(form_frame, text="Add Book", command=submit_form)
        submit_button.pack(pady=20)

    def view_books(self):
        conn = create_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        
        books_window = ctk.CTkToplevel(self)
        books_window.title("Books List")
        books_window.geometry("700x400")

        frame = ctk.CTkFrame(books_window)
        frame.pack(fill="both", expand=True)
        
        self.tree = ttk.Treeview(frame, columns=("ID", "Title", "Author", "Genre", "Available"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Genre", text="Genre")
        self.tree.heading("Available", text="Available")
        
        # Set column widths
        self.tree.column("ID", width=50)
        self.tree.column("Title", width=200)
        self.tree.column("Author", width=150)
        self.tree.column("Genre", width=150)
        self.tree.column("Available", width=100)

        self.tree.pack(side="top", fill="both", expand=True)

        for book in books:
            availability = "Yes" if book["available"] else "No"
            self.tree.insert("", "end", values=(book["id"], book["title"], book["author"], book["genre"], availability))
        
        delete_button = ctk.CTkButton(books_window, text="Delete Book", command=self.delete_book)
        delete_button.pack(pady=10)

    def delete_book(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Select a Book", "Please select a book to delete.")
            return

        book_id = self.tree.item(selected_item[0], 'values')[0]  # Get the selected book ID
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this book?")
        if confirm:
            try:
                conn = create_db_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
                conn.commit()
                messagebox.showinfo("Success", "Book deleted successfully.")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                conn.close()
            self.refresh_treeview()

    def refresh_treeview(self):
        if self.tree is None:  # Ensure treeview exists
            return

        # Clear the current entries in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Reload books data and update Treeview
        try:
            conn = create_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            conn.close()

            for book in books:
                availability = "Yes" if book["available"] else "No"
                self.tree.insert("", "end", values=(book["id"], book["title"], book["author"], book["genre"], availability))
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

# Run the application
if __name__ == "__main__":
    app = LibraryAdminPanel()
    app.mainloop()

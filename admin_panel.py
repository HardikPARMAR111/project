import mysql.connector
import customtkinter as ctk
from tkinter import messagebox, ttk

from tkinter import simpledialog

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
        title = simpledialog.askstring("Book Title", "Enter the book title:")
        author = simpledialog.askstring("Book Author", "Enter the book author:")
        genre = simpledialog.askstring("Book Genre", "Enter the book genre:")
        
        if title and author and genre:
            conn = create_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)", 
                           (title, author, genre))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Book added successfully")
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields")

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
        
        # Create a Treeview widget
        self.tree = ttk.Treeview(frame, columns=("Title", "Author", "Genre","Available"), show='headings')
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Genre", text="Genre")
        self.tree.heading("Available", text="Available")
        
        self.tree.column("Title", width=200)
        self.tree.column("Author", width=150)
        self.tree.column("Genre", width=150)
        self.tree.column("Available", width=100)
    
        # Pack the Treeview and scrollbars
        self.tree.pack(side="top",fill="both", expand=True)
       
        
        # Insert book data into the Treeview
        for book in books:
            availability = "Yes" if book["available"] else "No"
            self.tree.insert("", "end", values=(book["title"], book["author"], book["genre"],availability))
        
        books_window.update_idletasks()  # Update the window with the current size and layout
        window_width = books_window.winfo_reqwidth()
        window_height = books_window.winfo_reqheight()
        books_window.geometry(f"{window_width}x{window_height}")

        for col in self.tree["columns"]:
            self.tree.column(col, width=max(self.tree.column(col, "width"), 100))

        update_button = ctk.CTkButton(books_window, text="Update Book", command=self.update_book)
        update_button.pack(pady=10)

    def update_book(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Select a Book", "Please select a book to update.")
            return

        book_id = self.tree.item(selected_item[0], 'values')[0]  # Get the selected book ID
        self.open_update_dialog(book_id)

    def open_update_dialog(self, book_id):
        conn = create_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
        book = cursor.fetchone()
        conn.close()

        # Create an update dialog
        update_dialog = ctk.CTkToplevel(self)
        update_dialog.title("Update Book")

        # Create a frame for the form
        form_frame = ctk.CTkFrame(update_dialog)
        form_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Create labels and entry widgets for book details
        ctk.CTkLabel(form_frame, text="Title:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        title_entry = ctk.CTkEntry(form_frame)
        title_entry.insert(0, book["title"])
        title_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(form_frame, text="Author:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        author_entry = ctk.CTkEntry(form_frame)
        author_entry.insert(0, book["author"])
        author_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(form_frame, text="Year:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        year_entry = ctk.CTkEntry(form_frame)
        year_entry.insert(0, book["year"])
        year_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(form_frame, text="Genre:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        genre_entry = ctk.CTkEntry(form_frame)
        genre_entry.insert(0, book["genre"])
        genre_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(form_frame, text="Available (Yes/No):").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        available_entry = ctk.CTkEntry(form_frame)
        available_entry.insert(0, "Yes" if book["available"] else "No")
        available_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        def save_changes():
            title = title_entry.get()
            author = author_entry.get()
            year = year_entry.get()
            genre = genre_entry.get()
            available = available_entry.get().strip().lower() == "yes"
            
            # Update the book in the database
            conn = create_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE books
                SET title = %s, author = %s, year = %s, genre = %s, available = %s
                WHERE id = %s
            """, (title, author, year, genre, available, book_id))
            conn.commit()
            conn.close()

            # Close the dialog and refresh the Treeview
            update_dialog.destroy()
            self.refresh_treeview()

        # Add Save button
        save_button = ctk.CTkButton(form_frame, text="Save Changes", command=save_changes)
        save_button.grid(row=5, column=1, padx=10, pady=20, sticky="e")
    def refresh_treeview(self):
        # Clear the current entries in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Reload books data and update Treeview
        conn = create_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()

        for book in books:
            availability = "Yes" if book["available"] else "No"
            self.tree.insert("", "end", values=(book["id"], book["title"], book["author"], book["year"], book["genre"], availability))

# Run the application
if __name__ == "__main__":
    app = LibraryAdminPanel()
    app.mainloop()

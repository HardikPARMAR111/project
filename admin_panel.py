import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import mysql.connector

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="lms"
    )

# Functions to interact with the database
def add_book(title, author, year):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)", (title, author, year))
    conn.commit()
    conn.close()

def add_member(first_name, last_name, address, mobile_no, email, username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reg_table (fname, lname, address, mobileno, email, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (first_name, last_name, address, mobile_no, email, username, password)
    )
    conn.commit()
    conn.close()

def delete_book(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (id,))
    conn.commit()
    conn.close()

def delete_member(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM members WHERE id = %s", (id,))
    conn.commit()
    conn.close()

# CustomTkinter GUI
class AdminPanel(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Library Admin Panel")
        self.geometry("600x500")

        # Create tabbed interface
        tabview = ctk.CTkTabview(self)
        tabview.pack(expand=True, fill='both')

        # Books tab
        books_tab = tabview.add("Books")
        self.create_books_tab(books_tab)

        # Members tab
        members_tab = tabview.add("Members")
        self.create_members_tab(members_tab)

    def create_books_tab(self, tab):
        ctk.CTkLabel(tab, text="Add a Book").pack(pady=10)
        self.book_title_entry = ctk.CTkEntry(tab, placeholder_text="Title")
        self.book_title_entry.pack(pady=5)
        self.book_author_entry = ctk.CTkEntry(tab, placeholder_text="Author")
        self.book_author_entry.pack(pady=5)
        self.book_year_entry = ctk.CTkEntry(tab, placeholder_text="Year")
        self.book_year_entry.pack(pady=5)
        add_book_button = ctk.CTkButton(tab, text="Add Book", command=self.add_book)
        add_book_button.pack(pady=10)
        
        ctk.CTkLabel(tab, text="Delete a Book (by ID)").pack(pady=10)
        self.book_id_entry = ctk.CTkEntry(tab, placeholder_text="Book ID")
        self.book_id_entry.pack(pady=5)
        delete_book_button = ctk.CTkButton(tab, text="Delete Book", command=self.delete_book)
        delete_book_button.pack(pady=10)

    def create_members_tab(self, tab):
        ctk.CTkLabel(tab, text="Add a Member").pack(pady=10)
        self.member_first_name_entry = ctk.CTkEntry(tab, placeholder_text="First Name")
        self.member_first_name_entry.pack(pady=5)
        self.member_last_name_entry = ctk.CTkEntry(tab, placeholder_text="Last Name")
        self.member_last_name_entry.pack(pady=5)
        self.member_address_entry = ctk.CTkEntry(tab, placeholder_text="Address")
        self.member_address_entry.pack(pady=5)
        self.member_mobile_no_entry = ctk.CTkEntry(tab, placeholder_text="Mobile No")
        self.member_mobile_no_entry.pack(pady=5)
        self.member_email_entry = ctk.CTkEntry(tab, placeholder_text="Email")
        self.member_email_entry.pack(pady=5)
        self.member_username_entry = ctk.CTkEntry(tab, placeholder_text="Username")
        self.member_username_entry.pack(pady=5)
        self.member_password_entry = ctk.CTkEntry(tab, placeholder_text="Password", show="*")
        self.member_password_entry.pack(pady=5)
        add_member_button = ctk.CTkButton(tab, text="Add Member", command=self.add_member)
        add_member_button.pack(pady=10)
        
        ctk.CTkLabel(tab, text="Delete a Member (by ID)").pack(pady=10)
        self.member_id_entry = ctk.CTkEntry(tab, placeholder_text="Member ID")
        self.member_id_entry.pack(pady=5)
        delete_member_button = ctk.CTkButton(tab, text="Delete Member", command=self.delete_member)
        delete_member_button.pack(pady=10)

    def add_book(self):
        title = self.book_title_entry.get()
        author = self.book_author_entry.get()
        year = self.book_year_entry.get()

        if not title or not author or not year:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return

        try:
            year = int(year)
        except ValueError:
            messagebox.showwarning("Input Error", "Year must be a number")
            return

        add_book(title, author, year)
        messagebox.showinfo("Success", "Book added successfully")

    def add_member(self):
        first_name = self.member_first_name_entry.get()
        last_name = self.member_last_name_entry.get()
        address = self.member_address_entry.get()
        mobile_no = self.member_mobile_no_entry.get()
        email = self.member_email_entry.get()
        username = self.member_username_entry.get()
        password = self.member_password_entry.get()

        if not all([first_name, last_name, address, mobile_no, email, username, password]):
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return

        # Here, you might want to add additional validation for mobile_no and email.

        add_member(first_name, last_name, address, mobile_no, email, username, password)
        messagebox.showinfo("Success", "Member added successfully")

    def delete_book(self):
        book_id = self.book_id_entry.get()

        if not book_id:
            messagebox.showwarning("Input Error", "Please enter a book ID")
            return
        
if __name__ == "__main__":
    app = AdminPanel()
    app.mainloop()

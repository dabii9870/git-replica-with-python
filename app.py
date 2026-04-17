#imports
from tkinter import *
from tkinter import messagebox
import sqlite3
#database setup
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL UNIQUE,
               phone TEXT NOT NULL UNIQUE,
               password TEXT NOT NULL
               )
               
               ''')
conn.commit()

#window creation
root = Tk()
root.title('Sign Up')
root.geometry('620x620')
root.config(bg='lightblue')


#entry fields
def numbers_only(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False

phone_number = (root.register(numbers_only), "%P")

def name_label():
    name_label = Label(root, text='Name', bg='lightblue', font=('Segoe UI', 14))
    global name_entry
    name_entry = Entry(root, font=('Segoe UI', 14))
    name_label.place(x=200, y=100 )
    name_entry.place(x=300, y=100 )
name_label()

def phone_label():
    phone_label = Label(root, text='Phone', bg='lightblue', font=('Segoe UI', 14))
    global phone_entry
    phone_entry = Entry(root, font=('Segoe UI', 14), validate='key', validatecommand=phone_number)
    phone_label.place(x=200, y=150 )
    phone_entry.place(x=300, y=150 )
phone_label()

def password_label():
    password_label = Label(root, text='Password', bg='lightblue', font=('Segoe UI', 14))
    global password_entry
    password_entry = Entry(root, font=('Segoe UI', 14), show='*')
    password_label.place(x=200, y=200 )
    password_entry.place(x=300, y=200 )
password_label()

#login and signup buttons
def create_user():
    name = name_entry.get()
    phone = phone_entry.get()
    password = password_entry.get()
    
    if not name or not phone or not password:
        messagebox.showerror("Error", "All fields are required.")
        return
    
    try:
        cursor.execute("INSERT INTO users (name, phone, password) VALUES (?, ?, ?)", (name, phone, password))
        conn.commit()
        messagebox.showinfo("Success", "User created successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Name or phone number already exists.")

signup_button = Button(root, text='Sign Up', font=('Segoe UI', 14), bg='green', fg='white', command=create_user)
signup_button.place(x=300, y=250, width=200 )


#mainloop
root.mainloop()
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


def show_login_page():
    signup_page.pack_forget()
    login_page.pack(fill='both', expand=True)
def show_sign_up_page():
    login_page.pack_forget()
    signup_page.pack(fill='both', expand=True)
#login page

login_page = Frame(root, bg="#D31B1B")


#entry fields
def numbers_only(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False

phone_number = (root.register(numbers_only), "%P")
def name_label():
    name_label = Label(login_page, text='Name', bg='lightblue', font=('Segoe UI', 14))
    global name_entry
    name_entry = Entry(login_page, font=('Segoe UI', 14))
    name_label.place(x=200, y=100 )
    name_entry.place(x=300, y=100 )
name_label()

def phone_label():
    phone_label = Label(login_page, text='Phone', bg='lightblue', font=('Segoe UI', 14))
    global phone_entry
    phone_entry = Entry(login_page, font=('Segoe UI', 14), validate='key', validatecommand=phone_number)
    phone_label.place(x=200, y=150 )
    phone_entry.place(x=300, y=150 )
phone_label()

def password_label():
    password_label = Label(login_page, text='Password', bg='lightblue', font=('Segoe UI', 14))
    global password_entry
    password_entry = Entry(login_page, font=('Segoe UI', 14), show='*')
    password_label.place(x=200, y=200 )
    password_entry.place(x=300, y=200 )
password_label()


def login_user():
    name = name_entry.get()
    phone = phone_entry.get()
    password = password_entry.get()

    cursor.execute('''SELECT * FROM users WHERE name=? AND phone=? AND password=?''', (name, phone, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Success", f"Welcome, {user[1]}!")
    else:
        messagebox.showerror("Error", "Invalid name, phone number, or password.")

signup_button = Button(login_page, text='create new account', font=('Segoe UI', 14), bg='green', fg='white', command=show_sign_up_page)
signup_button.place(x=300, y=250, width=200 )
login_button = Button(login_page, text='Login', font=('Segoe UI', 14), bg='blue', fg='white', command=login_user)
login_button.place(x=300, y=300, width=200 )
#signup page

signup_page = Frame(root, bg="#3B035C")

#entry fields
def numbers_only(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False

phone_number = (signup_page.register(numbers_only), "%P")

def name_label():
    name_label = Label(signup_page, text='Name', bg='lightblue', font=('Segoe UI', 14))
    global name_entry
    name_entry = Entry(signup_page, font=('Segoe UI', 14))
    name_label.place(x=200, y=100 )
    name_entry.place(x=300, y=100 )
name_label()

def phone_label():
    phone_label = Label(signup_page, text='Phone', bg='lightblue', font=('Segoe UI', 14))
    global phone_entry
    phone_entry = Entry(signup_page, font=('Segoe UI', 14), validate='key', validatecommand=phone_number)
    phone_label.place(x=200, y=150 )
    phone_entry.place(x=300, y=150 )
phone_label()

def password_label():
    password_label = Label(signup_page, text='Password', bg='lightblue', font=('Segoe UI', 14))
    global password_entry
    password_entry = Entry(signup_page, font=('Segoe UI', 14), show='*')
    password_label.place(x=200, y=200 )
    password_entry.place(x=300, y=200 )
password_label()
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
signup_button = Button(signup_page, text='Sign Up', font=('Segoe UI', 14), bg='green', fg='white', command=create_user)
signup_button.place(x=300, y=250, width=200 )
login_button = Button(signup_page, text='Already have an account?', font=('Segoe UI', 14), bg='blue', fg='white', command=show_login_page)
login_button.place(x=300, y=300, width=200 )


login_page.pack(fill='both', expand=True)


root.mainloop()
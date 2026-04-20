from tkinter import *

root = Tk()
root.title('Learning Frames')
root.geometry('400x400')
#page 1

def show_login_page():
    signup_page.pack_forget()
    login_page.pack(fill='both', expand=True)
def show_sign_up_page():
    login_page.pack_forget()
    signup_page.pack(fill='both', expand=True)

login_page = Frame(root, bg="#D31B1B")
label = Label(login_page, text='login page')
button1 = Button(login_page, text='go to sign up page', command=show_sign_up_page)
label.pack()
button1.pack()


signup_page = Frame(root, bg="#3B035C")
label1 = Label(signup_page, text='signup page')
button2 = Button(signup_page, text='go to login page', command=show_login_page)
label1.pack()
button2.pack()


login_page.pack(fill='both', expand=True)


root.mainloop()
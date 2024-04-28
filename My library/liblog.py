from tkinter import *

import tkinter as tk
from tkinter import messagebox
import pymysql
#------------------------------------------FULL SCREEN------------------------------------------------------------------


def forgot_page():
    win.destroy()
    import libfor

def signup_page():
    win.destroy()
    import libreg

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)
        passwordEntry.config(show='*')

def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def hide():
    openeye.config(file='ceyeh.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='opens.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def login_btn():
    q=usernameEntry.get()
    if usernameEntry.get() == '' and passwordEntry.get() == '':
        messagebox.showerror("error!", "FILL THE  ALL DETAILS")
    elif usernameEntry.get() == '':
        messagebox.showerror("error!", "FILL THE  USERNAME")
    elif passwordEntry.get() == '':
        messagebox.showerror("error!", "FILL THE  PASSWORD")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="bgmi", database="library")
            curr = conn.cursor()
        except:
            messagebox.showerror("error!", "DATABASE CONNECTIVITY ISSUE, PLEASE TRY AGAIN")
            return
        curr.execute("select * from library where username=%s and password=%s",
                     (usernameEntry.get(), passwordEntry.get()))
        row = curr.fetchone()

        if row == None:
            messagebox.showerror("Error!", "Enter correct username and password")
            conn.commit()
            conn.close()
            clear_data()
        else:
            messagebox.showinfo("Info!", "successfully Login..")
            conn.commit()
            conn.close()
            clear_data()

            with open("libraryuser.txt", 'w') as f:
                f.write(q)
            win.destroy()
            import libraryfinal

def clear_data():
    user.set('')
    pw.set('')



win = tk.Tk()
win.geometry("400x650+600+50")
win.title("sohan's Iphone")
win.resizable(0, 0)

domino_logo = PhotoImage(file='iphone-frame-clipart-31.png')
dmLabel = Label(win, image=domino_logo)
dmLabel.place(x=38, y=0)
lib = Button(win, text='Library !', font=('Open Sans', 16, 'bold'), fg='white', bg='green',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=19)
lib.place(x=73, y=90)
heading = Label(win, text='USER LOGIN', font=('Microsoft Yeahei UI Light', 23, 'bold'), bg='white',
                fg='firebrick1')
heading.place(x=100, y=180)
desLabel = Label(win, text=' -----------------------------', font=('Open Sans', 16), fg='black',
                bg='white')
desLabel.place(x=90, y=215)
user = tk.StringVar()
pw = tk.StringVar()


usernameEntry = Entry(win, width=20, font=('Microsoft Yeahei UI Light', 11, 'bold'), bd=0, fg='firebrick1',textvariable=user)
usernameEntry.place(x=90, y=280)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1 = Frame(win, width=235, height=2,bg='black')
frame1.place(x=80, y=310)

passwordEntry = Entry(win, width=25, font=('Microsoft Yeahei UI Light', 11, 'bold'), bd=0, fg='firebrick1',textvariable=pw)
passwordEntry.place(x=90, y=340)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>',password_enter)
frame2 = Frame(win, width=235, height=2,bg='black')
frame2.place(x=80, y=370)

openeye = PhotoImage(file='opens.png')
eyeButton = Button(win, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                   command=hide)
eyeButton.place(x=290, y=345)

forgetButton = Button(win, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2',
                      font=('Microsoft Yeahei UI Light', 9, 'bold'), fg='firebrick1', activeforeground='firebrick1',command=forgot_page)
forgetButton.place(x=200, y=380)

loginButton = Button(win, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15,command=login_btn)
loginButton.place(x=100, y=420)


signupLabel = Label(win, text="Don't have an account?", font=('Open Sans', 10), fg='firebrick1', bg='white')
signupLabel.place(x=80, y=490)

newaccountButton = Button(win, text='Create New One', font=('Open Sans', 10, 'bold underline'), fg='blue',
                          bg='white', activeforeground='blue', activebackground='white', cursor='hand2', bd=0,command=signup_page)
newaccountButton.place(x=210, y=520)

frame = Frame(win, width=80, height=2,bg='black')
frame.place(x=160, y=590)

win.mainloop()
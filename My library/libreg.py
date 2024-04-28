
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pymysql


win1 = tk.Tk()
win1.geometry("400x650+600+50")
win1.title("sohan's Iphone")
win1.resizable(0, 0)
domino_logo = PhotoImage(file='iphone-frame-clipart-31.png')
dmLabel = Label(win1, image=domino_logo)
dmLabel.place(x=38, y=0)

email = tk.StringVar()
username = tk.StringVar()
password = tk.StringVar()
cpassword = tk.StringVar()

def connect_database():
    b = email_en.get()
    r = b[int(len(b)) - 10: int(len(b))]
    a= pw_en.get()
    o = int(len(a))
    b= cpw_en.get()
    if email_en.get() == '' and user_en.get() == '' and pw_en.get() == '' and cpw_en.get() == '':
        messagebox.showerror("error!", "FILL THE  ALL DETAILS")
    elif email_en.get() == '':
        messagebox.showerror("error!","FILL THE  EMAIL-ID")
    elif r != "@gmail.com":
        messagebox.showerror("Error!", "ENTER CORRECT EMAIL-ID")
    elif user_en.get() == '':
        messagebox.showerror("error!","FILL THE  USERNAME")
    elif pw_en.get() == '' :
        messagebox.showerror("error!","FILL THE  PASSWORD")
    elif cpw_en.get() == '':
        messagebox.showerror("error!","FILL THE  CONFORM PASSWORD")
    elif o < 6:
        messagebox.showerror("error!", "REQUIRED MAXIMUM 6 CHARACTER PASSWORD")
    elif a != b :
        messagebox.showerror("error!", "PASSWORD AND CONFORM PASSWORD NOT MATCH...")

    elif check.get() == 0:
        messagebox.showerror("error!", "ACEEPT THE ALL TERMS AND CONDITION")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="bgmi", database="library")
            curr = conn.cursor()
        except:
            messagebox.showerror("error!", "DATABASE CONNECTIVITY ISSUE, PLEASE TRY AGAIN")
            return
        curr.execute("select * from library where email=%s", (email_en.get()))
        row = curr.fetchone()
        curr.execute("select * from library where username=%s", (user_en.get()))
        raw = curr.fetchone()
        if row != None:
            messagebox.showerror("Error!", "This emial-id is already exist")

        elif raw != None:
            messagebox.showerror("Error!", "This username is already exist")
        else:
            curr.execute("INSERT INTO library(email,username,password) VALUES(%s,%s,%s) ",
                         (email_en.get(), user_en.get(), pw_en.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Info!", "Registration is successful")
            clear_data()

            win1.destroy()
            import liblog

def clear_data():
    email.set('')
    username.set('')
    password.set('')
    cpassword.set('')

def login_page():
    win1.destroy()
    import liblog
lib = Button(win1, text='Library !', font=('Open Sans', 16, 'bold'), fg='white', bg='green',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=19)
lib.place(x=73, y=90)
heading = Label(win1, text='CREATE ACCOUNT', font=('Microsoft Yeahei UI Light', 16, 'bold'), bg='white',fg='firebrick1')
heading.place(x=100, y=145)
dLabel = Label(win1, text=' ----------------------------------', font=('Open Sans', 16), fg='black',bg='white')
dLabel.place(x=70, y=170)

email_lb = Label(win1,text='Email',font=('Microsoft Yeahei UI Light', 10, 'bold'),fg='firebrick1',bg='white')
email_lb.place(x=80, y=195)
email_en = Entry(win1, width=30, font=('Microsoft Yeahei UI Light', 11, 'bold'), bd=0,bg='firebrick1', fg='white',textvariable=email)
email_en.place(x=79, y=225)

user_lb = Label(win1,text='Username',font=('Microsoft Yeahei UI Light', 10, 'bold'),fg='firebrick1',bg='white')
user_lb.place(x=80, y=255)
user_en = Entry(win1, width=30, font=('Microsoft Yeahei UI Light', 11, 'bold'), bd=0,bg='firebrick1', fg='white',textvariable=username)
user_en.place(x=79, y=285)

pw_lb = Label(win1,text='Password',font=('Microsoft Yeahei UI Light', 10, 'bold'),fg='firebrick1',bg='white')
pw_lb.place(x=80, y=315)
pw_en = Entry(win1, width=30, font=('Microsoft Yeahei UI Light', 11, 'bold'), bd=0,bg='firebrick1', fg='white',textvariable=password)
pw_en.place(x=79, y=345)

cpw_lb = Label(win1,text='Conform Password',font=('Microsoft Yeahei UI Light', 10, 'bold'),fg='firebrick1',bg='white')
cpw_lb.place(x=80, y=375)
cpw_en = Entry(win1, width=30, font=('Microsoft Yeahei UI Light', 11, 'bold'), bd=0,bg='firebrick1', fg='white',textvariable=cpassword)
cpw_en.place(x=79, y=405)
check = IntVar()

con=Checkbutton(win1,text='I agree to the terms & condition',font=('Microsoft Yeahei UI Light', 10, 'bold'), bd=0,bg='white',cursor='hand2', fg='firebrick1',variable=check)
con.place(x=75, y=440)

signupButton = Button(win1, text='Signup', font=('Open Sans', 15, 'bold'), fg='white', bg='firebrick1',
       activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15,command=connect_database)
signupButton.place(x=105,y=475)

signupLabel = Label(win1, text="you have an account ?", font=('Open Sans', 11), fg='firebrick1', bg='white')
signupLabel.place(x=80, y=520)

newaccountButton = Button(win1, text='Log in', font=('Open Sans', 11, 'bold underline'), fg='blue',bg='white',
                          activeforeground='blue', activebackground='white', cursor='hand2', bd=0,command=login_page)
newaccountButton.place(x=260, y=540)

frame = Frame(win1, width=80, height=2,bg='black')
frame.place(x=160, y=590)

win1.mainloop()
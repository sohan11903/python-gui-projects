from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pymysql


def hide():
    openeye.config(file='ceyeh.png')
    pw_en.config(show='*')
    eyeButton.config(command=show)
def show():
    openeye.config(file='opens.png')
    pw_en.config(show='')
    eyeButton.config(command=hide)

def hide1():
    openeye1.config(file='ceyeh1.png')
    cpw_en.config(show='*')
    eyeButton1.config(command=show1)
def show1():
    openeye1.config(file='opens1.png')
    cpw_en.config(show='')
    eyeButton1.config(command=hide1)

def clear_data():
    username.set('')
    password.set('')
    cpassword.set('')

def forgot():
    a = pw_en.get()
    o = int(len(a))
    b = cpw_en.get()
    if  user_en.get() == '' and pw_en.get() == '' and cpw_en.get() == '':
        messagebox.showerror("error!", "FILL THE  ALL DETAILS")
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
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="bgmi", database="library")
            curr = conn.cursor()
        except:
            messagebox.showerror("error!", "DATABASE CONNECTIVITY ISSUE, PLEASE TRY AGAIN")
            return

        curr.execute("select * from library where username=%s", (user_en.get()))
        raw = curr.fetchone()
        if raw == None:
            messagebox.showerror("Error!", "Wrong username")
            clear_data()
        else:

            curr.execute("update library set password=%s where username=%s",
                             (pw_en.get(), user_en.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Info!", "Suceesfully Password Reset, Login With New Password")

            win2.destroy()
            import liblog

win2 = Tk()
win2.geometry('400x650+600+50')
win2.resizable(0, 0)
win2.title('forgot page')
domino_logo = PhotoImage(file='iphone-frame-clipart-31.png')
dmLabel = Label(win2, image=domino_logo)

dmLabel.place(x=38, y=0)
lib = Button(win2, text='Library !', font=('Open Sans', 16, 'bold'), fg='white', bg='green',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=19)
lib.place(x=73, y=90)
heading = Label(win2, text='RESET PASSWORD', font=('Microsoft Yeahei UI Light', 18, 'bold'), bg='white',fg='firebrick1')
heading.place(x=80, y=165)
dLabel = Label(win2, text=' ----------------------------------', font=('Open Sans', 16), fg='black',bg='white')
dLabel.place(x=70, y=192)

username = tk.StringVar()
password = tk.StringVar()
cpassword = tk.StringVar()

user_lb = Label(win2,text='Username',font=('Microsoft Yeahei UI Light', 10, 'bold'),fg='firebrick1',bg='white')
user_lb.place(x=80, y=230)
user_en = Entry(win2, width=30, font=('Microsoft Yeahei UI Light', 11, 'bold'), bd=0, fg='black',textvariable=username)
user_en.place(x=80, y=260)
frame1 = Frame(win2, width=240, height=2,bg='black')
frame1.place(x=80, y=285)

pw_lb = Label(win2,text='Password',font=('Microsoft Yeahei UI Light', 10, 'bold'),fg='firebrick1',bg='white')
pw_lb.place(x=80, y=310)
pw_en = Entry(win2, width=30, font=('Microsoft Yeahei UI Light', 11, 'bold'), bd=0, fg='black',textvariable=password)
pw_en.place(x=80, y=340)
frame2 = Frame(win2, width=240, height=2,bg='black')
frame2.place(x=80, y=365)

cpw_lb = Label(win2,text='Confirm Password',font=('Microsoft Yeahei UI Light', 10, 'bold'),fg='firebrick1',bg='white')
cpw_lb.place(x=80, y=390)
cpw_en = Entry(win2, width=30, font=('Microsoft Yeahei UI Light', 11, 'bold'), bd=0, fg='black',textvariable=cpassword)
cpw_en.place(x=80, y=420)
frame3 = Frame(win2, width=240, height=2,bg='black')
frame3.place(x=80, y=445)

openeye = PhotoImage(file='opens.png')
eyeButton = Button(win2, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',command=hide)
eyeButton.place(x=290, y=340)

openeye1 = PhotoImage(file='opens1.png')
eyeButton1 = Button(win2, image=openeye1, bd=0, bg='white', activebackground='white', cursor='hand2',command=hide1)
eyeButton1.place(x=290, y=420)

signupButton = Button(win2, text='Submit', font=('Open Sans', 15, 'bold'), fg='white', bg='firebrick1',
                activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=20,command=forgot)
signupButton.place(x=76,y=500)

frame = Frame(win2, width=80, height=2,bg='black')
frame.place(x=160, y=690)
win2.mainloop()
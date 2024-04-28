from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from liblog import usernameEntry
import pymysql

win3 = tk.Tk()
win3.resizable(0,0)
win3.geometry("400x650+600+50")
win3.title("your notes")

domino_logo = PhotoImage(file='iphone-frame-clipart-31.png')
dmLabel = Label(win3, image=domino_logo)
dmLabel.place(x=38, y=0)



#---------------------------------------------------------function------------------------------------------------------

def add():

    if user_en.get() == '':
        messagebox.showerror("error!", "FILL THE NOTE")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="bgmi", database="library")
            curr = conn.cursor()
        except:
            messagebox.showerror("error!", "DATABASE CONNECTIVITY ISSUE, PLEASE TRY AGAIN")
            return
        with open('libraryuser.txt') as f:
            highscore = str(f.read())
        curr.execute("INSERT INTO library1(username,name,author,type) VALUES(%s,%s,%s,%s) ",
                         (highscore,name.get(),author.get(),type.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Info!", "Book Add Successfully !")
        fetch_data()
        clear_data()


def clear_data():
    name.set('')
    author.set('')
    type.set('')

def fetch_data():
    with open('libraryuser.txt') as f:
        highscore = str(f.read())
    conn = pymysql.connect(host="localhost", user="root", password="bgmi", database="library")
    curr = conn.cursor()
    curr.execute("select name,author,type from library1 where username "+ " LIKE '%" + str(highscore) + "%'")
    rows = curr.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',tk.END,values=row)
        conn.commit()
        conn.close()
def get_cursor(Event):
    current_row = student_table.focus()
    content = student_table.item(current_row)
    row = content['values']
    name.set(row[0])
    author.set(row[1])
    type.set(row[2])
def search():
    conn = pymysql.connect(host="localhost", user="root", password="bgmi", database="library")
    curr = conn.cursor()
    if str(searchtxt.get()) != "":
        curr.execute("select name,author,type from library1 where " + str(searchby.get()) + " LIKE '%" + str(searchtxt.get()) + "%'")

        rows = curr.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('', tk.END, values=row)
            conn.commit()
            conn.close()
    else:
        curr.execute("select "+str(searchby.get())+" from library1 " )
        rows = curr.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('', tk.END, values=row)
            conn.commit()
            conn.close()


def showall():
    fetch_data()
#------------------------------------------------------------------------------------------------------------------------
lib = Button(win3, text='My Library!', font=('Open Sans', 16, 'bold'), fg='white', bg='green',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=19)
lib.place(x=73, y=80)

mainframe = tk.Frame(win3,width=700,height=500,bg='lightgrey')
mainframe.place(x=75,y=140,height=160,width=250)

login_lbl = tk.Label(mainframe, text="Name:-", font=("Arial", 13 , 'bold'),bg="lightgrey")
login_lbl.place(x=2,y=10)

name = tk.StringVar()
author = tk.StringVar()
type = StringVar()
searchby=tk.StringVar()
searchtxt=tk.StringVar()

user_en = tk.Entry(mainframe, width=30, font=('Microsoft Yeahei UI Light', 11, 'bold'), bd=0,bg="lightgrey", fg='black'
                   ,textvariable=name)
user_en.place(x=74,y=10)
frame1 = tk.Frame(mainframe, width=172, height=2,bg='black')
frame1.place(x=74, y=30)

login_lbl1 = tk.Label(mainframe, text="Author:-", font=("Arial", 13 , 'bold'),bg="lightgrey")
login_lbl1.place(x=2,y=40)
user_en1 = tk.Entry(mainframe, width=30, font=('Microsoft Yeahei UI Light', 11, 'bold'), bd=0,bg="lightgrey", fg='black'
                   ,textvariable=author)
user_en1.place(x=74,y=40)
frame1 = tk.Frame(mainframe, width=172, height=2,bg='black')
frame1.place(x=74, y=60)

login_lbl2 = tk.Label(mainframe, text="Type:-", font=("Arial", 13 , 'bold'),bg="lightgrey")
login_lbl2.place(x=2,y=70)
user_en2 = tk.Entry(mainframe, width=30, font=('Microsoft Yeahei UI Light', 11, 'bold'), bd=0,bg="lightgrey", fg='black'
                   ,textvariable=type)
user_en2.place(x=74,y=70)
frame2 = tk.Frame(mainframe, width=172, height=2,bg='black')
frame2.place(x=74, y=90)
addButton = tk.Button(mainframe, text='Add Book', font=('Open Sans', 13, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=9,command=add)
addButton.place(x=75,y=120)


dLabel = Label(win3, text='------------------------------------', font=('Open Sans', 16), fg='black',bg='white')
dLabel.place(x=71, y=300)
#----------------------------------------------------------------------------------------------------------------------------

frame = Frame(win3, width=80, height=2,bg='black')
frame.place(x=160, y=590)



search_frame = tk.Frame(win3,width=700,height=780,bg='pink')
search_frame.place(x=75,y=330,height=255,width=250)

search_lbl = tk.Label(search_frame, text="Search ", font=("Arial", 8, "bold"))
search_lbl.place(x=8,y=10)

search_in = ttk.Combobox(search_frame, font=("Arial", 8),width=10, state="readonly",textvariable=searchby)
search_in['values'] = ("name", "author", "type")
search_in.place(x=60,y=10)

searchtxt_ent = tk.Entry(search_frame, bd=1,width=13, font=("Arial", 10),textvariable=searchtxt)
searchtxt_ent.place(x=150,y=10)

search_btn = tk.Button(search_frame, bd=1, text="Search", font=("Arial", 8, "bold"),command=search)
search_btn.place(x=70,y=34)

showall_btn = tk.Button(search_frame, bd=1, text="Show All", font=("Arial", 8, "bold"),command=showall)
showall_btn.place(x=140,y=34)
#-------------------------------------------------END-------------------------------------------------------------------

search1_frame = tk.Frame(win3,width=700,height=0,bg='red')
search1_frame.place(x=75,y=390,height=195,width=250)
main_frame = tk.Frame(search1_frame, bd=7, bg="lightgrey", relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)
y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL,width=11)

x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL,width=11)


student_table = ttk.Treeview(main_frame, columns=("name", "author", "type"),
                             yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)


student_table.heading("name", text="name")
student_table.heading("author", text="author")
student_table.heading("type", text="type")


student_table['show'] = ('headings')

student_table.column("name", width=70)
student_table.column("author", width=70)
student_table.column("type", width=70)


student_table.pack(fill=tk.BOTH, expand=True)
fetch_data()
student_table.bind("<ButtonRelease-1>",get_cursor)
#--------------------------MAIN DATA--------------------------------------------------------------

win3.mainloop()


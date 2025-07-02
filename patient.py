from tkinter import *
import sqlite3
from tkinter import messagebox

import os
from PIL import ImageTk, Image
root = Tk()
root.geometry('1366x768')
root.title("Registration Form")
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back2.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
Fullname = StringVar()
Email = StringVar()
Contact = StringVar()
Un = StringVar()
Pw = StringVar()

def cancel():
    root.destroy()
    os.system('python Patientlogin.py')

def database():
    name1 = Fullname.get()
    email = Email.get()
    contact = Contact.get()
    un = Un.get()
    pw = Pw.get()

    if name1=="":
        messagebox.showinfo("Healthcare","Enter Name")
    else:
        if email == "":
            messagebox.showinfo("Healthcare","Enter Email")
        else:
             conn = sqlite3.connect('Form.db')
             with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM register")
                rows = cursor.fetchall()
                for row in rows:
                    dbuser = row[0]

                    ph1 = row[1]
                if dbuser == name1 and email == ph1:
                    messagebox.showinfo("Healthcare", "Already Exist")
                else:
                    cursor.execute(
                    'CREATE TABLE IF NOT EXISTS register (Fullname TEXT,Email TEXT,Contact TEXT,Un TEXT,Pw TEXT)')
                    cursor.execute('INSERT INTO register (FullName,Email,Contact,Un,Pw) VALUES(?,?,?,?,?)',
                    (name1, email, contact, un, pw,))
                    conn.commit()
                    messagebox.showinfo("Healthcare","Record Saved")


label_0 = Label(root, justify=LEFT, bg='brown', text="Registration Here..", width=15, font=("bold", 20))
label_0.place(x=100, y=150)


label_1 = Label(root, text="FullName", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_1.place(x=100, y=300)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=300, y=300)

label_2 = Label(root, text="Email", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_2.place(x=100, y=350)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=300, y=350)

label_3 = Label(root, text="Contact",bg='white',justify=LEFT, width=20, font=("bold", 10))
label_3.place(x=100, y=400)

entry_3 = Entry(root, textvar=Contact)
entry_3.place(x=300, y=400)

label_4 = Label(root, text="Username", bg='white',justify=LEFT, width=20, font=("bold", 10))
label_4.place(x=100, y=450)

entry_5 = Entry(root, textvar=Un)
entry_5.place(x=300, y=450)

label_5 = Label(root, text="Password",bg='white', justify=LEFT, width=20, font=("bold", 10))
label_5.place(x=100, y=500)

entry_6 = Entry(root, textvar=Pw)
entry_6.place(x=300, y=500)

Button(root, text='Submit', width=20,height=2, bg='brown', fg='white', command=database).place(x=300, y=600)
Button(root, text='Cancel', width=20, height=2,bg='brown', fg='white', command=cancel).place(x=450, y=600)


root.mainloop()

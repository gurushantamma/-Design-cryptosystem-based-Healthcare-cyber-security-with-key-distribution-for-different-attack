from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
import image
import os
from PIL import ImageTk, Image

root = Tk()
root.geometry('1366x768')
root.title("Registration Form")
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back2.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1, 1, anchor=NW, image=photo)
Fullname = StringVar()
Email = StringVar()
Contact = StringVar()
Un = StringVar()
Pw = StringVar()
Age = StringVar()
Gkey = StringVar()
Faceimg = StringVar()


def cancel():
    root.destroy()



def gkey():
    import random

    print(random.randint(0, 100))
    xxx=random.randint(0, 100)
    Gkey.set(xxx)

def database():
    name1 = Fullname.get()
    email = Email.get()
    contact = Contact.get()

    l = len(contact)

    un = Un.get()
    pw = Pw.get()
    age = Age.get()
    gkey = Gkey.get()
    faceimg = Faceimg.get()
    status = "-"
    if name1 == "":
        messagebox.showinfo("BLockChain", "Enter Name")

    else:
        if email == "":
            messagebox.showinfo("BLockChain", "Enter Email")
        else:
            if contact == "":
                messagebox.showinfo("BLockChain", "Enter Contact")
            else:

                    if un == "":
                        messagebox.showinfo("BLockChain", "Username")
                    else:
                        if pw == "":
                            messagebox.showinfo("BLockChain", "Enter Password")
                        else:
                            if not (re.search(regex, email)):
                                messagebox.showinfo("BLockChain", "Enter valid Email")
                            else:
                                if l != 10:
                                    messagebox.showinfo("BLockChain", "Enter 10 digits only")
                                else:
                                    if not name1.isalpha():
                                        messagebox.showinfo("BLockChain", "Enter Name in alphabets Only ")
                                    else:




                                                    conn = sqlite3.connect('form.db')
                                                    with conn:
                                                            cursor = conn.cursor()

                                                            cursor.execute(
                                                                'CREATE TABLE IF NOT EXISTS doctor (Fullname TEXT,Email TEXT,Contact TEXT,Un TEXT,Pw TEXT,Age TEXT,Status TEXT,Gkey TEXT,Faceimg TEXT)')
                                                            cursor.execute('INSERT INTO doctor (FullName,Email,Contact,Un,Pw,Age,Status,Gkey,Faceimg) VALUES(?,?,?,?,?,?,?,?,?)',
                                                                (name1, email, contact, un, pw, age, status, gkey, faceimg,))

                                                            conn.commit()
                                                            messagebox.showinfo("BLockChain", "Record Saved")



def open_File():
    faceimg = askopenfilename(filetypes=[(".jpg", "*.jpg")])
    Faceimg.set(faceimg)
    fm = Faceimg.get()
    load = Image.open(fm)
    render = ImageTk.PhotoImage(load)

    # labels can be text or images
    img = Label(root, image=render)
    img.image = render
    img.place(x=600, y=300)


label_0 = Label(root, justify=LEFT, bg='white', text="Doctor Details", width=15, font=("bold", 20))
label_0.place(x=50, y=200)

label_1 = Label(root, text="FullName  Dr.", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_1.place(x=300, y=250)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=450, y=250)

label_2 = Label(root, text="Email", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_2.place(x=300, y=300)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=450, y=300)

label_3 = Label(root, text="Contact", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_3.place(x=300, y=350)

entry_3 = Entry(root, textvar=Contact)
entry_3.place(x=450, y=350)

label_4 = Label(root, text="Username", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_4.place(x=300, y=400)

entry_5 = Entry(root, textvar=Un)
entry_5.place(x=450, y=400)

label_5 = Label(root, text="Password", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_5.place(x=300, y=450)

entry_6 = Entry(root, textvar=Pw)
entry_6.place(x=450, y=450)

label_7 = Label(root, text="Specialist", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_7.place(x=300, y=500)

entry_7 = Entry(root, textvar=Age)
entry_7.place(x=450, y=500)

label_8 = Label(root, text="Permission Key", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_8.place(x=300, y=550)

entry_8 = Entry(root, textvar=Gkey)
entry_8.place(x=450, y=550)

label_7 = Label(root, text="Photo", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_7.place(x=300, y=600)

entry_7 = Entry(root, textvar=Faceimg)
entry_7.place(x=450, y=600)

Button(root, text='Generate Public Key', width=20,  bg='red', fg='white', command=gkey).place(x=600, y=550)
Button(root, text='Submit', width=10, bg='gray', fg='white', command=database).place(x=450, y=600)
Button(root, text='Cancel', width=10, bg='gray', fg='white', command=cancel).place(x=530, y=600)
Button(root, text='Browse Photo', width=20, bg='gray', fg='white', command=open_File).place(x=300, y=600)

root.mainloop()

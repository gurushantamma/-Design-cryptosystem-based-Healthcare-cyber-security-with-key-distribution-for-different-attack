
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
img = Image.open('back1.jpg')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
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
    os.system('python Main.py')

def gkey():
    root.destroy()
    os.system('python encr.py')

def database():
    name1 = Fullname.get()
    email = Email.get()
    contact = Contact.get()

    l=len(contact)


    un = Un.get()
    pw = Pw.get()
    age= Age.get()
    gkey = Gkey.get()
    faceimg = Faceimg.get()
    status="-"

    if name1=="":
        messagebox.showinfo("ECC","Enter Name")
    else:
        if email == "":
            messagebox.showinfo("ECC","Enter Email")
        else:
            if contact == "":
                messagebox.showinfo("ECC", "Enter Contact")
            else:

                    if un == "":
                        messagebox.showinfo("ECC", "Username")
                    else:
                        if pw == "":
                         messagebox.showinfo("ECC", "Enter Password")
                        else:
                            if not (re.search(regex, email)):
                                messagebox.showinfo("ECC", "Enter valid Email")
                            else:
                                if l != 10:
                                    messagebox.showinfo("ECC", "Enter 10 digits only")
                                else:
                                    if  not name1.isalpha():
                                        messagebox.showinfo("ECC", "Enter Name in alphabets Only ")
                                    else:




                                                conn = sqlite3.connect('form.db')
                                                with conn:
                                                    cursor = conn.cursor()
                                                    cursor.execute("SELECT * FROM register")
                                                    rows = cursor.fetchall()
                                                    for row in rows:
                                                        dbuser = row[0]
                                                       
                                                        ph1 = row[1]
                                                    if dbuser == name1 and email == ph1:
                                                        messagebox.showinfo("ECC", "Already Registered")
                                                    else:
                                                        cursor.execute(
                                                        'CREATE TABLE IF NOT EXISTS register (Fullname TEXT,Email TEXT,Contact TEXT,Un TEXT,Pw TEXT)')
                                                        cursor.execute('INSERT INTO register (FullName,Email,Contact,Un,Pw) VALUES(?,?,?,?,?)',
                                                        (name1, email, contact, un, pw))



                                                        conn.commit()

                                                        messagebox.showinfo("ECC","Record Saved")





label_0 = Label(root, justify=LEFT, bg='white', text="Register Here..", width=20, font=("bold", 15))
label_0.place(x=1000, y=200)


label_1 = Label(root, text="FullName", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_1.place(x=1000, y=350)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=1150, y=350)

label_2 = Label(root, text="Email", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_2.place(x=1000, y=400)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=1150, y=400)

label_3 = Label(root, text="Contact",bg='white',justify=LEFT, width=20, font=("bold", 10))
label_3.place(x=1000, y=450)

entry_3 = Entry(root, textvar=Contact)
entry_3.place(x=1150, y=450)

label_4 = Label(root, text="Username", bg='white',justify=LEFT, width=20, font=("bold", 10))
label_4.place(x=1000, y=500)

entry_5 = Entry(root, textvar=Un)
entry_5.place(x=1150, y=500)

label_5 = Label(root, text="Password",bg='white', justify=LEFT, width=20, font=("bold", 10))
label_5.place(x=1000, y=550)

entry_6 = Entry(root, textvar=Pw)
entry_6.place(x=1150, y=550)


Button(root, text='Submit', width=10, bg='gray', fg='white', command=database).place(x=1100, y=600)
Button(root, text='Cancel', width=10, bg='gray', fg='white', command=cancel).place(x=1180, y=600)

root.mainloop()

from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import re
from cryptography.fernet import Fernet



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
Ht = StringVar()
Wt = StringVar()
Bp = StringVar()
temp = StringVar()
Hr = StringVar()
Sympt= StringVar()
Dn=StringVar()
def cancel():
    root.destroy()
def gkey():
    import random
    zzz=random.randint(0, 100)
    print(random.randint(0, 100))
    Gkey.set(zzz)

def database():
    fullname1 = Fullname.get()
    email = Email.get()
    contact = Contact.get()

    l = len(contact)

    ht= Ht.get()
    wt = Wt.get()
    temp1 = temp.get()
    bp = Bp.get()
    hr = Hr.get()
    sympt = Sympt.get()
    gkey=Gkey.get()
    faceimg = Faceimg.get()
    dn1=Dn.get()
    file = open("data/record.txt", "w")
    xxx="Name : " + fullname1+ "Email :" + email+ "Contact : " + contact + "Height : " + ht+ "Weight :" + wt+ "Temperatre : " + temp1+ "Bp : "+bp+ "Heart Rate : " + hr+ "Symptom : " +sympt
    file.writelines(xxx)
    file.close()
    os.system("python encryption/encrypt.py")


    if fullname1 == "":
        messagebox.showinfo("BLockChain", "Enter Name")

    else:
        if email == "":
            messagebox.showinfo("BLockChain", "Enter Email")
        else:
            if contact == "":
                messagebox.showinfo("BLockChain", "Enter Contact")
            else:
                if ht== "":
                    messagebox.showinfo("BLockChain", "Enter Height")
                else:
                    if wt== "":
                        messagebox.showinfo("BLockChain", "Enter Weight")
                    else:
                        if temp== "":
                            messagebox.showinfo("BLockChain", "Enter Temperature")
                        else:
                            if not (re.search(regex, email)):
                                messagebox.showinfo("BLockChain", "Enter valid Email")
                            else:
                                if l != 10:
                                    messagebox.showinfo("BLockChain", "Enter 10 digits only")
                                else:
                                    if not fullname1.isalpha():
                                        messagebox.showinfo("BLockChain", "Enter Name in alphabets Only ")
                                    else:




                                                    conn = sqlite3.connect('Form.db')
                                                    with conn:
                                                            cursor = conn.cursor()
                                                            cursor.execute("SELECT * FROM patient")
                                                            rows = cursor.fetchall()
                                                            for row in rows:
                                                                dbuser = row[0]

                                                                ph1 = row[1]
                                                            if dbuser == fullname1 and email == ph1:
                                                                messagebox.showinfo("Healthcare", "Already Exist")
                                                            else:


                                                             cursor.execute('INSERT INTO patient (fullName,email,contact,Ht,Wt,temp,bp,Hr,Sympt,Gkey,photo,dn) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',
                                                                (fullname1,email,contact,ht,wt,temp1,bp,hr,sympt,gkey,faceimg,dn1))

                                                             conn.commit()
                                                             messagebox.showinfo("BLockChain", "Record Saved")


def viewlog():
    os.system("python bc.py")

def open_File():
    faceimg = askopenfilename(filetypes=[(".jpg", "*.jpg")])
    Faceimg.set(faceimg)
    fm = Faceimg.get()
    load = Image.open(fm)
    render = ImageTk.PhotoImage(load)

    # labels can be text or images
    img = Label(root, image=render)
    img.image = render
    img.place(x=500, y=300)

def update():
    fullname1 = Fullname.get()
    email = Email.get()
    contact = Contact.get()

    l = len(contact)

    ht = Ht.get()
    wt = Wt.get()
    temp1 = temp.get()
    bp = Bp.get()
    hr = Hr.get()
    sympt = Sympt.get()
    gkey = Gkey.get()
    faceimg = Faceimg.get()


    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            'delete from patient where fullname=',(fullname1,))
        cursor.execute(
        'INSERT INTO patient (fullName,email,contact,Ht,Wt,temp,bp,Hr,Sympt,Gkey,photo) VALUES(?,?,?,?,?,?,?,?,?,?,?)',
        (fullname1, email, contact, ht, wt, temp1, bp, hr, sympt, gkey, faceimg))

        conn.commit()
        messagebox.showinfo("BLockChain", "Record Updated")
label_0 = Label(root, justify=LEFT, bg='white', text="Patient Details", width=15, font=("bold", 20))
label_0.place(x=50, y=200)

label_1 = Label(root, text="FullName ", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_1.place(x=100, y=300)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=250, y=300)

label_2 = Label(root, text="Email", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_2.place(x=100, y=350)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=250, y=350)

label_3 = Label(root, text="Contact", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_3.place(x=100, y=400)

entry_3 = Entry(root, textvar=Contact)
entry_3.place(x=250, y=400)

label_4 = Label(root, text="Height", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_4.place(x=100, y=450)

entry_5 = Entry(root, textvar=Ht)
entry_5.place(x=250, y=450)


label_1 = Label(root, text="Select Doctor", bg='white', fg='black',justify=LEFT, width=20, font=("bold", 10))
label_1.place(x=400, y=400)
conn = sqlite3.connect('Form.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM doctor")
    rows = cur.fetchall()
    acn1 = []
    for row in rows:
        acn = row[0]
        acn1.append(acn)

        Dn.set('Select Name')
        entry_1=OptionMenu(root,Dn,*acn1)

entry_1.place(x=550, y=400)









label_5 = Label(root, text="Weight", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_5.place(x=400, y=450)

entry_6 = Entry(root, textvar=Wt)
entry_6.place(x=550, y=450)

label_7 = Label(root, text="Temperature", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_7.place(x=100, y=500)

entry_7 = Entry(root, textvar=temp)
entry_7.place(x=250, y=500)

label_8 = Label(root, text="Blood Pressure", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_8.place(x=400, y=500)
entry_7 = Entry(root, textvar=Bp)
entry_7.place(x=550, y=500)

label_7 = Label(root, text="Heart Rate", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_7.place(x=100, y=550)

entry_7 = Entry(root, textvar=Hr)
entry_7.place(x=250, y=550)

label_8 = Label(root, text="Symptoms", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_8.place(x=400, y=550)
entry_7 = Entry(root, textvar=Sympt)
entry_7.place(x=550, y=550)







label_8 = Label(root, text="Transaction ID", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_8.place(x=100, y=600)
entry_8 = Entry(root, textvar=Gkey)
entry_8.place(x=250, y=600)

label_7 = Label(root, text="Photo", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_7.place(x=100, y=650)

entry_7 = Entry(root, textvar=Faceimg)
entry_7.place(x=250, y=650)

Button(root, text='Generate Transaction ID', width=20, bg='red', fg='white', command=gkey).place(x=400, y=600)
Button(root, text='Upload', width=10, bg='gray', fg='white', command=database).place(x=650, y=650)
Button(root, text='Cancel', width=10, bg='gray', fg='white', command=cancel).place(x=730, y=650)
Button(root, text='Upload Report', width=20, bg='gray', fg='white', command=open_File).place(x=400, y=650)
Button(root, text='Update', width=10, bg='gray', fg='white', command=update).place(x=1050, y=650)
Button(root, text='View Log', width=10, bg='gray', fg='white', command=viewlog).place(x=1050, y=650)
root.mainloop()

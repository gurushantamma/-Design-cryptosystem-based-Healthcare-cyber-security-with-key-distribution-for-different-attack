from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

import os
from PIL import ImageTk, Image

root = Tk()
root.geometry('1366x768')
root.title("Report")
root.configure(bg="white")
Company = StringVar()
Email = StringVar()
Contact = StringVar()
Jname= StringVar()
Mreq = StringVar()
Age = StringVar()
Per = StringVar()
Nov = StringVar()


def cancel():
    root.destroy()









conn = sqlite3.connect('Form.db')
with conn:
        cursor = conn.cursor()

        cursor.execute("select *from doctor " )

        results = cursor.fetchall()
label_1 = Label(root, justify=LEFT, text=" Docotr Details",bg="white", fg="black", font=("bold", 20))
label_1.place(x=100, y=10)

label_1 = Label(root, justify=LEFT, text=" Name",bg="green",fg="white", font=("bold", 10))
label_1.place(x=100, y=50)
label_1 = Label(root, justify=LEFT, text="Email",bg="green",fg="white", font=("bold", 10))
label_1.place(x=300, y=50)
label_1 = Label(root, justify=LEFT, text="Contact",bg="green",fg="white", font=("bold", 10))
label_1.place(x=500, y=50)
rr=80
for row in results:
     a1 = row[0]
     a2 = row[1]
     a3 = row[2]
     Libcontect_label = Label(root, text=a1,bg="white", font=("bold", 10))
     Libcontect_label.place(x=100, y=rr)
     Libcontect_label = Label(root, text=a2, bg="white", font=("bold", 10))
     Libcontect_label.place(x=300, y=rr)
     Libcontect_label = Label(root, text=a3,bg="white", font=("bold", 10))
     Libcontect_label.place(x=500, y=rr)
     rr=int(rr)+30
conn.close()






Button(root, text='Cancel', width=10, bg='gray', fg='white', command=cancel).place(x=1010, y=650)

root.mainloop()

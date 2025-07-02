from tkinter import *
import sqlite3
import os
from tkinter import messagebox
from PIL import ImageTk, Image
root = Tk()
root.geometry('1366x768')
root.title("BlockChain")

canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back3.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1, 1, anchor=NW, image=photo)
Un = StringVar()
Pw = StringVar()
def back():
    root.destroy()
def reg():
    root.destroy()
    os.system('python patient.py')
def login():
    un = Un.get()
    pw = Pw.get()
    if un=="":
        messagebox.showinfo("BlockChain","Enter Email")
    else:
        if pw == "":
           messagebox.showinfo("BlockChain","Enter ID")
        else:
            conn = sqlite3.connect('Form.db')
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM register where un=? and pw=?",(un,pw))
                rows = cur.fetchall()
                for row in rows:
                 dbuser = row[3]
                 dbpw = row[4]
                 if dbuser == un and dbpw == pw:
                        root.destroy()
                        os.system('python patientdet.py')
                 else:
                    messagebox.showinfo("BlockChain", " Try Again")
#main program

label_0 = Label(root, text="Patient Login", bg='white', width=20, font=("bold", 20))
label_0.place(x=70, y=250)
label_1 = Label(root, text="Username", width=20, bg='white', font=("bold", 10))
label_1.place(x=100, y=350)
entry_2 = Entry(root, textvar=Un)
entry_2.place(x=300, y=350)
label_3 = Label(root, text="User ID", width=20,bg='white', font=("bold", 10))
label_3.place(x=90, y=400)
entry_6 = Entry(root, textvar=Pw, show="*")
entry_6.place(x=300, y=400)
Button(root, text='Login', width=20, bg='gray', fg='white', command=login).place(x=150, y=500)
Button(root, text='Cancel', width=20, bg='gray', fg='white', command=back).place(x=300, y=500)
Button(root, text='Register', width=20, bg='gray', fg='white', command=reg).place(x=150, y=550)
root.mainloop()

from tkinter import *

from PIL import ImageTk, Image
import sqlite3
import os
root = Tk()
root.geometry('1366x768')
root.title("Healthcare")
def patient():
    os.system('python Patientlogin.py')
def admin():
    os.system('python adminlogin.py')
def doct():
    os.system('python doctorlogin.py')
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.jpg')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
img1 = Image.open('h2.png')
photo1 = ImageTk.PhotoImage(img1)
img2 = Image.open('h1.png')
photo2 = ImageTk.PhotoImage(img2)
img3 = Image.open('doctor.png')
photo3 = ImageTk.PhotoImage(img3)
Button(root, text='Admin', image=photo1, width=200, height=180, bg='white', fg='white',font=("bold", 20) ,command=admin).place(x=600, y=100)
Button(root, text='Patient', image=photo2, width=200, height=180, bg='white', fg='white', font=("bold", 20),command=patient).place(x=800, y=100)
Button(root, text='Request Patient Data', image=photo3, width=200, height=180, bg='white', fg='white', font=("bold", 20),command=doct).place(x=1000, y=100)
root.mainloop()

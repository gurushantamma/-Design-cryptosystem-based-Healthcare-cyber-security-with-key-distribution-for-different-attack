from tkinter import *
import sqlite3
import os
from tkinter.filedialog import askopenfilename
import cv2
from PIL import ImageTk, Image
root = Tk()
root.geometry('1366x768')
root.title("Data")

canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back1.jpg')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
Un = StringVar()
Pw = StringVar()

def back():
    root.destroy()




def pre():

        os.system('python viewdoctor.py')
def adddoct():
    os.system("python doctordet.py")
def clf():
    root.destroy()
    os.system('python classification.py')
def dispred():
    root.destroy()
    os.system('python dispred.py')
Button(root, text='Back', width=15,height=2, bg='green', fg='white', command=back, font=("bold", 10)).place(x=600, y=200)
Button(root, text='Add Doctor', width=15,height=2, bg='green', fg='white', command=adddoct, font=("bold", 10)).place(x=730, y=200)
Button(root, text='View Doctor', width=15,height=2, bg='green', fg='white', command=pre, font=("bold", 10)).place(x=860, y=200)


root.mainloop()

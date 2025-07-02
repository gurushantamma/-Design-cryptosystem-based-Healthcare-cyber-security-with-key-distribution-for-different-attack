import os
import customtkinter as ctk
import tkinter.messagebox as tkmb
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry("400x400")
app.title("Login")

def login():
    un = user_entry.get()
    pw = user_pass.get()
    if "admin" == un and "admin" == pw:
        tkmb.showinfo(title="Login Successful", message="You have logged in Successfully,")
        app.destroy()
        os.system("python menu.py")
    elif user_entry.get() == un and user_pass.get() != pw:
        tkmb.showwarning(title='Wrong password', message='Please check your password')
    elif user_entry.get() != un and user_pass.get() == pw:
        tkmb.showwarning(title='Wrong username', message='Please check your username')
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and password")

label = ctk.CTkLabel(app, text="Blockchain in Healthcare",font=("BOLD",15))
label.pack(pady=20)
frame = ctk.CTkFrame(master=app)
frame.pack(pady=0, padx=0, fill='both', expand=True)
label = ctk.CTkLabel(master=frame, text='Admin Login Here....')
label.pack(pady=12, padx=10)
user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)
user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)
button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)
checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)
app.mainloop()
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import mysql.connector as sql
import tkinter as tk
import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter import messagebox
import db as db


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('USIU Medical Clinic')
        self.root.geometry('1199x600+100+50')
        # Background image
        self.bg = PIL.Image.open('background.png')
        self.img_copy = self.bg.copy()
        self.background = PIL.ImageTk.PhotoImage(self.bg)
        self.bg_image = Label(self.root, image=self.background)
        self.bg_image.pack(fill=BOTH, expand=YES)
        self.bg_image.bind('<Configure>', self.resize_image)

        # REGISTER FRAME
        register_frame = Frame(self.root, bg='white')
        register_frame.place(x=350, y=120, height=550, width=600)
        title = Label(register_frame, text='User Login', font=('Roboto', 35), fg='#5A63F5', bg='white')
        title.place(x=150, y=25)

        description = Label(register_frame, text='Please enter your details to login',
                            font=('Roboto', 12, 'italic'), fg='black', bg='white')
        description.place(x=150, y=90)

        first_label = Label(register_frame, text='First Name',
                            font=('Roboto', 12, 'italic'), fg='black', bg='white')
        first_label.place(x=90, y=120)

        # first name entry box
        self.first_name = Entry(register_frame, font=('Roboto', 15), bg='lightgray')
        self.first_name.place(x=90, y=150, width=350, height=35)

        # Last Name Label
        last_label = Label(register_frame, text='Last Name',
                           font=('Roboto', 12, 'italic'), fg='black', bg='white')
        last_label.place(x=90, y=190)

        # last Name entry box
        self.last_name = Entry(register_frame, font=('Roboto', 15), bg='lightgray')
        self.last_name.place(x=90, y=220, width=350, height=35)

        # Staff ID label
        staff_id = Label(register_frame, text='Staff ID',
                           font=('Roboto', 12, 'italic'), fg='black', bg='white')
        staff_id.place(x=90, y=260)
        # student id entry
        self.staff_id = Entry(register_frame, font=('Roboto', 15), bg='lightgray')
        self.staff_id.place(x=90, y=290, width=350, height=35)

        # Position label
        position = Label(register_frame, text='Position',
                           font=('Roboto', 12, 'italic'), fg='black', bg='white')
        position.place(x=90, y=330)

        # Position entry
        self.position = Entry(register_frame, font=('Roboto', 15), bg='lightgray')
        self.position.place(x=90, y=360, width=350, height=35)

        # Password
        password = Label(register_frame, text='Password',
                         font=('Roboto', 12, 'italic'), fg='black', bg='white')
        password.place(x=90, y=400)

        # Password entry
        self.password = Entry(register_frame, show='*', font=('Roboto', 15), bg='lightgray')
        self.password.place(x=90, y=430, width=350, height=35)

        # Button
        register = Button(register_frame, text='Login', bd=1, bg='white', fg='#5A63F5', font=('Roboto', 20, 'italic'),
                          command=self.login)
        register.place(x=120, y=470, height=45, width=180)

    def resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.bg = self.img_copy.resize((new_width, new_height))
        self.background = PIL.ImageTk.PhotoImage(self.bg)
        self.bg_image.configure(image=self.background)

    def login(self):
        data = (
            self.staff_id.get(),
            self.first_name.get(),
            self.last_name.get(),
            self.position.get(),
            self.password.get()
        )
        # Validations
        if self.staff_id.get() == '':
            messagebox.showerror('Error', 'Please provide the staff ID')
        elif self.first_name.get() == '':
            messagebox.showerror('Error', 'Please provide a first name')
        elif self.last_name.get() == '':
            messagebox.showerror('Error', 'Please provide a last name')
        elif self.position.get() =='':
            messagebox.showerror('Errpr', 'Please provide a position')
        elif self.password.get() == '':
            messagebox.showerror('Error', 'Please provide a password')
        else:
            res = db.user_login(data)
            if res:
                messagebox.showinfo('Success', 'User Login Successful')
            else:
                messagebox.showerror('Error!', 'Wrong name/schoolID')


root = Tk()
login_object = Login(root)
root.mainloop()


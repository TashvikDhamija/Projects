from tkinter import *
import tkinter.font as tkf
import tkinter.messagebox as tkm
import os


class Login:
    path = "*Directory*"
    # Constructor
    def __init__(self, master):
        self.master = master
        self.master.title("Main Log In")
        self.master.geometry("400x400")
        # Username Label
        fontStyle = tkf.Font(family="Arial", size=10)
        self.lbl1 = Label(self.master, text="Enter Username", font=fontStyle)
        self.lbl1.place(x=0, y=100)
        # Username Entry
        self.username = Entry(self.master, width=40)
        self.username.place(x=100, y=100)
        # Password Label
        fontStyle = tkf.Font(family="Arial", size=10)
        self.lbl2 = Label(self.master, text="Enter Password", font=fontStyle)
        self.lbl2.place(x=0, y=150)
        # Password Entry
        self.password = Entry(self.master, width=40)
        self.password.place(x=100, y=150)
        # Submit Button
        self.submit_but = Button(self.master, text="SUBMIT", command=self.submit_button)
        self.submit_but.place(x=80, y=170, width=120)
        # Quit Button
        self.quit_but = Button(self.master, text="QUIT", command=self.master.destroy)
        self.quit_but.place(x=140, y=310, width=120)
        # Change Password
        self.change_but = Button(self.master, text="Change Password", command=self.change_password)
        self.change_but.place(x=140, y=210, width=120)
        # Register User
        self.register_but = Button(self.master, text="Register", command=self.register_user)
        self.register_but.place(x=200, y=170, width=120)

    # Password Verification
    def submit_button(self):
        file_list = os.listdir(path)
        username = self.username.get() + '.txt'
        if username in file_list:
            file1 = open(self.username.get() + '.txt')
            verify = file1.read().splitlines()
            file1.close()
            if self.password.get() in verify:
                self.new_window(Main_app)
            else:
                c = tkm.askretrycancel("Login Error", "Password or Username Incorrect")
                if not c:
                    self.master.destroy()
        else:
            c = tkm.askretrycancel("Login Error", "User Does Not Exist")
            if not c:
                self.master.destroy()

    # Changing Password
    def change_password(self):
        self.new_window(Change_pass)

    # Registering New User
    def register_user(self):
        self.new_window(Register_user)

    # Creating New Window
    def new_window(self, _class):
        self.main_app = Toplevel(self.master)
        _class(self.main_app)


class Register_user:

    # Constructor
    def __init__(self, master):
        self.master = master
        self.master.title("Main Log In")
        self.master.geometry("400x400")
        # Username Label
        fontStyle = tkf.Font(family="Arial", size=10)
        self.lbl1 = Label(self.master, text="Enter Username", font=fontStyle)
        self.lbl1.place(x=0, y=100)
        # Username Entry
        self.username = Entry(self.master, width=40)
        self.username.place(x=130, y=100)
        # Password Label
        fontStyle = tkf.Font(family="Arial", size=10)
        self.lbl2 = Label(self.master, text="Enter Password", font=fontStyle)
        self.lbl2.place(x=0, y=150)
        # Password Entry
        self.password = Entry(self.master, width=40)
        self.password.place(x=130, y=150)
        # Password Label
        fontStyle = tkf.Font(family="Arial", size=10)
        self.lbl3 = Label(self.master, text="Re-Enter Password", font=fontStyle)
        self.lbl3.place(x=0, y=200)
        # Password Entry
        self.password_re = Entry(self.master, width=40)
        self.password_re.place(x=130, y=200)
        # Submit Button
        self.submit_but = Button(self.master, text="SUBMIT", command=self.submit_button)
        self.submit_but.place(x=80, y=230, width=120)
        # Quit Button
        self.quit_but = Button(self.master, text="QUIT", command=self.master.destroy)
        self.quit_but.place(x=200, y=230, width=120)

    def submit_button(self):
        file_list = os.listdir(path)
        username = self.username.get() + '.txt'
        if username in file_list:
            c = tkm.askretrycancel("Change Password Error", "User Doesn't Exist")
            if not c:
                self.master.destroy()
        else:
            file1 = open(self.username.get() + '.txt', 'w')
            file1.write(self.password.get())
            file1.close()
            tkm.showinfo('Register User', 'New User Created')
            self.master.destroy()


class Main_app:

    # Constructor
    def __init__(self, master):
        self.master = master
        self.master.title("Main Application")
        self.master.geometry("400x400")


class Change_pass:

    # Constructor
    def __init__(self, master):
        self.master = master
        self.master.title("Main Log In")
        self.master.geometry("400x400")
        # Username Label
        fontStyle = tkf.Font(family="Arial", size=10)
        self.lbl1 = Label(self.master, text="Enter Username", font=fontStyle)
        self.lbl1.place(x=0, y=100)
        # Username Entry
        self.username = Entry(self.master, width=40)
        self.username.place(x=100, y=100)
        # Submit Button
        self.submit_but_user = Button(self.master, text="SUBMIT", command=self.submit_button_user)
        self.submit_but_user.place(x=140, y=120, width=120)
        # Quit Button
        self.quit_but = Button(self.master, text="QUIT", command=self.master.destroy)
        self.quit_but.place(x=140, y=310, width=120)

    def submit_button_user(self):
        file_list = os.listdir(path)
        username = self.username.get() + '.txt'
        if username in file_list:
            # Password Label
            fontStyle = tkf.Font(family="Arial", size=10)
            self.lbl2 = Label(self.master, text="Enter Password", font=fontStyle)
            self.lbl2.place(x=0, y=170)
            # Password Entry
            self.password = Entry(self.master, width=40)
            self.password.place(x=130, y=170)
            self.lbl3 = Label(self.master, text="Re-Enter Password", font=fontStyle)
            self.lbl3.place(x=0, y=200)
            # Password Entry
            self.password_re = Entry(self.master, width=40)
            self.password_re.place(x=130, y=200)
            # Submit Button
            self.submit_but_pass = Button(self.master, text="SUBMIT", command=self.update_password)
            self.submit_but_pass.place(x=140, y=250, width=120)
        else:
            c = tkm.askretrycancel("Change Password Error", "User Doesn't Exist")
            if not c:
                self.master.destroy()

    def update_password(self):
        if self.password.get() == self.password_re.get():
            file1 = open(self.username.get() + '.txt', 'w')
            file1.write(self.password.get())
            file1.close()
            tkm.showinfo('Update Password', 'Password Updated')
            self.master.destroy()
        else:
            c = tkm.askretrycancel("Change Password Error", "Re-Entered Password does not match New Password")
            if not c:
                self.master.destroy()


# Running main Application
root = Tk()
app = Login(root)
root.mainloop()

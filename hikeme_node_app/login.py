import tkinter
from tkinter import *
import database
from django.conf import settings
settings.configure(DEBUG=True)
from django.contrib.auth.hashers import check_password

class LoginWindow(Toplevel):
    def __init__(self, mainapp, master=None):
        super().__init__(master=master)
        self.mainapp = mainapp

        self.db, self.cur = database.connectToDB()

        self.geometry("300x100")
        self.title("Login")
        
        self.usernameEntry = Entry(self, width = 25)
        self.usernameEntry.pack()
        self.passwordEntry = Entry(self, width = 25)
        self.passwordEntry.pack()
        
        self.submitButton=tkinter.Button(self, text="Submit", command=lambda: self.login(str(self.usernameEntry.get()), str(self.passwordEntry.get()))).pack()
        self.label1 = Label(self, text="Try logging into a DJANGO Superuser.").pack(side=BOTTOM)

    def login(self, username, password):
        grabbedUsername, grabbedPassword, grabbedSuperuserStatus, grabbedID = database.getUserDetails(self.db, self.cur, username)

        if grabbedUsername is not None:
            if check_password(password, grabbedPassword):
                currentUser = CurrentUser(grabbedID, grabbedUsername, grabbedPassword, grabbedSuperuserStatus)
                self.mainapp.currentUser = currentUser
                self.destroy()
            else:
                print("Wrong password!")
        else:
            print("Username not found!")

class CurrentUser:
    def __init__(self, id, username, password, is_superuser):
        self.userId = id
        self.username = username
        self.password = password
        self.is_superuser = is_superuser 
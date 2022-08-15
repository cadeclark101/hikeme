from hashlib import new
import tkinter
from tkinter import *
import sqlite3
from django.conf import settings
settings.configure(DEBUG=True)
from django.contrib.auth.hashers import check_password

db = sqlite3.connect("hikeme_database.sqlite3")
cur = db.cursor()

class LoginWindow(Toplevel):
    def __init__(self, mainapp, master=None):
        super().__init__(master=master)
        self.mainapp = mainapp

        self.geometry("300x100")
        self.title("Login")
        
        self.usernameEntry = Entry(self, width = 25)
        self.usernameEntry.pack()
        self.passwordEntry = Entry(self, width = 25)
        self.passwordEntry.pack()
        self.submitButton=tkinter.Button(self, text="Submit", command=lambda: self.login(str(self.usernameEntry.get()), str(self.passwordEntry.get())))
        self.submitButton.pack()
        self.label1 = Label(self, text="Try logging into a DJANGO Superuser.")
        self.label1.pack(side=BOTTOM)

    def login(self, username, password):
        query = f"SELECT username, password, is_superuser, id from auth_user WHERE username='{username}';"
        cur.execute(query)
        result = cur.fetchall()
        grabbedUsername, grabbedPassword, grabbedSuperuserStatus, grabbedID = result[[0][0]]
        
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
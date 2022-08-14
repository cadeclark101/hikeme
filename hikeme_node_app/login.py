import tkinter
from tkinter import *
import sqlite3
from django.conf import settings
settings.configure(DEBUG=True)
from django.contrib.auth.hashers import check_password

db = sqlite3.connect("hikeme_database.sqlite3")
cur = db.cursor()

class LoginWindow:
    def __init__(self, root):
        self.loginWindow = Toplevel(root)
        self.loginWindow.geometry("200x200")

        self.loginWindow.usernameEntry = Entry(self.loginWindow, width = 25)
        self.loginWindow.usernameEntry.pack()
        self.loginWindow.passwordEntry = Entry(self.loginWindow, width = 25)
        self.loginWindow.passwordEntry.pack()
        self.loginWindow.submitButton=tkinter.Button(self.loginWindow, text="Submit", command=lambda: self.login(str(self.loginWindow.usernameEntry.get()), str(self.loginWindow.passwordEntry.get())))
        self.loginWindow.submitButton.pack()

        closeWindowButton= Button(self.loginWindow, text="Close", command=lambda: self.loginWindow.closeWindow)
        closeWindowButton.pack(pady=5, side= TOP)

    def run(self):
        self.loginWindow.mainloop()

    def login(self, username, password):
        query = f"SELECT username, password from auth_user WHERE username='{username}';"
        cur.execute(query)
        result = cur.fetchall()
        grabbedUsername, grabbedPassword = result[[0][0]]
        
        if grabbedUsername is not None:
            print("User: '" + username + "' found!")
            if check_password(password, grabbedPassword):
                print("Passwords match!")
            else:
                print("Wrong password!")
        else:
            print("Username not found!")

    def closeWindow(self):
        self.loginWindow.destroy()
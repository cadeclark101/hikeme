import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import django.contrib.auth.hashers

def login(username, password):
    db = sqlite3.connect("hikeme_database.sqlite3")
    cur = db.cursor()
    query = f"SELECT username from auth_user WHERE username='{username}';"
    cur.execute(query)
    result = cur.fetchone()
    if result is not None:
        username = result
        print(str(username) + " found!")
    else:
        print("Username not found!")
    


    #passwordValid = django.contrib.auth.hashers.check_password(password)
    #if not passwordValid:
    #    print("Wrong password.")

root = Tk()
root.geometry("1920x1080")

def loginWindow():
    top = Toplevel(root)
    top.geometry("200x200")

    usernameEntry = Entry(top, width = 25)
    usernameEntry.pack()
    passwordEntry = Entry(top, width = 25)
    passwordEntry.pack()

    submitButton=tkinter.Button(top, text="Submit", command=lambda:login(str(usernameEntry.get()), str(passwordEntry.get())))
    submitButton.pack()

    closeWindowButton= Button(top, text="Close", command=lambda:closeWindow(top))
    closeWindowButton.pack(pady=5, side= TOP)


def closeWindow(top):
    top.destroy()

# Create a photoimage object of the image in the path
englandImage = Image.open("hikeme_node_app\england.jpg")
englandImage = ImageTk.PhotoImage(englandImage)

englandImageLabel = tkinter.Label(image=englandImage)
englandImageLabel.image = englandImage

pixel = tkinter.PhotoImage(width=5, height=5)
fileyButton=tkinter.Button(root, text="", image=pixel, bg='blue')
fileyButton.place(x=360, y=400)
saltburnButton=tkinter.Button(root, text="", image=pixel, bg='blue')
saltburnButton.place(x=325, y=375)
helmsleyButton=tkinter.Button(root, text="", image=pixel, bg='blue')
helmsleyButton.place(x=325, y=395)

mineheadButton=tkinter.Button(root, text="", image=pixel, bg='black')
mineheadButton.place(x=217, y=636)
stivesButton=tkinter.Button(root, text="", image=pixel, bg='black')
stivesButton.place(x=130, y=715)
brixhamButton=tkinter.Button(root, text="", image=pixel, bg='black')
brixhamButton.place(x=222, y=694)
pooleButton=tkinter.Button(root, text="", image=pixel, bg='black')
pooleButton.place(x=299, y=675)

doverButton=tkinter.Button(root, text="", image=pixel, bg='red')
doverButton.place(x=450, y=636)
kentButton=tkinter.Button(root, text="", image=pixel, bg='red')
kentButton.place(x=433, y=628)
otfordButton=tkinter.Button(root, text="", image=pixel, bg='red')
otfordButton.place(x=390, y=620)
farnhamButton=tkinter.Button(root, text="", image=pixel, bg='red')
farnhamButton.place(x=350, y=625)

loginButton=tkinter.Button(root, text="Login", command=loginWindow)
loginButton.place(bordermode=OUTSIDE)

# Position image
englandImageLabel.place(x=0, y=0)

root.mainloop()


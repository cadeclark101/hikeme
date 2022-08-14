import tkinter
from tkinter import *
from PIL import Image, ImageTk
import login

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1920x1080")
        self.root.englandImage = Image.open("hikeme_node_app\england.jpg")
        self.root.englandImage = ImageTk.PhotoImage(self.root.englandImage)
        self.root.englandImageLabel = tkinter.Label(image=self.root.englandImage)
        self.root.englandImageLabel.image = self.root.englandImage

        self.root.pixel = tkinter.PhotoImage(width=5, height=5)

        self.root.fileyButton=tkinter.Button(self.root, text="", image=self.root.pixel, bg='blue')
        self.root.fileyButton.place(x=360, y=400)
        self.root.saltburnButton=tkinter.Button(self.root, text="", image=self.root.pixel, bg='blue')
        self.root.saltburnButton.place(x=325, y=375)
        self.root.helmsleyButton=tkinter.Button(self.root, text="", image=self.root.pixel, bg='blue')
        self.root.helmsleyButton.place(x=325, y=395)

        self.root.mineheadButton=tkinter.Button(self.root, text="", image=self.root.pixel, bg='black')
        self.root.mineheadButton.place(x=217, y=636)
        self.root.stivesButton=tkinter.Button(self.root, text="", image=self.root.pixel, bg='black')
        self.root.stivesButton.place(x=130, y=715)
        self.root.brixhamButton=tkinter.Button(self.root, text="", image=self.root.pixel, bg='black')
        self.root.brixhamButton.place(x=222, y=694)
        self.root.pooleButton=tkinter.Button(self.root, text="", image=self.root.pixel, bg='black')
        self.root.pooleButton.place(x=299, y=675)

        self.root.doverButton=tkinter.Button(self.root, text="", image=self.root.pixel, bg='red')
        self.root.doverButton.place(x=450, y=636)
        self.root.kentButton=tkinter.Button(self.root, text="", image=self.root.pixel, bg='red')
        self.root.kentButton.place(x=433, y=628)
        self.root.otfordButton=tkinter.Button(self.root, text="", image=self.root.pixel, bg='red')
        self.root.otfordButton.place(x=390, y=620)
        self.root.farnhamButton=tkinter.Button(self.root, text="", image=self.root.pixel, bg='red')
        self.root.farnhamButton.place(x=350, y=625)
        self.root.loginButton=tkinter.Button(self.root, text="Login", command=lambda: login.LoginWindow(self.root))

        self.root.loginButton.place(bordermode=OUTSIDE)

        self.root.englandImageLabel.place(x=0, y=0)

    def run(self):
        self.root.mainloop()

root = MainWindow()
root.run()


 

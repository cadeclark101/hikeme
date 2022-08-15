from asyncio.windows_events import NULL
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import login
import os

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Hikeme Node Network")
        self.master.geometry("1920x1080")

        self.master.currentUser = None

        self.master.englandImage = Image.open("hikeme_node_app\england.jpg")
        self.master.englandImage = ImageTk.PhotoImage(self.master.englandImage)
        self.master.englandImageLabel = tkinter.Label(image=self.master.englandImage)
        self.master.englandImageLabel.image = self.master.englandImage

        self.master.pixel = tkinter.PhotoImage(width=5, height=5)

        self.master.fileyButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='blue')
        self.master.fileyButton.place(x=360, y=400)
        self.master.saltburnButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='blue')
        self.master.saltburnButton.place(x=325, y=375)
        self.master.helmsleyButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='blue')
        self.master.helmsleyButton.place(x=325, y=395)

        self.master.mineheadButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='black')
        self.master.mineheadButton.place(x=217, y=636)
        self.master.stivesButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='black')
        self.master.stivesButton.place(x=130, y=715)
        self.master.brixhamButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='black')
        self.master.brixhamButton.place(x=222, y=694)
        self.master.pooleButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='black')
        self.master.pooleButton.place(x=299, y=675)

        self.master.doverButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='red')
        self.master.doverButton.place(x=450, y=636)
        self.master.kentButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='red')
        self.master.kentButton.place(x=433, y=628)
        self.master.otfordButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='red')
        self.master.otfordButton.place(x=390, y=620)
        self.master.farnhamButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='red')
        self.master.farnhamButton.place(x=350, y=625)
        
        self.master.loginButton=tkinter.Button(self.master, text="Login", command=lambda: login.LoginWindow(self.master, self.master.currentUser))
        self.master.loginButton.place(bordermode=OUTSIDE)

        self.master.englandImageLabel.place(x=0, y=0)

    def run(self):
        self.master.mainloop()

def main():
    os.system('cls')
    root = Tk()
    MainWindow(root)
    root.mainloop()

if __name__ == "__main__": main()


 

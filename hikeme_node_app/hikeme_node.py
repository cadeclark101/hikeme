from asyncio.windows_events import NULL
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import login
import control_menu
import os

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Hikeme Node Network")
        self.master.geometry("487x778")

        self.master.currentUser = None
        self.master.selectedCheckpoint = None

        self.master.englandImage = Image.open("hikeme_node_app\england.jpg")
        self.master.englandImage = ImageTk.PhotoImage(self.master.englandImage)
        self.master.englandImageLabel = tkinter.Label(image=self.master.englandImage)
        self.master.englandImageLabel.image = self.master.englandImage

        self.master.pixel = tkinter.PhotoImage(width=5, height=5)

        self.master.fileyButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='blue', command=lambda: self.openMenuWindow(0)).place(x=360, y=400)
        self.master.saltburnButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='blue', command=lambda: self.openMenuWindow(1)).place(x=325, y=375)
        self.master.helmsleyButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='blue', command=lambda: self.openMenuWindow(2)).place(x=325, y=395)

        self.master.mineheadButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='black').place(x=217, y=636)
        self.master.stivesButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='black').place(x=130, y=715)
        self.master.brixhamButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='black').place(x=222, y=694)
        self.master.pooleButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='black').place(x=299, y=675)

        self.master.doverButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='red').place(x=450, y=636)
        self.master.kentButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='red').place(x=433, y=628)
        self.master.otfordButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='red').place(x=390, y=620)
        self.master.farnhamButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='red').place(x=350, y=625)
        
        self.master.loginButton=tkinter.Button(self.master, text="Login", command= self.openLoginWindow).pack()

        self.master.englandImageLabel.place(x=0, y=0)

    def openMenuWindow(self, selectedCheckpoint):
        if self.master.currentUser is not None:
                self.master.selectedCheckpoint = selectedCheckpoint
                control_menu.ControlMenuWindow(self.master)
        else:
            tkinter.messagebox.showinfo(title="Error", message="Not logged in.")

    def openLoginWindow(self):
        login.LoginWindow(self.master, self.master.currentUser)

    def run(self):
        self.master.mainloop()

def main():
    os.system('cls')
    root = Tk()
    MainWindow(root)
    root.mainloop()

if __name__ == "__main__": main()


 

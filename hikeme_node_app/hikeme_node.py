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

        self.master.topWindow = None

        self.master.allTrailInfo = None
        self.master.allTrailCheckpointInfo = None
        self.master.selectedCheckpoints = []

        self.master.currentUser = None

        self.loadInitUI()
        




    def loadInitUI(self):
        self.master.englandImage = Image.open("hikeme_node_app\england.jpg")
        self.master.englandImage = ImageTk.PhotoImage(self.master.englandImage)
        self.master.englandImageLabel = tkinter.Label(image=self.master.englandImage)
        self.master.englandImageLabel.image = self.master.englandImage

        self.master.pixel = tkinter.PhotoImage(width=5, height=5)

        self.master.fileyButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='blue', command=lambda: self.updatedSelectedCheckpoints("1")).place(x=360, y=400)
        self.master.saltburnButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='blue', command=lambda: self.updatedSelectedCheckpoints("2")).place(x=325, y=375)
        self.master.helmsleyButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='blue', command=lambda: self.updatedSelectedCheckpoints("3")).place(x=325, y=395)

        self.master.mineheadButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='black', command=lambda: self.updatedSelectedCheckpoints("4")).place(x=217, y=636)
        self.master.stivesButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='black', command=lambda: self.updatedSelectedCheckpoints("5")).place(x=130, y=715)
        self.master.brixhamButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='black', command=lambda: self.updatedSelectedCheckpoints("6")).place(x=222, y=694)
        self.master.pooleButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='black', command=lambda: self.updatedSelectedCheckpoints("7")).place(x=299, y=675)

        self.master.doverButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='red', command=lambda: self.updatedSelectedCheckpoints("8")).place(x=450, y=636)
        self.master.kentButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='red', command=lambda: self.updatedSelectedCheckpoints("9")).place(x=433, y=628)
        self.master.otfordButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='red', command=lambda: self.updatedSelectedCheckpoints("10")).place(x=390, y=620)
        self.master.farnhamButton=tkinter.Button(self.master, text="", image=self.master.pixel, bg='red', command=lambda: self.updatedSelectedCheckpoints("11")).place(x=350, y=625)
        
        self.master.loginButton=tkinter.Button(self.master, text="Login", command= self.openLoginWindow).pack()
        self.master.openMenuButton=tkinter.Button(self.master, text="Menu", command= self.openMenuWindow).pack()

        self.master.englandImageLabel.place(x=0, y=0)
            


    def updatedSelectedCheckpoints(self, selectedCheckpoint):
        if selectedCheckpoint not in self.master.selectedCheckpoints:
            self.master.selectedCheckpoints.append(selectedCheckpoint)
            if self.master.topWindow is not None:
                self.master.topWindow.updateTree()




    def openMenuWindow(self):
        if self.master.currentUser is not None:
                self.master.topWindow = control_menu.ControlMenuWindow(self.master)
        else:
            tkinter.messagebox.showinfo(title="Error", message="Not logged in.")




    def openLoginWindow(self):
        self.master.topWindow = login.LoginWindow(self.master)




    def run(self):
        self.master.mainloop()




def main():
    os.system('cls')
    root = Tk()
    MainWindow(root)
    root.mainloop()

if __name__ == "__main__": main()


 

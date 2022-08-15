from struct import pack
from tkinter import *
from tkinter import Listbox
from tkinter import messagebox       

class ControlMenuWindow(Toplevel):
    def __init__(self, mainapp, master=None):
        super().__init__(master=master)
        self.mainapp = mainapp

        self.geometry("500x500")
        self.title("Control Menu")

        self.selectedCheckpoint = self.mainapp.selectedCheckpoint

        self.label1 = Label(self, text="Checkpoint ID: " + str(self.mainapp.selectedCheckpoint)).pack()
        self.label2 = Label(self, text="Warning:").pack()
        self.warningEntry = Entry(self, width=50)
        self.warningEntry.pack()
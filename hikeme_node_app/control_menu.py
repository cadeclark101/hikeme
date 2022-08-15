import tkinter
from tkinter import *
from tkinter import Listbox
import login

class SuperuserControlMenuWindow(Toplevel):
    def __init__(self, mainapp, master=None):
        super().__init__(master=master)
        self.mainapp = mainapp

        self.geometry("500x500")
        self.title("SUPERUSER Menu")

        self.checkpointButtonIDList = self.mainapp.selectedCheckpoints

        if self.checkpointButtonIDList is None:
            self.label1 = Label(self, text="No checkpoints selected!").pack()
            #self.listbox1 = Listbox(self)
            #for i in range(len(self.checkpointButtonIDList)):
                #self.listbox1.insert(i, str(self.checkpointButtonIDList[i]))
            #self.listbox1.pack()
        if len(self.checkpointButtonIDList) >= 3:
            print(self.checkpointButtonIDList)
            self.multithreadCB = Checkbutton(self, text='Enable Multithreading', onvalue=1, offvalue=0)
            self.multithreadCB.pack()
        

class ControlMenuWindow(Toplevel):
    def __init__(self, mainapp, master=None):
        super().__init__(master=master)
        self.mainapp = mainapp

        self.geometry("500x500")
        self.title("Menu")

        self.checkpointButtonID = self.mainapp.checkpointButtonID
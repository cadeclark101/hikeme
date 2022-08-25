from tkinter import *
from tkinter import ttk
from tkinter import Listbox      

class ControlMenuWindow(Toplevel):
    def __init__(self, mainapp, master=None):
        super().__init__(master=master)
        self.mainapp = mainapp

        self.geometry("500x500")
        self.title("Control Menu")

        self.selectedCheckpoints = self.mainapp.selectedCheckpoints

        #self.label1 = Label(self, text="Checkpoint ID: " + str(self.mainapp.selectedCheckpoint)).pack()
        #self.label2 = Label(self, text="Warning:").pack()
        
        #self.warningEntry = Entry(self, width=50)
        #self.warningEntry.pack()

        #self.submitButton=tkinter.Button(self, text="Submit", command=lambda: self.login(str(self.warningEntry.get())).pack()
        
        self.t_scroll = Scrollbar(self)
        self.t_scroll.pack(side=RIGHT, fill=Y)
        self.t_table = ttk.Treeview(self, yscrollcommand=self.t_scroll.set)
        self.t_scroll.config(command=self.t_table.yview) 
        self.loadInit()
        self.t_table.pack()

    def loadInit(self):
        for i in self.selectedCheckpoints:
            self.t_table.insert('', 'end', i, text=i)

    def updateTree(self):
        self.t_table.insert(parent='', index='end', text=self.mainapp.selectedCheckpoints[-1])

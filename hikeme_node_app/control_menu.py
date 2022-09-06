from cgitb import enable
from tkinter import *
from tkinter import ttk
from tkinter import Listbox  
from tkinter import messagebox
from turtle import bgcolor, width 




class ControlMenuWindow(Toplevel):
    def __init__(self, mainapp):
        super().__init__()
        self.mainapp = mainapp
        self.protocol("WM_DELETE_WINDOW", self.onClose)

        self.geometry("500x400")
        self.resizable(False,False)
        self.title("Control Menu")


        self.selectedCheckpoints = self.mainapp.selectedCheckpoints

        if self.master.currentUser.is_superuser:
            self.loadInitUI()




    def loadInitUI(self):
        self.listboxFrame = Frame(self)

        self.t_scroll = Scrollbar(self)
        self.t_table = ttk.Treeview(self.listboxFrame, columns="checkpointIDcol", show="headings", yscrollcommand=self.t_scroll.set)
        self.t_scroll.config(command=self.t_table.yview) 
        
        self.loadInitTableElements()

        self.t_table.heading("checkpointIDcol", text="Checkpoint ID")
        self.t_table.grid(row = 0, column = 0, sticky = NSEW, padx = 5, pady = 5)
        self.t_scroll.grid(row=0, column=0, sticky=NS, padx = 50)
        self.listboxFrame.grid(row=0, column=0, columnspan=1, sticky = NW)

        self.menuItemsFrame = Frame(self)
        self.label2 = Label(self.menuItemsFrame, text= "POST NEW CHECK-INS").grid(row = 1, column=0, sticky=N, padx=20)
        self.checkInNum = Entry(self.menuItemsFrame, width=5).grid(row = 1, column = 2, sticky=N, padx=20)

        self.label3 = Label(self.menuItemsFrame, text= "POST NEW WARNINGS").grid(row = 2, column=0, sticky=N, padx=20)
        self.warningNum = Entry(self.menuItemsFrame, width=5).grid(row = 2, column = 2, sticky=N, padx=20)

        self.goButton = Button(self.menuItemsFrame, text="GO").grid(row = 3, column=0, sticky=NW, padx=20)
        self.stopButton = Button(self.menuItemsFrame, text="STOP").grid(row = 3, column=2, sticky=NE, padx=20)
        
        self.menuItemsFrame.grid(row=0, column=0, sticky= NE)

        self.outputFeedBox = Text(self, height=10, width=60).grid(row = 2, column = 0, columnspan=1, sticky = S, padx = 5, pady=5)


        


    def loadInitTableElements(self):
        if self.selectedCheckpoints is not None:
            for i in self.selectedCheckpoints:
                self.t_table.insert('', 'end', i, values=i)



    def updateTree(self):
        self.t_table.insert(parent='', index='end', values=self.mainapp.selectedCheckpoints[-1])

        

    def onClose(self):
        self.mainapp.selectedCheckpoints = []
        self.destroy()
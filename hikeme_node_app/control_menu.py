import multiprocessing
from tkinter import *
from tkinter import ttk
import database
import utils
import cProfile


class ControlMenuWindow(Toplevel):
    def __init__(self, mainapp):
        super().__init__()
        self.mainapp = mainapp
        self.protocol("WM_DELETE_WINDOW", self.onClose)

        self.geometry("500x400")
        self.resizable(False,False)
        self.title("Control Menu")

        self.db, self.cur = database.connectToDB()


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
        self.checkInNumEntry = Entry(self.menuItemsFrame, width=5)
        self.checkInNumEntry.grid(row = 1, column = 2, sticky=N, padx=15)

        self.label3 = Label(self.menuItemsFrame, text= "POST NEW WARNINGS").grid(row = 2, column=0, sticky=N, padx=20)
        self.warningNumEntry = Entry(self.menuItemsFrame, width=5)
        self.warningNumEntry.grid(row = 2, column = 2, sticky=N, padx=15)

        self.label4 = Label(self.menuItemsFrame, text= "NO. OF PROCESSES").grid(row = 3, column=0, sticky=N, padx=20)
        self.processNumEntry = Entry(self.menuItemsFrame, width=5)
        self.processNumEntry.grid(row = 3, column = 2, sticky=N, padx=15)

        self.goButton = Button(self.menuItemsFrame, text="GO", command=lambda: self.handleGoButton(self.checkInNumEntry.get(), self.warningNumEntry.get(), self.processNumEntry.get())).grid(row = 4, column=0, sticky=NW, padx=20)
        self.stopButton = Button(self.menuItemsFrame, text="STOP").grid(row = 4, column=2, sticky=NE, padx=15)
        
        self.menuItemsFrame.grid(row=0, column=0, sticky= NE)

        self.outputFeedBox = Text(self, height=9, width=60).grid(row = 2, column = 0, columnspan=1, sticky = S, padx = 5, pady=5)


    def handleGoButton(self, checkinN, warningN, processN):
        grabbedUserIDs = database.getNumPersonID(self.cur, warningN)
        grabbedUserIDsLength = len(grabbedUserIDs)

        if grabbedUserIDsLength < int(checkinN) or grabbedUserIDsLength < int(warningN):
            self.label4 = Label(self.menuItemsFrame, text=("ONLY %s USER IDs EXIST" % grabbedUserIDsLength)).grid(row = 4, column=0, sticky=S, pady=60, columnspan=3)
        self.createWarningInsertProcesses(int(warningN), int(processN), grabbedUserIDsLength)


    def createWarningInsertProcesses(self, warningN, processN, grabbedUserIDsLength):
        async_results = []
        warningFile = utils.loadFile("warnings.txt", "r")

        profile = cProfile.Profile()
        profile.enable()

        with multiprocessing.Pool(processes=processN) as pool:
            for _ in range(warningN):
                async_results.append(pool.apply_async(database.insertWarning(self.selectedCheckpoints, grabbedUserIDsLength, warningFile)))
        pool.close()
        pool.join()

        profile.disable()
        profile.print_stats(sort='tottime')
 


    def loadInitTableElements(self):
        if self.selectedCheckpoints is not None:
            for i in self.selectedCheckpoints:
                self.t_table.insert('', 'end', i, values=i)



    def updateTree(self):
        self.t_table.insert(parent='', index='end', values=self.mainapp.selectedCheckpoints[-1])

        

    def onClose(self):
        self.mainapp.selectedCheckpoints = []
        self.destroy()
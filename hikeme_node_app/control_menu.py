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

        self.geometry("500x450")
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

        self.goUntilStoppedChk = Checkbutton(self, text='GO UNTIL STOPPED', onvalue=1, offvalue=0)
        self.goUntilStoppedChk.grid(row = 1, column=0, sticky=NW)

        self.menuItemsFrame = Frame(self)
        self.label2 = Label(self.menuItemsFrame, text= "POST  x  CHECK-INS PER\nCHECKPOINT").grid(row = 1, column=0, sticky=N)
        self.checkInNumEntry = Entry(self.menuItemsFrame, width=5)
        self.checkInNumEntry.grid(row = 1, column = 2, sticky=N, padx=5, pady=5)

        self.label3 = Label(self.menuItemsFrame, text= "POST  x  WARNINGS PER\nCHECKPOINT").grid(row = 2, column=0, sticky=N)
        self.warningNumEntry = Entry(self.menuItemsFrame, width=5)
        self.warningNumEntry.grid(row = 2, column = 2, sticky=N, padx=5, pady=5)

        self.label4 = Label(self.menuItemsFrame, text= "NO. OF PROCESSES").grid(row = 3, column=0, sticky=N, padx=20, pady=15)
        self.processNumEntry = Entry(self.menuItemsFrame, width=5)
        self.processNumEntry.grid(row = 3, column = 2, sticky=N, padx=10, pady=15)
        
        self.menuItemsFrame.grid(row=0, column=0, sticky= NE)

        self.outputFeedBox = Text(self, height=9, width=60)
        self.outputFeedBox.grid(row = 2, column = 0, columnspan=1, sticky = S, padx = 5, pady=5)

        self.goButton = Button(self, text="GO", command=lambda: self.handleGoButton(self.checkInNumEntry.get(), self.warningNumEntry.get(), self.processNumEntry.get())).grid(row = 3, column=0, sticky=SW, padx=5)
        self.stopButton = Button(self, text="STOP").grid(row = 3, column=0, sticky=SE, padx=5)


    def handleGoButton(self, checkinN, warningN, processN):
        grabbedUserIDs = database.getNumPersonID(self.cur, warningN)
        grabbedUserIDsLength = len(grabbedUserIDs)

        if grabbedUserIDsLength < int(checkinN) or grabbedUserIDsLength < int(warningN):
            self.outputFeedBox.insert(END, ("ONLY %s USER IDs EXIST\n" % grabbedUserIDsLength))
            self.outputFeedBox.grid(row = 2, column = 0, columnspan=1, sticky = S, padx = 5, pady=5)
        
        if self.checkSelectedCheckPointIsEmpty():
            self.outputFeedBox.insert(END, ("NO CHECKPOINT(S) SELECTED!\n"))
            self.outputFeedBox.grid(row = 2, column = 0, columnspan=1, sticky = S, padx = 5, pady=5)
        else:
            self.createWarningInsertProcesses(int(warningN), int(processN), grabbedUserIDsLength)

    def checkSelectedCheckPointIsEmpty(self):
        if self.selectedCheckpoints is None or len(self.selectedCheckpoints) == 0:
            return True
        else:
            return False

    def createWarningInsertProcesses(self, warningN, processN, grabbedUserIDsLength):
        # add X warnings per N checkpoints spread over B processes
        async_results = []
        warningFile = utils.loadFile("warnings.txt", "r")

        self.profile = cProfile.Profile()
        self.profile.enable()

        with multiprocessing.Pool(processes=processN) as pool:
            for _ in range(warningN):
                async_results.append(pool.apply_async(database.insertWarning(self.selectedCheckpoints, grabbedUserIDsLength, warningFile)))
        pool.close()
        pool.join()

        self.profile.disable()
        self.profile.print_stats(sort='tottime')
 


    def loadInitTableElements(self):
        if self.selectedCheckpoints is not None:
            for i in self.selectedCheckpoints:
                self.t_table.insert('', 'end', i, values=i)



    def updateTree(self):
        self.t_table.insert(parent='', index='end', values=self.mainapp.selectedCheckpoints[-1])

        

    def onClose(self):
        self.mainapp.selectedCheckpoints = []
        self.destroy()
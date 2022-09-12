from distutils.log import warn
import multiprocessing
from tkinter import *
from tkinter import ttk
import database
import utils
import time


class ControlMenuWindow(Toplevel):
    def __init__(self, mainapp):
        super().__init__()
        self.mainapp = mainapp
        self.protocol("WM_DELETE_WINDOW", self.onClose)

        self.geometry("500x475")
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

        self.t_table.heading("checkpointIDcol", text="CHECKPOINT ID")
        self.t_table.grid(row = 0, column = 0, sticky = NSEW, padx = 5, pady = 5)
        self.t_scroll.grid(row=0, column=0, sticky=NS, padx = 50)
        self.listboxFrame.grid(row=0, column=0, columnspan=1, sticky = NW)

        self.removeButton = Button(self, text="REMOVE", command=self.handleRemoveButton).grid(row = 1, column = 0, sticky=SW, padx=5)
        self.clearButton = Button(self, text="CLEAR", command=self.handleClearButton).grid(row = 1, column = 0, sticky=SW, padx=160)

        self.menuItemsFrame = Frame(self)
        self.label2 = Label(self.menuItemsFrame, text= "POST  x  CHECK-INS per\nCHECKPOINT").grid(row = 1, column=0, sticky=N)
        self.checkInNumEntry = Entry(self.menuItemsFrame, width=5)
        self.checkInNumEntry.grid(row = 1, column = 2, sticky=N, padx=5, pady=5)

        self.label3 = Label(self.menuItemsFrame, text= "POST  x  WARNINGS per\nCHECKPOINT").grid(row = 2, column=0, sticky=N)
        self.warningNumEntry = Entry(self.menuItemsFrame, width=5)
        self.warningNumEntry.grid(row = 2, column = 2, sticky=N, padx=5, pady=5)

        self.label4 = Label(self.menuItemsFrame, text= "NO. OF PROCESSES").grid(row = 3, column=0, sticky=N, padx=20, pady=15)
        self.processNumEntry = Entry(self.menuItemsFrame, width=5)
        self.processNumEntry.grid(row = 3, column = 2, sticky=N, padx=10, pady=15)
        
        self.menuItemsFrame.grid(row=0, column=0, sticky= NE)

        self.outputFeedBox = Text(self, height=9, width=60)
        self.outputFeedBox.grid(row = 2, column = 0, columnspan=1, sticky = S, padx = 5, pady=5)

        self.goButton = Button(self, text="GO", width=50, command=lambda: self.handleGoButton(self.checkInNumEntry.get(), self.warningNumEntry.get(), self.processNumEntry.get())).grid(row = 3, column=0, sticky=S, padx=5)



    def handleRemoveButton(self):
        getTreeview = self.t_table.focus()
        treeviewSelectedItem = self.t_table.item(getTreeview)
        treeviewSelectedItemValue = treeviewSelectedItem.get('values')[0]
        print(treeviewSelectedItemValue)
        print(self.selectedCheckpoints)
        self.selectedCheckpoints.remove(str(treeviewSelectedItemValue))
        self.t_table.delete(self.t_table.selection()) 



    def handleClearButton(self):
        self.selectedCheckpoints = []
        self.mainapp.selectedCheckpoints = []
        self.t_table.delete(*self.t_table.get_children())



    def handleGoButton(self, checkinN, warningN, processN):
        if warningN <= checkinN:
            grabbedUserIDs = database.getNumPersonID(self.cur, checkinN)
        else:
            grabbedUserIDs = database.getNumPersonID(self.cur, warningN)
            
        grabbedUserIDsLength = len(grabbedUserIDs)

        if grabbedUserIDsLength < int(checkinN) or grabbedUserIDsLength < int(warningN):
            self.updateTextBox(("ONLY %s USER IDs EXIST\n" % grabbedUserIDsLength))
        
        if self.checkSelectedCheckPointIsEmpty():
            self.updateTextBox(("NO CHECKPOINT(S) SELECTED!\n"))
        else:
            self.createProcesses(int(warningN), int(checkinN), int(processN), grabbedUserIDsLength)

                


    def createProcesses(self, warningN, checkInN, processN, grabbedUserIDsLength):
            # add X warnings per N checkpoints spread over B processes
            async_results_warnings = []
            async_results_check_ins = []

            warningFile = utils.loadFile("warnings.txt")
            statusFile = utils.loadFile("statuses.txt")

            start = time.process_time()
            if warningN is not None or warningN != 0:
                with multiprocessing.Pool(processes=processN) as pool:
                    for _ in range(warningN):
                        async_results_warnings.append(pool.apply_async(database.insertWarning(self.selectedCheckpoints, grabbedUserIDsLength, warningFile)))
            timeTaken = (time.process_time() - start)
            self.updateTextBox((f"TIME TAKEN: {timeTaken} seconds to INSERT {warningN} warnings.\n"))

            start = time.process_time()
            if checkInN is not None or checkInN != 0: 
                with multiprocessing.Pool(processes=processN) as pool:
                    for _ in range(checkInN):
                        async_results_check_ins.append(pool.apply_async(database.insertCheckIn(self.selectedCheckpoints, grabbedUserIDsLength, statusFile)))
            timeTaken = (time.process_time() - start)
            self.updateTextBox((f"TIME TAKEN: {timeTaken} seconds to CREATE and UPDATE {checkInN} user statuses.\n"))



    def checkSelectedCheckPointIsEmpty(self):
        if self.selectedCheckpoints is None or len(self.selectedCheckpoints) == 0:
            return True
        else:
            return False


    def updateTextBox(self, text):
        self.outputFeedBox.insert(END, text)
        self.outputFeedBox.grid(row = 2, column = 0, columnspan=1, sticky = S, padx = 5, pady=5)


    def handleAddButton(self):
        # allow superuser to update just one particular user status and warning using 1 checkpoint
        # get all user ID's in drop down (with search?)
        # click on one selected checkpoint in treeview
        # type in a warning
        # type in a status
        # insert warning and status for selected person ID
        # update person status ID and current checkpoint
        pass


    def loadInitTableElements(self):
        if self.selectedCheckpoints is not None:
            for i in self.selectedCheckpoints:
                self.t_table.insert('', 'end', i, values=i)




    def updateTree(self):
        self.t_table.insert(parent='', index='end', values=self.mainapp.selectedCheckpoints[-1])

        

    def onClose(self):
        self.mainapp.selectedCheckpoints = []
        self.destroy()
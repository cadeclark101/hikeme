from tkinter import *
from tkinter import ttk


class win1:
    def __init__(self, master):
        self.master = master
        self.master.geometry('200x200+0+0')
        # Initialize app (second window)
        self.app = None

        self.fullname = StringVar()
        self.age = StringVar()

        self.example_lst = [('John', 12), ('Hannah', 10)]

        self.lblname = Label(self.master, text='Name:')
        self.lblname.pack()
        self.entryname = Entry(self.master, textvariable=self.fullname)
        self.entryname.pack()

        self.lblage = Label(self.master, text='Age:')
        self.lblage.pack()
        self.entryage = Entry(self.master, textvariable=self.age)
        self.entryage.pack()

        self.btn1 = Button(self.master, text='Submit', command=self.submit)
        self.btn1.pack()

        self.btn2 = Button(self.master, text='Open window', command=self.openwin)
        self.btn2.pack()

    def submit(self):
        self.example_lst.append((self.fullname.get(), self.age.get()))
        self.fullname.set('')
        self.age.set('')
        # Add update to app in the submit button.
        if self.app is not None:
            self.app.update_tree()

    def openwin(self):
        openwin2 = Toplevel(self.master)
        self.app = win2(openwin2, self)


class win2:
    def __init__(self, master, mainwin):
        self.master = master
        self.mainwin = mainwin
        self.master.geometry('300x300+100+100')

        self.t_scroll = Scrollbar(self.master)
        self.t_scroll.pack(side=RIGHT, fill=Y)
        self.t_table = ttk.Treeview(self.master, yscrollcommand=self.t_scroll.set)

        self.t_scroll.config(command=self.t_table.yview)

        self.t_table['column'] = ('Name', 'Age')

        self.t_table.column('#0', width=0, stretch=NO)
        self.t_table.column('Name', width=50, minwidth=30)
        self.t_table.column('Age', width=30, minwidth=30)

        headings = ['#0', 'Name', 'Age']
        txt_headings = ['', 'Name', 'Age']
        for heading in zip(headings, txt_headings):
            self.t_table.heading(heading[0], text=f'{heading[1]}', anchor=W)

        # Initialize the example list data.
        self.load_init()

        self.t_table.pack()

    def load_init(self):
        for x in range(len(self.t_table.children), len(self.mainwin.example_lst)):
            self.t_table.insert(parent='', index='end', values=self.mainwin.example_lst[x])

    def update_tree(self):
        self.t_table.insert(parent='', index='end', values=self.mainwin.example_lst[-1])




def main():
    root = Tk()
    app = win1(root)
    root.mainloop()


if __name__ == '__main__':
    main()

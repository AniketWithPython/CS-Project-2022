#Use appropiate query as per student year

import tkinter as tk
import tkinter.font as tkFont
import tksheet
import datetime

yeardata=[]
class App:
    def __init__(self, root):
        global data
        #setting title
        root.title("Room")
        #setting window size
        width=631
        height=389
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg="#282424")

        GButton_856=tk.Button(root)
        GButton_856["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_856["font"] = ft
        GButton_856["fg"] = "#FFFFFF"
        GButton_856["justify"] = "center"
        GButton_856["text"] = "Back"
        GButton_856.place(x=510,y=330,width=87,height=31)
        GButton_856["command"] = self.GButton_856_command

        sheet=tksheet.Sheet(root)
        sheet.pack(fill="both",expand=False)
        #replace sample with actual data
        sheet.set_sheet_data(yeardata)


    def GButton_856_command(self):
        root.destroy()

def roomview_screen():
    global root
    root = tk.Toplevel()
    app = App(root)
    root.mainloop()

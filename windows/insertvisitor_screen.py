import tkinter as tk
import tkinter.font as tkFont
from datetime import datetime
import database_controller
class App:
    def __init__(self, root):
        global GLineEdit_624,GLineEdit_824,GLineEdit_992
        #setting title
        root.title("Insert")
        #setting window size
        width=390
        height=388
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
        GButton_856["bg"] = "#282424"
        GButton_856["justify"] = "center"
        GButton_856["text"] = "Cancel"
        GButton_856.place(x=260,y=290,width=87,height=31)
        GButton_856["command"] = self.GButton_856_command

        GLabel_671=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_671["font"] = ft
        GLabel_671["fg"] = "#FFFFFF"
        GLabel_671["bg"] = "#282424"
        GLabel_671["justify"] = "center"
        GLabel_671["text"] = "ID:"
        GLabel_671.place(x=70,y=40,width=85,height=30)

        GLabel_215=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_215["font"] = ft
        GLabel_215["fg"] = "#FFFFFF"
        GLabel_215["bg"] = "#282424"
        GLabel_215["justify"] = "center"
        GLabel_215["text"] = "Room ID:"
        GLabel_215.place(x=80,y=90,width=80,height=30)

        GButton_199=tk.Button(root)
        GButton_199["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_199["font"] = ft
        GButton_199["fg"] = "#FFFFFF"
        GButton_199["bg"] = "#282424"
        GButton_199["justify"] = "center"
        GButton_199["text"] = "Insert"
        GButton_199.place(x=50,y=290,width=87,height=31)
        GButton_199["command"] = self.GButton_199_command

        GLabel_9=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_9["font"] = ft
        GLabel_9["fg"] = "#FFFFFF"
        GLabel_9["bg"] = "#282424"
        GLabel_9["justify"] = "center"
        GLabel_9["text"] = "Visitor Name:"
        GLabel_9.place(x=60,y=150,width=120,height=25)

        GLabel_593=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_593["font"] = ft
        GLabel_593["fg"] = "#FFFFFF"
        GLabel_593["bg"] = "#282424"
        GLabel_593["justify"] = "center"
        GLabel_593["text"] = "Check-in time:"
        GLabel_593.place(x=60,y=210,width=121,height=30)

        GLineEdit_624=tk.Entry(root)
        GLineEdit_624["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        GLineEdit_624["font"] = ft
        GLineEdit_624["fg"] = "#FFFFFF"
        GLineEdit_624["bg"] = "#282424"
        GLineEdit_624["justify"] = "center"
        GLineEdit_624.place(x=220,y=40,width=140,height=25)

        GLineEdit_824=tk.Entry(root)
        GLineEdit_824["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        GLineEdit_824["font"] = ft
        GLineEdit_824["fg"] = "#FFFFFF"
        GLineEdit_824["bg"] = "#282424"
        GLineEdit_824["justify"] = "center"
        GLineEdit_824.place(x=220,y=90,width=140,height=25)

        GLineEdit_992=tk.Entry(root)
        GLineEdit_992["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        GLineEdit_992["font"] = ft
        GLineEdit_992["fg"] = "#FFFFFF"
        GLineEdit_992["bg"] = "#282424"
        GLineEdit_992["justify"] = "center"
        GLineEdit_992.place(x=220,y=150,width=140,height=25)

        GLabel_905=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_905["font"] = ft
        GLabel_905["fg"] = "#FFFFFF"
        GLabel_905["bg"] = "#282424"
        GLabel_905["justify"] = "center"
        GLabel_905["text"] = datetime.now().strftime(r'%H:%M:%S')
        GLabel_905.place(x=220,y=210,width=140,height=25)

    def GButton_856_command(self):  #cancel
        root.destroy()


    def GButton_199_command(self):  #insert
        data=(GLineEdit_992.get(),datetime.now().strftime(r'%H:%M:%S'),GLineEdit_824.get(),GLineEdit_624.get())
        root.destroy()
        database_controller.insertvisitor(data)

def insertvisitor_screen():
    global root
    root = tk.Toplevel()
    app = App(root)
    root.mainloop()

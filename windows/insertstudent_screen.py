import tkinter as tk
import tkinter.font as tkFont
import database_controller

class App:
    def __init__(self, root):
        global GLineEdit_298,GLineEdit_313,GLineEdit_58,GLineEdit_585,GLineEdit_73,GLineEdit_82,GLineEdit_9
        #setting title
        root.title("Insert")
        #setting window size
        width=390
        height=483
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg="#282424")

        GButton_466=tk.Button(root)
        GButton_466["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_466["font"] = ft
        GButton_466["fg"] = "#FFFFFF"
        GButton_466["justify"] = "center"
        GButton_466["text"] = "Insert"
        GButton_466.place(x=40,y=400,width=87,height=31)
        GButton_466["command"] = self.GButton_466_command

        GButton_698=tk.Button(root)
        GButton_698["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_698["font"] = ft
        GButton_698["fg"] = "#FFFFFF"
        GButton_698["justify"] = "center"
        GButton_698["text"] = "Cancel"
        GButton_698.place(x=260,y=400,width=87,height=31)
        GButton_698["command"] = self.GButton_698_command

        GLabel_650=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_650["font"] = ft
        GLabel_650["fg"] = "#FFFFFF"
        GLabel_650["bg"] = "#282424"
        GLabel_650["justify"] = "center"
        GLabel_650["text"] = "ID"
        GLabel_650.place(x=80,y=60,width=70,height=25)

        GLabel_58=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_58["font"] = ft
        GLabel_58["fg"] = "#FFFFFF"
        GLabel_58["bg"] = "#282424"
        GLabel_58["justify"] = "center"
        GLabel_58["text"] = "Name"
        GLabel_58.place(x=80,y=100,width=70,height=25)

        GLabel_466=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_466["font"] = ft
        GLabel_466["fg"] = "#FFFFFF"
        GLabel_466["bg"] = "#282424"
        GLabel_466["justify"] = "center"
        GLabel_466["text"] = "Parent"
        GLabel_466.place(x=80,y=140,width=70,height=25)

        GLabel_41=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_41["font"] = ft
        GLabel_41["fg"] = "#FFFFFF"
        GLabel_41["bg"] = "#282424"
        GLabel_41["justify"] = "center"
        GLabel_41["text"] = "Department"
        GLabel_41.place(x=60,y=180,width=108,height=30)

        GLabel_913=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_913["font"] = ft
        GLabel_913["fg"] = "#FFFFFF"
        GLabel_913["bg"] = "#282424"
        GLabel_913["justify"] = "center"
        GLabel_913["text"] = "Age"
        GLabel_913.place(x=80,y=220,width=70,height=25)

        GLabel_537=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_537["font"] = ft
        GLabel_537["fg"] = "#FFFFFF"
        GLabel_537["bg"] = "#282424"
        GLabel_537["justify"] = "center"
        GLabel_537["text"] = "DOB(YYYY/MM/DD)"
        GLabel_537.place(x=10,y=260,width=206,height=30)

        GLabel_290=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_290["font"] = ft
        GLabel_290["fg"] = "#FFFFFF"
        GLabel_290["bg"] = "#282424"
        GLabel_290["justify"] = "center"
        GLabel_290["text"] = "Year"
        GLabel_290.place(x=80,y=300,width=70,height=25)

        GLineEdit_58=tk.Entry(root)
        GLineEdit_58["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        GLineEdit_58["font"] = ft
        GLineEdit_58["fg"] = "#FFFFFF"
        GLineEdit_58["bg"] = "#282424"
        GLineEdit_58["justify"] = "center"
        GLineEdit_58.place(x=220,y=60,width=140,height=25)

        GLineEdit_73=tk.Entry(root)
        GLineEdit_73["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        GLineEdit_73["font"] = ft
        GLineEdit_73["fg"] = "#FFFFFF"
        GLineEdit_73["bg"] = "#282424"
        GLineEdit_73["justify"] = "center"
        GLineEdit_73.place(x=220,y=100,width=140,height=25)

        GLineEdit_82=tk.Entry(root)
        GLineEdit_82["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        GLineEdit_82["font"] = ft
        GLineEdit_82["fg"] = "#FFFFFF"
        GLineEdit_82["bg"] = "#282424"
        GLineEdit_82["justify"] = "center"
        GLineEdit_82.place(x=220,y=140,width=140,height=25)

        GLineEdit_298=tk.Entry(root)
        GLineEdit_298["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        GLineEdit_298["font"] = ft
        GLineEdit_298["fg"] = "#FFFFFF"
        GLineEdit_298["bg"] = "#282424"
        GLineEdit_298["justify"] = "center"
        GLineEdit_298.place(x=220,y=220,width=140,height=25)

        GLineEdit_9=tk.Entry(root)
        GLineEdit_9["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        GLineEdit_9["font"] = ft
        GLineEdit_9["fg"] = "#FFFFFF"
        GLineEdit_9["bg"] = "#282424"
        GLineEdit_9["justify"] = "center"
        GLineEdit_9.place(x=220,y=260,width=140,height=25)

        GLineEdit_313=tk.Entry(root)
        GLineEdit_313["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        GLineEdit_313["font"] = ft
        GLineEdit_313["fg"] = "#FFFFFF"
        GLineEdit_313["bg"] = "#282424"
        GLineEdit_313["justify"] = "center"
        GLineEdit_313.place(x=220,y=180,width=140,height=25)

        GLineEdit_585=tk.Entry(root)
        GLineEdit_585["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        GLineEdit_585["font"] = ft
        GLineEdit_585["fg"] = "#FFFFFF"
        GLineEdit_585["bg"] = "#282424"
        GLineEdit_585["justify"] = "center"
        GLineEdit_585.place(x=220,y=300,width=140,height=25)

    def GButton_466_command(self):  #insert
        data=(GLineEdit_58.get(),GLineEdit_73.get(),GLineEdit_82.get(),GLineEdit_313.get(),GLineEdit_298.get(),GLineEdit_9.get(),GLineEdit_585.get())
        database_controller.insertstudent(data)
        root.destroy()
    
    def GButton_698_command(self):  #cancel
        root.destroy()

def insertstudent_screen():
    global root
    root = tk.Toplevel()
    app = App(root)
    root.mainloop()
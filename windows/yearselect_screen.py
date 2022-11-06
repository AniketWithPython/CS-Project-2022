import tkinter as tk
import tkinter.font as tkFont
import database_controller
import windows

class App:
    def __init__(self, root):
        #setting title
        root.title("Rooms")
        #setting window size
        width=389
        height=229
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
        GButton_856["text"] = "Year 4"
        GButton_856.place(x=240,y=150,width=87,height=31)
        GButton_856["command"] = self.GButton_856_command

        GButton_199=tk.Button(root)
        GButton_199["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_199["font"] = ft
        GButton_199["fg"] = "#FFFFFF"
        GButton_199["justify"] = "center"
        GButton_199["text"] = "Year 3"
        GButton_199.place(x=60,y=150,width=87,height=31)
        GButton_199["command"] = self.GButton_199_command

        GButton_803=tk.Button(root)
        GButton_803["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_803["font"] = ft
        GButton_803["fg"] = "#FFFFFF"
        GButton_803["justify"] = "center"
        GButton_803["text"] = "Year 1"
        GButton_803.place(x=60,y=50,width=87,height=31)
        GButton_803["command"] = self.GButton_803_command

        GButton_59=tk.Button(root)
        GButton_59["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_59["font"] = ft
        GButton_59["fg"] = "#FFFFFF"
        GButton_59["justify"] = "center"
        GButton_59["text"] = "Year 2"
        GButton_59.place(x=240,y=50,width=87,height=31)
        GButton_59["command"] = self.GButton_59_command

    def GButton_856_command(self):  #year 4
        show(4)


    def GButton_199_command(self):  #year 3
        show(3)

    def GButton_803_command(self):  #year 1
        show(1)

    def GButton_59_command(self):   #year 2
        show(2)

    
def show(click):
    windows.yeardata=database_controller.viewroom(click)
    windows.roomview_screen()


def yearselect_screen():
    root = tk.Toplevel()
    app = App(root)
    root.mainloop()

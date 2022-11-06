import tkinter as tk
import tkinter.font as tkFont
import windows


class App:
    def __init__(self, root):
        #setting title
        root.title("Hostel Managenemt System")
        #setting window size
        width=538
        height=312
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg="#282424")

        GButton_780=tk.Button(root)
        GButton_780["bg"] = "#363636"
        ft = tkFont.Font(family='Times',size=16)
        GButton_780["font"] = ft
        GButton_780["fg"] = "#FFFFFF"
        GButton_780["justify"] = "center"
        GButton_780["text"] = "Start"
        GButton_780.place(x=220,y=230,width=87,height=31)
        GButton_780["command"] = self.GButton_780_command

        GLabel_212=tk.Label(root)
        GLabel_212["anchor"] = "nw"
        ft = tkFont.Font(family='Times',size=28)
        GLabel_212["font"] = ft
        GLabel_212["fg"] = "#FFFFFF"
        GLabel_212["bg"] = "#282424"
        GLabel_212["justify"] = "center"
        GLabel_212["text"] = "Hostel Management System"
        GLabel_212.place(x=70,y=50,width=414,height=47)

        GLabel_333=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_333["font"] = ft
        GLabel_333["fg"] = "#FFFFFF"
        GLabel_333["bg"] = "#282424"
        GLabel_333["justify"] = "center"
        GLabel_333["text"] = "XYZ Boys Hostel"
        GLabel_333.place(x=140,y=120,width=254,height=39)

    def GButton_780_command(self):
        root.destroy()
        windows.details_screen()

def start_screen():
    global root
    root = tk.Tk()
    app = App(root)
    root.mainloop()

    
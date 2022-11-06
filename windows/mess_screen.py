import tkinter as tk
import tkinter.font as tkFont
import windows

class App:
    def __init__(self, root):
        #setting title
        root.title("Mess")
        #setting window size
        width=404
        height=234
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
        GButton_856["text"] = "Back"
        GButton_856.place(x=290,y=160,width=87,height=31)
        GButton_856["command"] = self.GButton_856_command

        GLabel_671=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_671["font"] = ft
        GLabel_671["fg"] = "#FFFFFF"
        GLabel_671["bg"] = "#282424"
        GLabel_671["justify"] = "center"
        GLabel_671["text"] = "Basic Pay:"
        GLabel_671.place(x=90,y=80,width=85,height=30)

        GLabel_215=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_215["font"] = ft
        GLabel_215["fg"] = "#FFFFFF"
        GLabel_215["bg"] = "#282424"
        GLabel_215["justify"] = "center"
        GLabel_215["text"] = 5000
        GLabel_215.place(x=220,y=80,width=70,height=25)

        GLabel_662=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_662["font"] = ft
        GLabel_662["fg"] = "#FFFFFF"
        GLabel_662["bg"] = "#282424"
        GLabel_662["justify"] = "center"
        GLabel_662["text"] = "Mess"
        GLabel_662.place(x=160,y=20,width=70,height=25)

        GButton_791=tk.Button(root)
        GButton_791["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_791["font"] = ft
        GButton_791["fg"] = "#FFFFFF"
        GButton_791["justify"] = "center"
        GButton_791["text"] = "Canteen"
        GButton_791.place(x=30,y=160,width=87,height=31)
        GButton_791["command"] = self.GButton_791_command

        '''GButton_199=tk.Button(root)
        GButton_199["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_199["font"] = ft
        GButton_199["fg"] = "#FFFFFF"
        GButton_199["justify"] = "center"
        GButton_199["text"] = "Mess Fee"
        GButton_199.place(x=160,y=160,width=87,height=31)
        GButton_199["command"] = self.GButton_199_command'''

    def GButton_856_command(self):
        root.destroy()

    def GButton_791_command(self):
        windows.canteenview_screen()

    def GButton_199_command(self):
        print("command")

def mess_screen():
    global root
    root = tk.Toplevel()
    app = App(root)
    root.mainloop()
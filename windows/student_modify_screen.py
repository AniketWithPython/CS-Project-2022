import tkinter as tk
import tkinter.font as tkFont
import windows

class App:
    def __init__(self, root):
        #setting title
        root.title("Modify Records")
        #setting window size
        width=269
        height=156
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
        GButton_466["text"] = "Add"
        GButton_466.place(x=90,y=30,width=87,height=31)
        GButton_466["command"] = self.GButton_466_command

        GButton_698=tk.Button(root)
        GButton_698["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_698["font"] = ft
        GButton_698["fg"] = "#FFFFFF"
        GButton_698["justify"] = "center"
        GButton_698["text"] = "Delete"
        GButton_698.place(x=90,y=80,width=87,height=31)
        GButton_698["command"] = self.GButton_698_command

    def GButton_466_command(self):  #add
        windows.insertstudent_screen()


    def GButton_698_command(self):  #remove
        windows.student_delete_screen()

def student_modify_screen():
    root = tk.Toplevel()
    app = App(root)
    root.mainloop()

import tkinter as tk
import tkinter.font as tkFont
import windows

class App:
    def __init__(self, root):
        #setting title
        root.title("Students")
        #setting window size
        width=404
        height=234
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg="#282424")

        GLabel_212=tk.Label(root)
        GLabel_212["anchor"] = "nw"
        ft = tkFont.Font(family='Times',size=28)
        GLabel_212["font"] = ft
        GLabel_212["fg"] = "#FFFFFF"
        GLabel_212["bg"] = "#282424"
        GLabel_212["justify"] = "center"
        GLabel_212["text"] = "Students"
        GLabel_212.place(x=138,y=20,width=132,height=40)

        GButton_823=tk.Button(root)
        GButton_823["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_823["font"] = ft
        GButton_823["fg"] = "#FFFFFF"
        GButton_823["justify"] = "center"
        GButton_823["text"] = "View"
        GButton_823.place(x=30,y=160,width=87,height=31)
        GButton_823["command"] = self.GButton_823_command

        GButton_48=tk.Button(root)
        GButton_48["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_48["font"] = ft
        GButton_48["fg"] = "#FFFFFF"
        GButton_48["justify"] = "center"
        GButton_48["text"] = "Modify"
        GButton_48.place(x=160,y=160,width=87,height=31)
        GButton_48["command"] = self.GButton_48_command

        GButton_769=tk.Button(root)
        GButton_769["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_769["font"] = ft
        GButton_769["fg"] = "#FFFFFF"
        GButton_769["justify"] = "center"
        GButton_769["text"] = "Back"
        GButton_769.place(x=290,y=160,width=87,height=31)
        GButton_769["command"] = self.GButton_769_command

    def GButton_823_command(self):  #view
        windows.studentsview_screen()

    def GButton_48_command(self):   #modify
        windows.student_modify_screen()

    def GButton_769_command(self):  #back
        root.destroy()

def students_screen():
    global root
    root = tk.Toplevel()
    app = App(root)
    root.mainloop()

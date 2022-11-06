import tkinter as tk
import tkinter.font as tkFont
import database_controller
class App:
    def __init__(self, root):
        global GLineEdit_117
        #setting title
        root.title("Delete")
        #setting window size
        width=389
        height=229
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg="#282424")

        GButton_199=tk.Button(root)
        GButton_199["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=16)
        GButton_199["font"] = ft
        GButton_199["fg"] = "#FFFFFF"
        GButton_199["bg"] = "#282424"
        GButton_199["justify"] = "center"
        GButton_199["text"] = "Delete"
        GButton_199.place(x=150,y=150,width=87,height=31)
        GButton_199["command"] = self.GButton_199_command

        GLabel_477=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_477["font"] = ft
        GLabel_477["fg"] = "#FFFFFF"
        GLabel_477["bg"] = "#282424"
        GLabel_477["justify"] = "center"
        GLabel_477["text"] = "Student ID:"
        GLabel_477.place(x=60,y=70,width=109,height=30)

        GLineEdit_117=tk.Entry(root)
        GLineEdit_117["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        GLineEdit_117["font"] = ft
        GLineEdit_117["fg"] = "#FFFFFF"
        GLineEdit_117["bg"] = "#282424"
        GLineEdit_117["justify"] = "center"
        GLineEdit_117["text"] = "Entry"
        GLineEdit_117.place(x=230,y=70,width=100,height=25)

    def GButton_199_command(self):
        database_controller.deletestudent(GLineEdit_117.get())
        root.destroy()

def student_delete_screen():
    global root
    root = tk.Toplevel()
    app = App(root)
    root.mainloop()

import tkinter as tk
import tkinter.font as tkFont
import windows
class App:
    def __init__(self, root):
        #setting title
        root.title("Details")
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
        GButton_780["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_780["font"] = ft
        GButton_780["fg"] = "#FFFFFF"
        GButton_780["justify"] = "center"
        GButton_780["text"] = "Room"
        GButton_780.place(x=230,y=240,width=87,height=31)
        GButton_780["command"] = self.GButton_780_command

        GLabel_212=tk.Label(root)
        GLabel_212["anchor"] = "nw"
        ft = tkFont.Font(family='Times',size=28)
        GLabel_212["font"] = ft
        GLabel_212["fg"] = "#FFFFFF"
        GLabel_212["bg"] = "#282424"
        GLabel_212["justify"] = "center"
        GLabel_212["text"] = "Details"
        GLabel_212.place(x=210,y=30,width=106,height=36)

        GButton_823=tk.Button(root)
        GButton_823["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_823["font"] = ft
        GButton_823["fg"] = "#FFFFFF"
        GButton_823["justify"] = "center"
        GButton_823["text"] = "Students"
        GButton_823.place(x=130,y=240,width=87,height=31)
        GButton_823["command"] = self.GButton_823_command

        GButton_609=tk.Button(root)
        GButton_609["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_609["font"] = ft
        GButton_609["fg"] = "#FFFFFF"
        GButton_609["justify"] = "center"
        GButton_609["text"] = "Quit"
        GButton_609.place(x=430,y=240,width=87,height=31)
        GButton_609["command"] = self.GButton_609_command

        GButton_856=tk.Button(root)
        GButton_856["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_856["font"] = ft
        GButton_856["fg"] = "#FFFFFF"
        GButton_856["justify"] = "center"
        GButton_856["text"] = "Mess"
        GButton_856.place(x=330,y=240,width=87,height=31)
        GButton_856["command"] = self.GButton_856_command

        GButton_48=tk.Button(root)
        GButton_48["bg"] = "#282424"
        ft = tkFont.Font(family='Times',size=16)
        GButton_48["font"] = ft
        GButton_48["fg"] = "#FFFFFF"
        GButton_48["justify"] = "center"
        GButton_48["text"] = "Visitor"
        GButton_48.place(x=30,y=240,width=87,height=31)
        GButton_48["command"] = self.GButton_48_command

        GLabel_160=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_160["font"] = ft
        GLabel_160["fg"] = "#FFFFFF"
        GLabel_160["bg"] = "#282424"
        GLabel_160["justify"] = "center"
        GLabel_160["text"] = "Rooms:"
        GLabel_160.place(x=80,y=90,width=70,height=25)

        GLabel_496=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_496["font"] = ft
        GLabel_496["fg"] = "#FFFFFF"
        GLabel_496["bg"] = "#282424"
        GLabel_496["justify"] = "center"
        GLabel_496["text"] = "Students:"
        GLabel_496.place(x=80,y=130,width=75,height=25)

        GLabel_824=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_824["font"] = ft
        GLabel_824["fg"] = "#FFFFFF"
        GLabel_824["bg"] = "#282424"
        GLabel_824["justify"] = "center"
        GLabel_824["text"] = "Annual Expenses:"
        GLabel_824.place(x=40,y=170,width=148,height=30)

        GLabel_448=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_448["font"] = ft
        GLabel_448["fg"] = "#FFFFFF"
        GLabel_448["bg"] = "#282424"
        GLabel_448["justify"] = "center"
        GLabel_448["text"] = 300
        GLabel_448.place(x=380,y=90,width=70,height=25)

        GLabel_279=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_279["font"] = ft
        GLabel_279["fg"] = "#FFFFFF"
        GLabel_279["bg"] = "#282424"
        GLabel_279["justify"] = "center"
        GLabel_279["text"] = "[students]"
        GLabel_279.place(x=380,y=130,width=70,height=25)

        GLabel_8=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_8["font"] = ft
        GLabel_8["fg"] = "#FFFFFF"
        GLabel_8["bg"] = "#282424"
        GLabel_8["justify"] = "center"
        GLabel_8["text"] = "[expenses]"
        GLabel_8.place(x=380,y=170,width=70,height=25)

    def GButton_780_command(self):  #rooms
        windows.yearselect_screen()


    def GButton_823_command(self):  #students
        windows.students_screen()


    def GButton_609_command(self):  #quit
        root.destroy()


    def GButton_856_command(self):  #mess
        windows.mess_screen()


    def GButton_48_command(self):   #visitor
        windows.visitor_screen()

def details_screen():
    global root
    root = tk.Tk()
    app = App(root)
    root.mainloop()


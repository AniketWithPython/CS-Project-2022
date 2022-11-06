import tkinter as tk
def cmd():
    print(entry.get())
app=tk.Tk()
entry=tk.Entry()
entry.pack()
btn=tk.Button(text="click",command=cmd)
btn.pack()
app.mainloop()


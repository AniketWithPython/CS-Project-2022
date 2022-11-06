#didn't work :')

import tkinter as tk
def cmd():
    print(var.get())
win=tk.Tk()
canvas=tk.Canvas(win)
sb=tk.Scrollbar(win,orient='vertical',command=canvas.yview)
var=tk.StringVar()
l=["abc"+str(i) for i in range(1,16)]
for i in l:
    rd=tk.Radiobutton(text=i,variable=var,value=i,command=cmd)
    canvas.create_window(0,int(i[-1])*40,anchor='nw',window=rd,height=50)

canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=sb.set)
canvas.pack(fill='both', expand=True, side='left')
sb.pack(side='right',fill='y')
win.mainloop()
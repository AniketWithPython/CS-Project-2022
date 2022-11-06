import tkinter as tk
i=0
def comd():
    global label,i
    i+=1
    label.config(text=f'Testing{i}')

app=tk.Tk()
label=tk.Label(text=f'Testing{i}')
label.pack()
button=tk.Button(text='refresh',command=comd)
button.pack()
app.mainloop()

from tkinter import *
root =Tk()
entry = Entry(root,fg='white',bg='black',borderwidth=10)
entry.grid(row=0,column=0)
entry.insert(0,"ENTRY YOUR NAME")
def myClick():
    global entry
    
    label=Label(root,text = "HELLO "+ entry.get()+"!!")
    label.grid(row=22,column=0)

but = Button(root , text= " ENTER YOUR NAME ", command=myClick, fg='white',bg='red',padx=50)
but.grid(row=1,column=0)

root.mainloop()


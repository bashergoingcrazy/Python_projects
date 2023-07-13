from tkinter import *
root = Tk()

def myClick():
    label = Label(root , text=" LOOK YOU CLICKED ").grid(row=3,column=0)
    




x = Label(root,text="YO WHAT's UP WORLD").grid(row=0,column=0)
y = Button(root, text = "CLICK ME! ", command=myClick,fg='blue',bg='red').grid(row=1, column=0)
root.mainloop()

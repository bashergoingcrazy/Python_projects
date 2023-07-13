from tkinter import *

from PIL import ImageTk,Image
root=Tk()
root.title(" Using Frames ")

frame = LabelFrame(root,padx=50,pady=50)
frame.pack(padx=10,pady=10)


b = Button(frame,text= "Don't Click Here!")
b2 = Button(frame,text= "OR Here")
b.grid(row=0,column=0,padx=15,pady=15)
b2.grid(row=0,column=1,padx=20,pady=20)
root.mainloop()

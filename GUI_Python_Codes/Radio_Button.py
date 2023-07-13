from tkinter import *
from PIL import ImageTk,Image

root =Tk()
root.title('Using Radio Buttons ')
modes =[
    ("Pepperoni","Pepperoni"),
    ("Chesse","Chesse"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text,mode in modes:
    Radiobutton(root,text=text, variable=pizza,value=mode).pack(anchor=W)







def clicked(value):
    mylabel1 = Label(root,text=pizza.get()).pack()

myButton =Button(root,text="Click Me!",command = lambda:clicked(pizza.get()))
myButton.pack()



#r = IntVar()
#r.set("2")
#Radiobutton(root,text="option 1",variable=r,value=1,command = lambda:clicked(r.get())).pack()
#Radiobutton(root,text="option 2",variable=r,value=2,command = lambda:clicked(r.get())).pack()

root.mainloop() 


# my first test
from tkinter import *
root=Tk()

num1=float(input("Enter your first number here :"))
num2=float(input("Enter your second number here :"))
tp=num1+num2
mri=str(tp)
mylabel=Label(root,text="The sum of your numbers are; "+mri)
mylabel.pack()
root.mainloop()

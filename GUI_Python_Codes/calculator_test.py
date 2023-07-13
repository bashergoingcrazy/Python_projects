#Importing Tkinter
from tkinter import *

#Creating the root screen
root = Tk()
root.title("Simple Calculator")
i = 0
num = ''
def clickzero():
    global i
    e.insert(i,0)
    i+=1
def clickone():
    global num
    global i
    e.insert(i,1)
    num+='1'
    i+=1
def clicktwo():
    global i
    global num
    e.insert(i,2)
    num+='2'
    i+=1
def clickthree():
    global num
    global i
    e.insert(i,3)
    num+='3'
    i+=1
def clickfour():
    global num
    global i
    e.insert(i,4)
    num+='4'
    i+=1
def clickfive():
    global num
    global i
    e.insert(i,5)
    num+='5'
    i+=1
def clicksix():
    global i
    global num
    e.insert(i,6)
    num+='6'
    i+=1
def clickseven():
    global i
    global num
    e.insert(i,7)
    num+='7'
    i+=1
def clickeight():
    global i
    global num
    e.insert(i,8)
    i+=1
    num+='8'
def clicknine():
    global i
    global num
    e.insert(i,9)
    i+=1
    num+='9'
def clickback():
    global i
    e.delete(i-1)
    i-=1
def clickclear():
    global i
    e.delete(0,'end')
    i=0
    
def clickadd():
    global i
    global l
    l=int(e.get())
    clickclear()

def clickequals():
    global i
    global l
    m=int(e.get())
    k=l+m
    clickclear()
    e.insert(0,k)




e = Entry(root,borderwidth=10,width=50)
e.grid(row=0,column=0)

seven = Button(root, text=" 7 ", padx=20,pady=20,command=clickseven)
seven.grid(row=0,column=1)

eight = Button(root, text=" 8 ", padx=20,pady=20,command=clickeight)
eight.grid(row=0,column=2)

nine = Button(root, text=" 9 ", padx=20,pady=20,command=clicknine)
nine.grid(row=0,column=3)

four = Button(root, text=" 4 ", padx=20,pady=20,command=clickfour)
four.grid(row=1,column=1)

five = Button(root, text=" 5 ", padx=20,pady=20,command=clickfive)
five.grid(row=1,column=2)

six = Button(root, text=" 6 ", padx=20,pady=20,command = clicksix)
six.grid(row=1,column=3)

one = Button(root, text=" 1 ", padx=20,pady=20, command = clickone)
one.grid(row=2,column=1)

two = Button(root, text=" 2 ", padx=20,pady=20,command = clicktwo)
two.grid(row=2,column=2)

three = Button(root, text=" 3 ", padx=20,pady=20, command = clickthree)
three.grid(row=2,column=3)

add = Button(root, text='+',padx=20,pady=20,command=clickadd)
add.grid(row=0,column=4)

zero = Button(root, text='0',padx=20,pady=20,command=clickzero)
zero.grid(row=3,column=1)

equals= Button(root, text='=',padx=20,pady=20,command=clickequals)
equals.grid(row=1,column=0)

back = Button(root,text='BACKSPACE',padx=20,pady=20,command=clickback)
back.grid(row=2,column=0)

clear = Button(root,text='CLEAR',padx=20,pady=20,command=clickclear)
clear.grid(row=3,column=0)








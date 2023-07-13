from tkinter import *
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35 , borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
i=0
def button_click(number):
    #e.delete(0,END)
    global i
    e.insert(i,number)
    i+=1
def button_clear():
    e.delete(0,END)
    i=0
def button_add():
    global l
    global math
    math = "addition"
    l= float(e.get())
    e.delete(0,END)
    i=0 
def click_back():
    global i
    e.delete(i-1)
    i-=1
    
def button_equal():
    m= float(e.get())
    e.delete(0,END)
    if math=="addition":
        k=l+m
        e.insert(0,k)

    elif math=="subtraction":
        k=l-m
        e.insert(0,k)
    elif math=="multiplication":
        k=l*m
        e.insert(0,k)
    elif math=="divide":
        k=l/m
        e.insert(0,k)
    else:
        print("ABBORT")




       
def button_subtract():
    global l
    global math
    math = "subtraction"
    l= float(e.get())
    e.delete(0,END)
    i=0 
 
    return
def button_multiply():
    global l
    global math
    math = "multiplication"
    l= float(e.get())
    e.delete(0,END)
    i=0 
 
    return
def button_divide():
    global l
    global math
    math = "divide"
    l= float(e.get())
    e.delete(0,END)
    i=0 
 
    return
    
    
button_1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
button_add = Button(root,text="+",padx=39,pady=20,fg="black",bg="blue" ,command= button_add)
button_equal = Button(root,text="=",padx=91,pady=20,fg="black",bg ="magenta",command=button_equal)
button_clear = Button(root,text="CLEAR",padx=75,pady=20,fg="black",bg="red",command=button_clear)
button_subtract = Button(root,text="-",padx=42,pady=20,fg="black",bg="yellow",command= button_subtract)
button_multiply = Button(root,text="*",padx=42,pady=20,fg="black",bg="green",command= button_multiply)
button_divide = Button(root,text="/",padx=42,pady=20,fg="black",bg="pink",command= button_divide)
button_back = Button(root,text="BACK",padx=28,pady=20,bg="black",command=click_back)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=5,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=4,column=1,columnspan=2)

button_subtract.grid(row=2,column=4)
button_multiply.grid(row=3,column=4)
button_divide.grid(row=4,column=4)
button_back.grid(row=5,column=4)

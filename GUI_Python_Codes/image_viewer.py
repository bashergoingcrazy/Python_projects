from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title(" Image Viewer ")
my_img1= ImageTk.PhotoImage(Image.open("/home/vansh/Pictures/images.jpg/one_piece.jpeg"))
my_img2= ImageTk.PhotoImage(Image.open("/home/vansh/Pictures/images.jpg/metallica.jpeg"))
my_img3= ImageTk.PhotoImage(Image.open("/home/vansh/Pictures/images.jpg/micro.jpeg"))
my_img4= ImageTk.PhotoImage(Image.open("/home/vansh/Pictures/images.jpg/index.jpeg"))


img_lst=[my_img1,my_img2,my_img3,my_img4]

status = Label(root,text="Image 1 of "+ str(len(img_lst)),bd=1,relief=SUNKEN,anchor=E)



my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)
r=len(img_lst)
i=0
def forward():
    global i
    global r
    global my_label
    i+=1
    if i == r-1:
        button_forw = Button(root,text =">>",state=DISABLED)
        button_forw.grid(row=1,column=2)
        my_label.grid_forget()
        my_label = Label(image=img_lst[i])
        my_label.grid(row=0,column=0,columnspan=3)
        status = Label(root,text="Image " +str(i+1)+" of "+ str(len(img_lst)),bd=1,relief=SUNKEN,anchor=E)
        status.grid(row=2,column=0,columnspan=3,sticky=W+E)
         
    else:
        button_back = Button(root, text = "<<",command=back)
        button_forw = Button(root,text =">>",command=forward)
        button_forw.grid(row=1,column=2)
        button_back.grid(row=1,column=0)
        status = Label(root,text="Image " +str(i+1)+" of "+ str(len(img_lst)),bd=1,relief=SUNKEN,anchor=E)
        my_label.grid_forget()
        my_label = Label(image=img_lst[i])
        my_label.grid(row=0,column=0,columnspan=3)
        status.grid(row=2,column=0,columnspan=3,sticky=W+E)  
    
        
def back():
    global i
    global r
    global my_label
    
    i-=1
    if i == 0:
        my_label.grid_forget()
        my_label = Label(image=img_lst[i])
        my_label.grid(row=0,column=0,columnspan=3)
        status = Label(root,text="Image " +str(i+1)+" of "+ str(len(img_lst)),bd=1,relief=SUNKEN,anchor=E)
         
        button_back = Button(root,text ="<<",state=DISABLED)
        button_back.grid(row=1,column=0)
        status.grid(row=2,column=0,columnspan=3,sticky=W+E)   
        
    else:
        button_back = Button(root, text = "<<",command=back)
        button_back.grid(row=1,column=0)
        button_forw = Button(root,text =">>",command=forward)
        button_forw.grid(row=1,column=2)
        status = Label(root,text="Image " +str(i+1)+" of "+ str(len(img_lst)),bd=1,relief=SUNKEN,anchor=E)
        my_label.grid_forget()
        my_label = Label(image=img_lst[i])
        my_label.grid(row=0,column=0,columnspan=3)
        status.grid(row=2,column=0,columnspan=3,sticky=W+E)   
           



button_back = Button(root, text = "<<",command=back,state=DISABLED)
button_forw = Button(root,text =">>",command=forward)


button_quit= Button(root,text='EXIT ',command=root.quit)
button_quit.grid(row=1,column=1)
button_forw.grid(row=1,column=2,pady=10)
button_back.grid(row=1,column=0)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)                 


root.mainloop()








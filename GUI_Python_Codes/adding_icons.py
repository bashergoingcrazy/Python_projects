from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title(" Adding Images ")
#root.iconbitmap("/home/vansh/Pictures/cute-skull.png")

my_img= ImageTk.PhotoImage(Image.open("/home/vansh/Pictures/images.jpg/one_piece.jpeg"))
my_label = Label(image=my_img)
my_label.pack()













button_quit= Button(root,text='Exit Programe',command=root.quit)
button_quit.pack()



root.mainloop()













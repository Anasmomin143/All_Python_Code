# Q38. Write a python program for following gui radio button:

from tkinter import*
def fn():
    x=var.get()
    if(x==1):
        lb1.config(fg="red")
    elif(x==2):
        lb1.config(fg="green")
    elif(x==3):
        lb1.config(fg="blue")
gui=Tk()
gui.title("radio Button")
gui.geometry("300x300")
var = IntVar()
lb1=Label(gui,text="Choose color from")
lb1.pack()
rb1=Radiobutton(gui,text="red",variable=var,value=1 ,command=fn)
rb1.pack()
rb2=Radiobutton(gui,text="green",variable=var,value=2,command=fn)
rb2.pack()
rb3=Radiobutton(gui,text="blue",variable=var,value=3,command=fn)
rb3.pack()
gui.mainloop()

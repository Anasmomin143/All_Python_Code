from tkinter import*
a=0
b=0
add=0
sub=0
div=0
mul=0
def action():
    global a
    global b
    a=int(input("Enter I no.="))
    b=int(input("Enter II no.="))
    global add
    global sub
    global div
    global mul
    add=a+b
    sub=a-b
    div=a/b
    mul=a*b
    lb1.config(text="Value 1 = "+str(a))
    lb2.config(text="Value 2 = "+str(b))
    lb3.config(text="Add = "+str(add))
    lb4.config(text="Sub = "+str(sub))
    lb5.config(text="Div = "+str(div))
    lb6.config(text="Multi = "+str(mul))
gui=Tk()
gui.title("math operation")
gui.geometry("300x400")
lb1=Label(gui,text="Value 1 = 0")
lb2=Label(gui,text="Value 2 = 0")
lb3=Label(gui,text="Add = 0")
lb4=Label(gui,text="Sub = 0")
lb5=Label(gui,text="Div = 0")
lb6=Label(gui,text="Multi = 0")
b1=Button(gui,text="evaluate",command=action)
lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack()
lb5.pack()
lb6.pack()
b1.pack()

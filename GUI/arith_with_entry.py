from tkinter import*
def fn():
    x=int(entry1obj.get())
    y=int(entry2obj.get())
    entry3obj.insert(0,str(x+y))
    entry4obj.insert(0,str(x-y))
    entry5obj.insert(0,str(x/y))
    entry6obj.insert(0,str(x*y))

def reset():
    entry1obj.delete(0,END)
    entry2obj.delete(0,END)
    entry3obj.delete(0,END)
    entry4obj.delete(0,END)
    entry5obj.delete(0,END)
    entry6obj.delete(0,END)
gui=Tk()
gui.title("Entry control name")
gui.geometry("800x800")
canobj=Canvas(gui)
canobj.pack()

lb1=Label(gui,text="Enter Value 1:- ")
canobj.create_window(100,50,window=lb1)
entry1obj=Entry(gui)
canobj.create_window(200,50,window=entry1obj)

lb2=Label(gui,text="Enter Value 2:- ")
canobj.create_window(100,100,window=lb2)
entry2obj=Entry(gui)
canobj.create_window(200,100,window=entry2obj)

bt1=Button(gui,text="Submit",bg="#90ee90",fg="black",command=fn)
canobj.create_window(100,150,window=bt1)

bt2=Button(gui,text="Reset",bg="#90ee90",fg="black",command=reset)
canobj.create_window(200,150,window=bt2)

lb3=Label(gui,text="Addition :- ")
canobj.create_window(100,200,window=lb3)
entry3obj=Entry(gui)
canobj.create_window(200,200,window=entry3obj)

lb4=Label(gui,text="Substraction:- ")
canobj.create_window(100,250,window=lb4)
entry4obj=Entry(gui)
canobj.create_window(200,250,window=entry4obj)

can1obj=Canvas(gui)
can1obj.pack()
lb5=Label(gui,text="Division:- ")
can1obj.create_window(100,50,window=lb5)
entry5obj=Entry(gui)
can1obj.create_window(200,50,window=entry5obj)

lb6=Label(gui,text="multiplication:- ")
can1obj.create_window(100,100,window=lb6)
entry6obj=Entry(gui)
can1obj.create_window(200,100,window=entry6obj)

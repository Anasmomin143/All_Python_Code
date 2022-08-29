# from tkinter import *
# def fn():
#     x=t1.get(1.0,"end")
#     t2.delete(1.0,"end")
#     t2.insert(INSERT,x)
# gui=Tk()
# gui.geometry("300x300")
# t1=Text(gui,height=1)
# t2=Text(gui,height=1)
# btn=Button(gui,text="Copy Text",command=fn)
# t1.pack()
# btn.pack()
# t2.pack()

#messagebox.showinfo

# from tkinter import *
# from tkinter import messagebox
# def fn():
#     x=messagebox.showinfo("Demo","This is Info Dialog Box")
#     print(x)
# gui=Tk()
# gui.geometry("300x300")
# btn=Button(gui,text="Click Here",command=fn)

# btn.pack()

#warnning

# from tkinter import*
# from tkinter import messagebox
# def fn1():
#     x=messagebox.showwarning("warning","this is warning")
#     print(x)
# gui=Tk();
# gui.title("demo")
# gui.geometry("200x200")
# btn=Button(gui,text="hello",command=fn1)
# btn.pack

#showerror
#from tkinter import*
# from tkinter import messagebox
# def fn1():
#     x=messagebox.showerror("error","this is error")
#     print(x)
# gui=Tk();
# gui.title("demo")
# gui.geometry("200x200")
# btn=Button(gui,text="hello",command=fn1)
# btn.pack()


from tkinter import*
from tkinter import messagebox
def fn1():
    x=messagebox.askquestion("error","this is error")
    print(x)
    if(x=="yes"):
        lb1.config(str("hello"))
gui=Tk();
gui.title("demo")
gui.geometry("200x200")
btn=Button(gui,text="hello",command=fn1)
btn.pack()
lb1=Label(gui,text="something")
lb1.pack()

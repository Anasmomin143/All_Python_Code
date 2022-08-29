from tkinter import*

def fn():
   s=int(entry.get())
   entry1.insert(0,str(s*s))
gui=Tk()
gui.title("Square")
gui.geometry("400x300")
lb1=Label(gui,text="Enter A number ")
lb1.grid(row=0,column=0)
entry=Entry(gui)
entry.grid(row=0,column=1)
btn=Button(gui,text="ok" ,command=fn)
btn.grid(row=1,column=1)
lb2=Label(gui,text="Square ")
lb2.grid(row=2,column=0)
entry1=Entry(gui)
entry1.grid(row=2,column=1)

from tkinter import*
def fn():
    x=int(entryobj.get())
    lb2.config(text="Square : "+str(x*x))

gui=Tk()
gui.title("Square with Entry Control")
gui.geometry("300x300")
canobj=Canvas(gui)
canobj.pack()
lb1=Label(gui,text="Enter one no :")
canobj.create_window(150,50,window=lb1)
entryobj=Entry(gui)
canobj.create_window(150,100,window=entryobj)
btn=Button(gui,text="Submit",command=fn)
canobj.create_window(150,150,window=btn)
lb2=Label(gui,text="Square :")
canobj.create_window(150,200,window=lb2)

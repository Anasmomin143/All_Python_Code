from tkinter import*
def fn():
    x=entryobj.get()
    lb2.config(text="Welcome "+x)

gui=Tk()
gui.title("Entry control name")
gui.geometry("400x300")
canobj=Canvas(gui)
canobj.pack()
lb1=Label(gui,text="Enter Your Name")
canobj.create_window(180,50,window=lb1)
entryobj=Entry(gui)
canobj.create_window(180,100,window=entryobj)
btn=Button(gui,text="Submit",command=fn)
canobj.create_window(180,150,window=btn)
lb2=Label(gui,text="")
canobj.create_window(180,200,window=lb2)

from tkinter import*
def fn():
    print("hello")
gui=Tk()
gui.title("Using Button Widgt")
gui.geometry("300x300")
b1=Button(gui,text="check here",bg="red",fg="yellow",font="Bold",command=fn)
#b1.pack()
b1.place(x=30,y=60)

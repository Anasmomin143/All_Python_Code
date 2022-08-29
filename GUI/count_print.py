from tkinter import*
i=0
a="Counter="
def count():
    global i
    i=i+1
    global a
    lb1.config(text=a+str(i))

gui=Tk()
gui.title("Click Counter")
gui.geometry("300x300")
lb1=Label(gui,text="Counter=0")
b1=Button(gui,text="Show Counter",command=count)
lb1.pack()
b1.pack()

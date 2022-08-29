from tkinter import*
def Lb1Event(a):
    print("label is clicked")
gui=Tk()
gui.title("Label Event Demo")
gui.geometry("300x300")
lb1=Label(gui,text="Click Here")
lb1.pack()
lb1.bind("<Button>",Lb1Event)

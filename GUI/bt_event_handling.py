# Button Event handling
from tkinter import*
def b1():
    print("Button is Clicked")
gui=Tk()
gui.title("Button Event Handling")
gui.geometry("400x400")
b1=Button(gui,text="Click here", command=b1)
b1.pack()

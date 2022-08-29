# WAP to create Following interface with three Label on button Click Event show
# show the curesponding operation using a value

import math
from tkinter import*
x =5
def square(a):
    global x
    print("square",x*x)
def cube(b):
    global x
    print("square",x*x*x)
def sq_root(c):
    global x
    print("square",math.sqrt(x))
gui=Tk()
gui.title("Arithmatic operation")
gui.geometry("400x400")
lb1=Label(gui,text="Square")
lb1.bind("<Button>",square)
lb2=Label(gui,text="Cube")
lb2.bind("<Button>",cube)
lb3=Label(gui,text="Sq root")
lb3.bind("<Button>",sq_root)
lb1.pack()
lb2.pack()
lb3.pack()


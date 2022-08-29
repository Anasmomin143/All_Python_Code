from tkinter import*
gui=Tk()
gui.title("Label 1 image demo")
gui.geometry("300x300")
label=Label(gui,text="")
canobj=Canvas(gui)
canobj.pack()
imgobj=PhotoImage(file="p1.png",)
canobj.create_image(20,20,image=imgobj)

from tkinter import*
def fn():
    a=int(t1.get(1.0,"end"))
    b=int(t2.get(1.0,"end"))
    c=int(t3.get(1.0,"end"))
    d=int(t4.get(1.0,"end"))
    total=(b+c+d)
    avg=total/3
    t5.insert(INSERT,str(total))
    t6.insert(INSERT,str(avg))
gui=Tk()
gui.title("Student Result")
gui.geometry("500x600")
lb1=Label(gui,text="Stud Name")
lb1.pack()
t1=Text(gui,height=1,width=20)
t1.pack()

lb2=Label(gui,text="Test Marks 1:- ")
lb2.pack()
t2=Text(gui,height=1,width=20)
t2.pack()

lb3=Label(gui,text="Test Marks 2:- ")
lb3.pack()
t3=Text(gui,height=1,width=20)
t3.pack()

lb4=Label(gui,text="Test Marks 3:- ")
lb4.pack()
t4=Text(gui,height=1,width=20)
t4.pack()

bt1=Button(gui,text="Submit",command=fn)
bt1.pack()

lb5=Label(gui,text="Total Marks :- ")
lb5.pack()
t5=Text(gui,height=1,width=20)
t5.pack()

lb6=Label(gui,text="Avg Marks :- ")
lb6.pack()
t6=Text(gui,height=1,width=20)
t6.pack()

lb7=Label(gui,text="Grade :- ")
lb7.pack()
t7=Text(gui,height=1,width=20)
t7.pack()

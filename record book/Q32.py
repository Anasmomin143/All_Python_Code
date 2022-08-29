# Q32.Write a program use of Destructor
class B:
    n=0
    def __init__(self):
        self.n="Anas"
    def display(self):
        print("hello And welcome ",self.n)
    def __del__(self):
        print("destructor executed")
    def display2(self):
        print(self.n)
        
        

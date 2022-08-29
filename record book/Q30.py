#Q30.Write a program to create following class “Number”
 #        Data member n ,m 
 #      Function member 
# i.  getInput()
# ii.Showminshow smallest of n& m
# iii.showmaxshow highest of n & m

class number:
    n=0
    m=0
    def getInput(self):
        self.n=int(input("Enter 1st Number ="))
        self.m=int(input("Enter 2nd Number ="))
    def Showmin(self):
        if(self.n<self.m):
            print(self.n,"is smallest")
        elif(self.n>self.m):
            print(self.m,"is smallest")
    def Showmax(self):
        if(self.n<self.m):
            print(self.m,"is grater")
        elif(self.m<self.n):
            print(self.n,"is grater")

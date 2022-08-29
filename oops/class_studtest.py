class studtest:
    t1=0;t2=0;t3=0
    def getInput(self):
        self.t1=int(input("test 1:"))
        self.t2=int(input("test 2:"))
        self.t3=int(input("test 3:"))
    def showdata(self):
        tot=self.t1+self.t2+self.t3
        avg=tot/3
        print("Total Marks=",tot)
        print("Avrg marks",avg)

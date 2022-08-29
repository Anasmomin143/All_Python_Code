class A:
   n=10 #data member
   def display(self):
       self.n=self.n+5
       print("value of n",self.n)
       #without self
       #n=n+5
       #print("value of n",n)

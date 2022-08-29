# Q34.Write a program of use of Multi-level Inheritance
fathername=0
mothername=0
class father:
    def father(self):
        self.fathername="Abdul Naim"
class mother:
    def mother(self):
        self.mother="Arefa Fatema"
class son(father,mother):
    def son(self):
        print("father :",self.father)
        print("mother :",self.mother)
                

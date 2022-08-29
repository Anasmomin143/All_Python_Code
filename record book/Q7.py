#Q7.Write a program to get input of 3 elements & 3 values display one key only values and also show all elements .
a=input("key 1 =")
b=input("key 2 =")
c=input("key 3 =")
x=input("value 1 =")
y=input("value 2 =")
z=input("value 3 =")
data={a:x,b:y,c:z}
print("To show all Element =",data)
print("all keys =",(data.keys()))
print("all values =",(data.values()))
print("Total no of element =",len(data))

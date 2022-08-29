# Q22.Write a program to display execute a loop between 1-10 but when the loop counter 5 exit the loop
list=[]
while True:
    n=int(input("Enter one int Value ="))
    if(n>=100):
        break
    else:
        list.append(n)
print(list)

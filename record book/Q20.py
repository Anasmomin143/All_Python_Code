# Q20.Write a program to show 1-100 series but skip even number between 50-60
for i in range(1,101,1):
    if(i>=50 or i<=60): 
        if(i%2==0):
            continue
        else:
            print(i)


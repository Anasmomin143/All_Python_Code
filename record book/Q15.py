t1=int(input("Test Mark 1="))
t2=int(input("Test Mark 2="))
t3=int(input("Test Mark 3="))
tot=t1+t2+t3
avg=tot/3
if(avg<10):
    print("Grade C")
elif(avg >=10 and avg<14):
    print("Grade B")
elif(avg>=14 and avg<18):
    print("Grade A")
elif(avg>=18 and avg<=20):
    print("Grade A+")
else:
    print("Fail")

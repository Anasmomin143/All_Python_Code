# Q14.Write a program to get input of maxmarks , obtmarks  calculate average marks show result “PASS ” when avrg marks>=40  else “FAIL”.
tot=int(input("Enter total Marks ="))
obt=int(input("Enter Obt Marks ="))
avg=(obt/tot)*100
if(avg>=40):
    print("pass")
else:
    print("Fail")
        

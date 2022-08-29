# Q19.Write a program to get input of string  & char find & show the frequency of character in string.
freq=0
s=input("Enter one string Value =")
ch=input("Enter one char Value =")
for i in range(len(s)):
    if(ch==s[i]):
        freq+=1
    else:
        print("char is not found in of string")
print(freq ,"no of char found")
        

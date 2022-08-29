# Q18Write a program to get input of string count number vowels in it
count=0
s=input("Enter one String =")
for i in range(len(s)):
    if s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or s[i]=='O' or s[i]=='u' or s[i]=='U':
        count+=1
        print(s[i],"is a vowel")
    else:
        print(s[i],"is not a vowel")

print("No of vowel in given string =",count)
        

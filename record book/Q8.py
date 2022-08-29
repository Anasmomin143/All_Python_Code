#Q8.Write a program to get input of a string of at least 8 chars & show the result of following operation
# i.	Display whole the string 
# ii.	Display only 2nd,3rd,5th,7thchar(not index)
# iii.	Display only 1st,3rd,5th& 8th char (not index)
# iv.	Display a substring from 3rd to 6th char

s=input("Enter str at least 8 chars =")
print(s)
print("2nd=",s[1],"3rd=",s[2],"5th=",s[4],"7th",s[6])
print("1st=",s[0],"3rd=",s[2],"5th=",s[4],"8th=",s[7])
print("from 3rd to 6th char = ",s[2:6])



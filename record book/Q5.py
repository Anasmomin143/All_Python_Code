#Q5.Write a program to get input of one integer & one float value and display all 6 arithmetic operation.
x=int(input("Enter one Int NO. ="))
y=float(input("Enter one float NO. ="))
add=x+y
sub=x-y
mul=x*y
div=x/y
mod=x%y                 #   Modulus  operator
exp=x**y                #   Exponentiation  operator
floordiv=x//y           #   floor division  operator
print("Addition = ",add)
print("Substraction = ",sub)
print("Multiplication = ",mul)
print("Division = ",div)
print("modulus = ",mod)
print("Exponentiation = ",exp)
print("floor Division = ",floordiv)

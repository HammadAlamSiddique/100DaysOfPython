# Let's create a calculator using python 
a = 50
b = 3

print("The value of",a,"+",b,"is",a+b)
print("The value of",a,"-",b,"is",a-b)
print("The value of",a,"*",b,"is",a*b)
print("The value of",a,"/",b,"is",a/b)



# by using input function, arithmetic operators and if-else statements
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
oper = input("Chose any one Operator: +,-,*,/: ")

if oper == '+':
    print("The addition of two numbers is", num1+num2)
elif oper == '-':
    print("The subtraction of two numbers is", num1-num2)
elif oper == '*':
    print("The multiplication of two numbers is", num1*num2)
else:
    print("The division of two numbers is", num1/num2)
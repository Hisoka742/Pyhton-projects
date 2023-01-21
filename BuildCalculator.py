from ast import operator


num1 = float(input("enter the first num :"))
operator = input("please enter the operator :")
num2 = float(input("enter the second num :"))

if operator == "+":
   print(num1 + num2)
elif operator == "-":
    print(num1 - num2 )
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Try again wrong operator")
    


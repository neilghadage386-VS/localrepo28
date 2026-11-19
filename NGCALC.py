print("====NGCALCULATOR====")

num1 = int(input("enter the first no:"))
num2 = int(input("enter second no:"))
opera = input("enter the op(+, -, *, /):")

if opera == "+":
    print(num1+num2)
elif opera == "-":
    print(num1-num2)
elif opera == "*":
    print(num1*num2)
elif opera == "/":
    if num2 == 0:
        print("error")
    else:
        print(num1/num2)
else:
    print("invalid input")

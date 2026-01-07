def calc():
    num1 = int(input("Enter first number \n"))
    num2 = int(input("Enter second number \n"))
    
    act = input("choose the option: *, +, -, /, ^, √ \n")

    if act == "*":
        print(num1*num2)
    elif act == "+":
        print(num1+num2)
    elif act == "-":
        print(num1-num2)
    elif act == "/":
        print(num1/num2)
    elif act == "^":
        print(num1**num2)
    elif act == "√" or act == "korin":
        print(num1**(1/num2))
    else:
        print("invalid action")
        calc()
    
    
calc()

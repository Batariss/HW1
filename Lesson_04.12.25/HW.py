def ex1():
    num = int(input("enter the number: \n"))

    if num > 0 :
        print("Додатнє\n")
        choose()
    elif num < 0 :
        print("Від'ємне\n")
        choose()
    elif num == 0 :
        print("Нуль\n")
        choose()
    else:
        print("Invalid command\n")
        choose()


def ex2():
    num = int(input("enter your age: \n"))

    if 5 <= num <= 0:
        print("Малюк\n")
        choose()
    elif 6 <= num <= 17:
        print("Школяр\n")
        choose()
    elif 18 <= num <= 23:
        print("Студент\n")
        choose()
    elif 24 <= num <= 60:
        print("Дорослий\n")
        choose()
    elif 24 <= 61:
        print("Дорослий\n")
        choose()
    else:
        print("Invalid command \n")
        choose()
        
def ex3():
    password = input("enter the password: \n")

    if password == "admin123":
        print("Correct password \n")
        choose()
    else:
        print("Incorrect password \n")
        choose()     
        
def ex4():
    temp = int(input("enter the temperature: \n"))

    if temp < 0:
        print("Мороз \n")
        choose()
    elif 0 <= temp <= 20:
        print("Прохолодно \n")
        choose()
    elif 21 <= temp < 30:
        print("Тепло \n")
        choose()
    elif temp > 30:
        print("Спека \n")
        choose()
    else:
        print("Invalid command \n")
        choose()
        
        
def ex5():
    money = int(input("enter your cash balans: \n"))
    card = input("do you have our loyal card? \n")


    if money > 5000:
        money = True
    else:
        money = False
    
    if card == "yes" or "Yes":
        card = True
    else:
        card = False
        
    if card == True and money == True:
        print("You`re s VIP client \n")
        choose()
    else:
        print("You`re a normal client \n")
        choose()
        
def ex6():
    
    num = int(input("enter the number: \n"))
    
    if num % 10 == 0:
        print("Особливе число \n")
        choose()
    elif num % 2 == 0:
        print("Парне \n")
        choose()
    else:
        print("Непарне \n")
        choose()

        
def choose():       
    quest = input("choose the exercise: \n1.ex1 \n2.ex2 \n3.ex3 \n4.ex4 \n5.ex5 \n6.ex6 \n")

    if quest == "ex1" or quest == "1":
        ex1()
    elif quest == "ex2"or quest == "2":
        ex2()
    elif quest == "ex3" or quest == "3":
        ex3()
    elif quest == "ex4" or quest == "4":
        ex4()
    elif quest == "ex5" or quest == "5":
        ex5()
    elif quest == "ex6" or quest == "6":
        ex6()
        
choose()
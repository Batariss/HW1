
def ex1():
    allsteps = 0
    days = 0
    steps = int(input("Введи кількість кроків за день: \n"))


    while allsteps < 100000:
        allsteps += steps
        days += 1

    print(f"Щоб набрати 100 000 кроків, треба {days} д.")
    
def ex2():
    num1 = int(input("Введіть число: \n"))
    num2 = 0
    for i in range (11):
        print(f'{num1}*{num2}={num1*num2}')
        num2 +=1
        
        
def ex3():
    user = True
    while True:
        password = input("Введи пароль: ")
        if password == "dragon":
            user = False
            if user == False:
                print("Вітаю в грі!")
            
def ex4():
    word = input("Enter the word: \n")
    gol = "aeiuoyAEIUOY"
    a = 0
    
    for i in word:
        if i in gol:
            a += 1
        
    
    print(f"Голосних: {a}")
    
def ex5():
    hp = 30
    
    while hp > 0:
        damage  = int(input("Введи урон: \n"))
        hp -= damage
    print("Ворог поконаний")
    
def choose():       
    quest = input("choose the exercise: \n1.ex1 \n2.ex2 \n3.ex3 \n4.ex4 \n5.ex5 \n")

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
        
choose()
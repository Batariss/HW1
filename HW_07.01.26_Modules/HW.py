# #EX1
# import random
# rightnum = random.randint(0, 10)
# ch = 3
# def ex():
#     global rightnum, ch, num
#     num = int(input(f"Enter the number from 0 to 10, you have {ch} chances: "))
#     if num == rightnum:
#         print("you Win")
#     elif ch <= 1:
#         print(f"loose, the right number is {rightnum}")
#         exit()
#     else:
#         ch -= 1
#         ex()
    
# #print(rightnum)

# ex()


# #EX2
# import time

# minutes = int(input("Enter minutes: "))
# seconds = minutes * 60

# while seconds > 0:
#     mins = seconds // 60
#     secs = seconds % 60
#     print(f"{mins:02}:{secs:02}", end = "\r")
#     time.sleep(1)
#     seconds -= 1

# print("\nTime is up!")


# #EX3
# import time

# input("Натисни Enter для початку")

# start = time.time()

# input("Enter для Lap 1")
# lap1 = time.time() - start
# print(f"Lap 1: {lap1:.2f} секунд")

# input("Enter для Lap 2")
# lap2 = time.time() - start
# print(f"Lap 2: {lap2:.2f} секунд")

# input("Enter для Lap 3")
# lap3 = time.time() - start
# print(f"Lap 3: {lap3:.2f} секунд")

# alltime = time.time() - start
# print(f"\nЗагальний час: {alltime:.2f} секунд")

# EX4
# import random


# passdict = [1,2,3,4,5,6,7,8,9,".","!","@","#","$","%","&","_","*"
#             "q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","k","l","z","x","c","v","b","n","m",
#             "Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]

# random.shuffle(passdict)

# passbarier = passdict[0:7:]

# password = "".join(map(str,passbarier))

# #print(password)

# userpassword = input("Enter the password: ")

# if userpassword == password:
#     print("Correct password")
# else:
#     print("incorrect password")


#Ex5
# import random
# value ="Orel","Reshka"
# choise = random.choice(value)

# # print(choise)

# monetka = input("Enter Orel or Reshka: ")

# if monetka == choise:
#     print("Win")
# else:
#     print("Lose")
    
    
#EX6
# import time
# import random


# globaltime = time.time()

# for i in range(random.randint(1,10)):
#     time.sleep(1)
#     fortime = time.time() - globaltime
# print(f"Цикл длився {fortime} секунд")

#спочатку я не правильно зрозумів завдання, але ось привильний варіант:

# import time
# globaltime = time.time()

# for i in range(1):
#     fortime = time.time() - globaltime
    
# print(f"Цикл длився {round(fortime, 7)} секунд")

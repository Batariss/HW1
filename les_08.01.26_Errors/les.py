# try:
#     x = int(input("Enter the number: ")) 
# except ValueError:
#     print("Incorrect value")

 
# def nums(): 
#     try:
#         x = int(input("Enter first number: ")) 
#         y = int(input("Enter second number: "))
#         print(x/y)
#     except ValueError:
#         print("Incorrect value")
#         nums()
#         exit()
#     except ZeroDivisionError:
#         print("b value mustn't be 0")
#         nums()
#         exit()
#     finally:
#         print("Execution complete")
#         exit()
# nums()

# try:
#     age = int(input("enter your age: "))
#     if age < 0:
#         age/0
# except ValueError:
#     print("Incorrect value")
# except ZeroDivisionError:
#     print("Incorrect age")  

# while True:
#     try:
#         num = int(input("Enter the number: "))
#         if num == 777:
#             break
#         else:
#             print(100/num)
#     except ValueError:
#         print("Incorrect value")
#     except ZeroDivisionError:
#         print("Value mustn't be 0")
#     finally:
#         print("Program finished")
    

# sproby = 0
# maxsprob = 3

# while sproby < maxsprob:
#     try:
#         usernum = int(input("Введіть число: "))
#         print(f"Ви ввели число: {usernum}")
#         break
#     except ValueError:
#         print("Це не число.")
#         sproby += 1

# if sproby == maxsprob:
#     print("Більше нема спроб")





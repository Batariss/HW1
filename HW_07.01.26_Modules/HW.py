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


#EX3
import time 




#Ex1
# def calc(a, b, operation):
#     if operation == "+":
#         return a + b
#    if operation == "-":
#         return a - b
#     if operation == "*":
#         return a * b
#     if operation == "/":
#         return a / b
    
# result = calc(3, 4, "-")
    
# print(f"result is:{result}")

#Ex2
# number = lambda x: x % 10
# print(number(298415))

#Ex3
# numbers = [1, 4, 59, 9, 5, 7]
# squares = list(map(lambda x: x**2, numbers))
# print(squares)

#Ex4
# words = {"Hello","apple","apologize","forgiving","hi","Oleksii"}
# result = list(filter(lambda x: len(x) > 5 , words))
# print(result)

#Ex5 від молодшого до старшого
# students = [
#     {"name": "Ivan", "age": 18},
#     {"name": "Olya", "age": 20},
#     {"name": "Max", "age": 17}
# ]

# result = sorted(students, key=lambda x: x["age"])
# print(result)

# #Ex5 від старшого до молодшого
# students = [
#     {"name": "Ivan", "age": 18},
#     {"name": "Olya", "age": 20},
#     {"name": "Max", "age": 17}
# ]

# result = sorted(students, key=lambda x: x["age"] * -1)
# print(result)

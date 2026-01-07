#EX1
# a = [1,3,5]
# b = [2,4,6]

# res = a+b

# res.sort()

# print(res)



#EX2
# sentence = input("Введіть речення: ")

# words = sentence.lower().split()

# for word in set(words):
#     print(word, "—", words.count(word))

#EX3
# words = ["Hi", "WORLD", "hello", "MyList", "It'sMyHomwork"]

# result = []

# for word in words:
#     if len(word) > 4:
#         result.append(word)

# print(result)


#EX4
# a = [(1, 2), (3, 4), (1, 2), (5, 6)]

# b = []

# for i in a:
#     if i not in b:
#         b.append(i)

# print(b)


#EX5
# pokupki = []

# while True:
#     tovar = input("Введіть товар (назва:ціна): ")
#     if tovar == "":
#         break

#     name, price = tovar.split(":")
#     price = float(price)

#     pokupki.append((name, price))

# total = 0
# for item in pokupki:
#     total += item[1]

# average = total / len(pokupki)

# cheapest = pokupki[0]
# for item in pokupki:
#     if item[1] < cheapest[1]:
#         cheapest = item

# print("Список товарів:", pokupki)
# print("Загальна сума:", total)
# print("Середня ціна:", average)
# print("Найдешевший товар:", cheapest)





# film = {
#         "title": "Spider-Man",
#         "year": "2012",
#         "rezyser": "NULL",
# }

# film["type"]="Super-Hero"
# del film["year"]
# print(film.keys())
# print(film.values())

# print("\n\n\n--------------------\n\n\n")

# student =  {
#     "name":"Alex",
#     "age":"19"
# }

# for key, values in student.items():
#     print(f"{key}:{values}")
    
    
    
# student =  {
#     "name":["Alex", "Omar", "Sten"],
#     "age":[12,14,15]
    
#             }
# student2 = {"Alina","Steve","Omar"}


fruit1 = {"apple", "banana", "pear"}
fruit2 = {"banana", "kiwi"}

fruits = fruit1 & fruit2
print(fruits)

word1 = {"apple","banana","kiwi","pear"}
word2 = {"pear","cucumber","arbuz","kiwi"}
rizhytsia = (word1^word2)
print(rizhytsia)
    

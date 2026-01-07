name = 'Alex Yanets'

print(len(name))#виводить кількість символів в стрінгу
print(name[0:6])#виводить від 0 знаку до 6
print(name[0:7:1])#виводить від 0 знаку до 7 з кроком 1
print(name[0:6:2])#виводить від 0 знаку до 7 з кроком 2
print(name[::2])#виводить всі знаки з кроком 2
print(name[::-1])#виводить всі знаки в зворотньому напрямку

print(name.upper())
print(name.lower())

print(name.replace('A','O').replace('x','k'))
print(name.capitalize())
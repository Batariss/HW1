#Ex 1
val1 = int(input("Enter the value in UAH: \n"))

usd = round(val1/42.35, 2)
eur = round(val1/49.26, 2)
pln = round(val1/11.62, 2) 

print(f"{val1} is {usd}$, {eur}€, {pln}zł")

#Ex2

num1 = int(input("Enter first number \n"))
num2 = int(input("Enter second number \n"))

act = input("choose the option: *, +, -, / \n")

if act == "*":
    print(num1*num2)
elif act == "+":
    print(num1+num2)
elif act == "-":
    print(num1-num2)
elif act == "/":
    print(num1/num2)
    
#Ex3

sent = input("Enter your sentence: \n")

words = len(sent.split())

letters = len(sent)

upper_sentence = sent.upper()

print(words)
print(letters)
print(upper_sentence)

#Ex4

year = int(input("Enter the Year: \n"))

if (year % 4 == 0 and year % 100 != 0):
    print("Interacalary")
else:
    print("Not intercalary")
    
    
#Ex5

numm = input("Enter the number: \n")

print(sum(map(int,numm)))



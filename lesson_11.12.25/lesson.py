mark = []
for i in range(5):
    m = int(input("Enter your mark: \n"))
    mark.append(m)
    
    
maxx = max(mark)
mark.sort()

print(maxx)
print(mark)
print(mark.count(12))

list = [1, 2, 2, 5, 8, 4, 4, 8]
Count=5 
i=0
b=[]
while i<len(list):
    if list[i] not in b:
        b.append (list[i])
    i=i+1
print(b)


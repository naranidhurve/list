
list=[6,1,3,5,6,3,1]
a=int(input("enter the number total number"))
l=[]
for i in range(a):
    ele=input("enter the number")
    l.append(ele)
    print("my list",ele)

list=[6,1,3,5,6,3,1]
i=1
mul=1
while i <len(list):
    mul=mul*list[i]
    i=i+1
print(mul)

list=[6,1,3,5,6,3,1]
i=0
a=[]
mul=1
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
        mul=mul*a[i]
    i+=1
print(mul)


list=[6,1,3,5,6,3,1]
i=0
b=[]
while i<len(list):
    if list[i] not in b:
        b.append (list[i])
    i=i+1
print(b)



list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
i=0
a=[]
while i<len(list1):
    if list1[i]>3 and list1[i]<6:
        a.append(list1[i])
    i=i+1
print(a)



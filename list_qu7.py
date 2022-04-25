list1=[1,4,9,[2,6],3]
i=0
b=[]
while i<len(list1):
    if type(list1[i])==type([]):
        j=0
        while j<len(list1[i]):
              b.append(list1[i][j])
              j=j+1
    else:
         b.append(list1[i])
    i=i+1
print(b)










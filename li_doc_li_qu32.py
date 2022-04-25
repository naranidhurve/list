
a=[1,2,3]
b=[5,6,7]
i=0
while i<len(a):
    i=i+1
print(a+b)


a=[9.0, "soso","narani",16,9,6.7]
i=0
a1=[]
b=[]
c=[]
while i<len(a):
    if (type(a[i])==int):
       a1.append(a[i])
    elif (type(a[i])==str):
        b.append(a[i])
    elif (type(a[i])==float):
        c.append(a[i])
    i=i+1
print(a1,"\n",b,"\n",c)

a=[[1,2],[5,8],[4,8],[4,7],[3,9],[12,81]]    
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        e=(a[i][j])
        if i%2==0:
         b.append(e)
        j=j+1
    i=i+1
print(b)

a=[[1,2],[5,8],[4,8],[4,7],[3,9],[12,81]]    
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        e=0
        e=(a[i][j])
        b.append(e)
        j=j+1
    i=i+1
print(b)


a=[1,2,5,8,4,8,4,7,3,9,12,81]    
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a):
        e=0
        e=(a)
        b.append(a)
        j=j+1
    i=i+1
print(a)



    

list1=[2,5,1,8,3,6]

num=int(input("enter the bainary number"))
sum=0
i=0
while num!=0:
    rem=num%10
    sum=sum+rem*pow(2,i)
    num=int(num/10)
    i=i+1
print("decimal num:",sum)



list=[1,2,3,4,5,6,7,8,9,10]
a=[]
i=0
while i<len(list):
    a.append(list)
    print(list[i])
    i=i+1
    


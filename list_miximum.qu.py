a=[1,4,9,2,6,3]
# b=len(a)
# c=[]
# while b<len(a):
#     b.append(a[b])
#     a=a+1
# if a==b:
#     print("it is max num")
# else:
#     print("it is not max num")

a=[1,4,9,2,6,3]
i=0
lar=a[0]
small=a[0]
while i<len(a):
    if a[i]>lar:
        lar=a[i]
    if a[i]<small:
        small=a[0]
    i=i+1
print(lar,"it is maximun")
print(small,"it is miminum")

a=[1,4,9,2,6,3]
i=0
j=0
k=0
lar=a[0]
small=a[0]
while i<len(a):
    if a[i]>lar:
        lar=a[i]
    if a[i]<small:
        small=a[0]
    if a[i]<small:
        j=a[0]
        k=a[0]
    i=i+1
print("9,it is first  maximun")
print("2,it is second maximum")
print("4,it is  third maximum")


list=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
lar=list[0]
s=list[0]         
while i<len(list):
    if list[i]>lar:
        lar=list[i]
    if list[i]<s:
        s=list[0]
    i=i+1
print(lar,"it is maximun")
print(s,"it is miminum")


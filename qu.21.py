name=('Narani','dhurve')
i=0
a=0
string=" "
while i<len(name):
    j=0
    while i<len(name):
        if j==0:
            a=name[i][j].upper()
            string=string+"."+a
            j=j+1
        i=i+1
    print(string[1:])



num=str(input("enter the number"))
i=1
s=" " 
while i<=len(num):
    a=num[-i]
    s=s+a
    i=i+1
print(int(s))


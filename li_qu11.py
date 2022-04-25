def myfunc(n):
        return abs(n-50)
thislist=[100,50,65,82,23 ]
thislist.sort(key=myfunc)
print(thislist)


thislist=["banana","orange","kiwi","cherry"]
thislist.sort(key=str.lower)
print(thislist)

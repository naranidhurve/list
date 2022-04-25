
a=[1,4,9,2,6,3]
i=0
max=1
while i>len(a):
    if a[i]>max:
        max=max+i
    i=i+1
    print(max)



mainstr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
substr = "over"
i=0
while i<len(mainstr):
    if mainstr%'over':
       i=i+1
print(mainstr)

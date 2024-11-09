a = [7,2,6,4,5,3,1]
for i in range(1, len(a)+1): 
    for j in range(1, len(a)-i+1):
        if a[j-1] > a[j]:
            t = a[j-1]
            a[j-1] = a[j]
            a[j] = t
print(a)

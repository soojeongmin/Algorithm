k = int(input())
arr = []
d = 2
while d * d <= k:
    while k % d == 0:
        arr.append(d)
        k //= d
    d += 1
if k > 1: arr.append(k)

for i in arr:
    print(i)

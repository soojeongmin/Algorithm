a,b = map(int,input().split())
a -= 1
tmp_A, tmp_B = a, b
for i in range(1,50): tmp_A += (a//(2**i))*(2**i-2**(i-1))
for i in range(1,50): tmp_B += (b//(2**i))*(2**i-2**(i-1))
print(tmp_B - tmp_A)

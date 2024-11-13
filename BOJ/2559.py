a,b = map(int,input().split())
arr = list(map(int,input().split()))
p = [0 for _ in range(a+2)]
for i in range(0,a): p[i+1] = p[i] + arr[i]
ans = []
for k in range(b,a+1): ans.append(p[k] - p[k-b])
print(max(ans))

n = int(input())
arr = []
arr_x = []
arr_y = []

ans = [-1]*n
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])
    arr_x.append(a)
    arr_y.append(b)

for y in arr_y:
    for x in arr_x:
        dist = []

        for dx, dy in arr:
            distance = abs(dx-x) + abs(dy-y)
            dist.append(distance)

        dist.sort()

        tmp = 0

        for i in range(len(dist)):
            distance = dist[i]
            tmp += distance
            if ans[i] == -1:
                ans[i] = tmp
            else:
                ans[i] = min(tmp, ans[i])

print(*ans)

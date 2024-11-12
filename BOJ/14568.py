c = int(input())
a = 0
for A in range(0, c+1):
    for B in range(0, c+1):
        for C in range(0, c+1):
            if A + B + C == c:
                if A >= B+2:
                    if A != 0 and B != 0 and C != 0:
                        if C % 2 == 0:
                            a += 1
print(a)

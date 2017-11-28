n = int(input())
a = 0
b = 0
c = 0
d = 0
point = 0
for i in range(n):
    v,p = map(int,input().split())
    if v == 0:
        a += p
    elif v == 1:
        b += p
    elif v == 2:
        c += p
    elif v == 3:
        d += p

point += (a // 100) * 5
point += (b // 100) * 3
point += (c // 100) * 2
point += d // 100
print(point)

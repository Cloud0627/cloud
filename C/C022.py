n = int(input())
s = 0
e = 0
h = 0
l = 1000000
for i in range(n):
    s1,e1,h1,l1 = map(int,input().split())
    if i == 0:
        s = s1
    if i == n-1:
        e = e1
    if h <= h1:
        h = h1
    if l >= l1:
        l = l1
print(s,e,h,l)

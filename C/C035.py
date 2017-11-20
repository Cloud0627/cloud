num = int(input())
count = 0
for i in range(num):
    a,b,c,d,e,f = map(str,input().split())
    b1 = int(b)
    c1 = int(c)
    d1 = int(d)
    e1 = int(e)
    f1 = int(f)
    testnum = b1 + c1 + d1 + e1 + f1
    if a == "s":
        test = c1 + d1
    if a == "l":
        test = e1 + f1
    if testnum >= 350:

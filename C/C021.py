xc,yc,r1,r2 = map(int,input().split())
n = int(input())
for i in range(n):
    x1,y1 = map(int,input().split())
    if r1**2 <= (x1 - xc)**2 + (y1 - yc)**2 and (x1 - xc)**2 + (y1 - yc)**2 <= r2**2:
        print("yes")
    else:
        print("no")

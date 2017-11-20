a,b = map(int,input().split())
num = int(input())
for j in range(num):
    c,d = map(int,input().split())
    if a > c:
        print("High")
    elif a == c:
        if b < d:
            print("High")
        else:
            print("Low")
    else:
        print("Low")

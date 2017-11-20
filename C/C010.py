a,b,R = map(int,input().split())
N = int(input())
for i in range(N):
    x,y = map(int,input().split())
    if (x-a)**2 + (y-b)**2 >= R**2:
        print("silent")
    else:
        print("noisy")

n,r = map(int,input().split())
list1 = []
r2 = r*2
for i in range(n):
    h,w,d = map(int,input().split())
    if r2 <= h and r2 <= w and r2 <= d:
        list1.append(i+1)
list1.sort()
for j in range(len(list1)):
    print(list1[j])

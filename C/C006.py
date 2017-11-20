n,m,k = map(int,input().split())
list1 = map(float,input().split())
list1 = list(list1)
list3 = [0] * m
for i in range(m):
    list2 = map(int,input().split())
    list2 = list(list2)
    for b in range(n):
        list3[i] = list3[i] + (list1[b]*list2[b])
    list3[i] = int(round(list3[i],0))
list3.sort()
list3.reverse()
for j in range(k):
    print(list3[j])

n = int(input())
mylist1=[]
mylist2=[]
tag = 0
for i in range(n):
    mylist1.append(input().split())

mydict1=dict(mylist1)

m = int(input())
for j in range(m):
    mylist2.append(input().split())

mydict2=dict(mylist2)

list3 = mydict1.keys()
list3 = list(list3)
menu=[0]*len(list3)
for k in range(len(list3)):
    if list3[k] in mydict2:
        menu1 = mydict1.get(list3[k])
        menu2 = mydict2.get(list3[k])
        menu[k] = int(menu2) // int(menu1)
    else:
        break
    if k == len(list3)-1:
        tag = 1


if tag == 1:
    minimum = min(menu)
    print(minimum)
else:
    print(0)

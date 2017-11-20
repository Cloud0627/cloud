import math

num = int(input())
mount = 0
for i in range(num):
    day,total = map(str,input().split())
    if "3" in day:
        mount += math.floor((int(total) / 100) * 3)
    elif "5" in day:
        mount += math.floor((int(total) / 100) * 5)
    else:
        mount += math.floor(int(total) / 100)
print(int(mount))

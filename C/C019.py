n = int(input())
for k in range(n):
    num = int(input())
    count = 0
    for a in range(1,num):
        j = num % a
        if j == 0:
            count += a
    if num == count:
        print("perfect")
    elif abs(count - num) == 1:
        print("nearly")
    else:
        print("neither")

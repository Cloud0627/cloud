n = int(input())
actuallyHight = 200
actuallyLow = 100
for i in range(n):
    hantei,cm = map(str,input().split())
    if hantei == "le":
        if actuallyHight >= float(cm):
            actuallyHight = float(cm)
    elif hantei == "ge":
        if actuallyLow <= float(cm):
            actuallyLow = float(cm)
print(actuallyLow,actuallyHight)

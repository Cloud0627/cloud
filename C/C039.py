num = str(input())
count = 0
for i in range(len(num)):
    if num[i] == "/":
        count += 1
    elif num[i] == "<":
        count += 10
    elif num[i] == "+":
        continue
print(count)

n = int(input())
i1 = 0
i2 = 0
for a in range(n):
    command = []
    command = input().split()
    if command[0] == "SET":
        if command[1] == "1":
            i1 = int(command[2])
        elif command[1] == "2":
            i2 = int(command[2])
    elif command[0] == "ADD":
        i2 = i1 + int(command[1])
    elif command[0] == "SUB":
        i2 = i1 - int(command[1])
print(i1,i2)

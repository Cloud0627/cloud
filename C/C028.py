num = int(input())
count = 0
for i in range(num):
    answer,test = map(str,input().split())
    if answer == test:
        count+=2
    elif len(answer) == len(test):
        misscount = 0
        for n in range(len(answer)):
            if answer[n] != test[n]:
                misscount+=1
            if misscount == 2:
                break
            if n == len(answer)-1:
                count+=1
print(count)

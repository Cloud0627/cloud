tousen = map(int,input().split())
tousen = list(tousen)
n = int(input())
for i in range(n):
    count = 0
    kuji = []
    kuji = map(int,input().split())
    kuji = list(kuji)
    for j in range(6):
        for  k in range(6):
            if tousen[j] == kuji[k]:
                count += 1
    print(count)

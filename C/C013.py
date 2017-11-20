hate = input()
n = int(input())
s = [input() for i in range(n)] #N回繰り返し s に値を取得
count = 0
for i in range(n):
    #print(s[i])
    if hate in s[i]:
        continue
    else:
        count+=1
        print(s[i])
if count == 0:
    print("none")

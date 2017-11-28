#未回答
num = int(input())
strike = 0
ball = 0
for i in range(num):
    string = input()
    if string == "strike":
        strike += 1
        if strike == 3:
            print("out!")
            break
        print("strike!")
    elif string == "ball":
        ball += 1
        if ball == 4:

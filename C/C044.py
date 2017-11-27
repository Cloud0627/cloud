n = int(input())
a = [0] * n
for i in range(n):
    a[i] = str(input())
if "rock" in a and "scissors" in a and "paper" in a:
    print("draw")
elif a.count("rock") == n:
    print("draw")
elif a.count("scissors") == n:
    print("draw")
elif a.count("paper") == n:
    print("draw")
else:
    if "rock" in a and "scissors" in a:
        print("rock")
    elif "rock" in a and "paper" in a:
        print("paper")
    elif "scissors" in a and "paper" in a:
        print("scissors")

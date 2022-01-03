n = 26 ## int(input())
num = n
score = 0
while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c

    score += 1
    if (num == n):
        break

print(score)
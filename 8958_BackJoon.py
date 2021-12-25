n = 5
a = ["OOXXOXXOOO","OOXXOOXXOO","OXOXOXOXOXOXOX","OOOOOOOOOO","OOOOXOOOOXOOOOX"]

score = 0
answer = []
for j in a:
    answer = []
    for i in range(len(j)):
        if j[i] == "O":
            score += 1
            answer.append(score)
        elif j[i] == "X":
            score = 0
            answer.append(score)
    print(sum(answer))
    score = 0

## 백준답
n = int(input())
a = []
for i in range(n):
    a.append(input())
score = 0
answer = []
for j in a:
    answer = []
    for i in range(len(j)):
        if j[i] == "O":
            score += 1
            answer.append(score)
        elif j[i] == "X":
            score = 0
            answer.append(score)
    print(sum(answer))
    score = 0
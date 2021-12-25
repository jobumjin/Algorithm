n = 4
NUM = [1, 100, 100, 100]
answer = []
for i in NUM:
    answer.append(i/max(NUM)*100)
print(sum(answer)/n)

## 백준 답
n = int(input())
NUM = list(map(int,input().split()))
answer = []
for i in NUM:
    answer.append(i/max(NUM)*100)
print(sum(answer)/n)
n = 5
case =[[5,50,50,70,80,100],[7,100,95,90,80,70,60,50],[3,70,90,80],[3,70,90,81],[9,100,99,98,97,96,95,94,93,91]]

for i in case:
    a = 0
    for j in i:
        if j > (sum(i)-i[0])/i[0]:
            a += 1
    print("{:.3f}%".format(a / i[0] * 100))

## 백준에서는 한 줄씩 입력받고 출력하기를 원했다.
n = int(input())
for i in range(n):
    case = list(map(int, input().split()))
    a = 0
    for j in case[1:]:
        if j > (sum(case[1:]))/case[0]:
            a += 1
    print("{:.3f}%".format(a / case[0] * 100))
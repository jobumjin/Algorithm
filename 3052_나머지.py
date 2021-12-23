answer = []
for i in range(10):
    i = int(input())
    answer.append(i%42)
print(len(set(answer)))
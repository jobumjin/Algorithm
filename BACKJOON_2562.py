m = []
for i in range(9):
    m.append(int(input()))
a = 1
print(max(m))
for i in range(len(m)):
    if m[i] == max(m):
        print(a)
    else:
        a += 1
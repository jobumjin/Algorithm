A, B, C = 150 ,266, 427
X = list(map(int,str(A * B * C)))
for i in range(10):
    print(X.count(i))
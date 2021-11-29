from sys import stdin
N, M = map(int,stdin.readline().split())
nolisten = [stdin.readline().strip() for i in range(N)]
nosee = [stdin.readline().strip() for j in range(M)]

V = sorted(list(set(nolisten)&(set(nosee))))

print(len(V))
for i in range(len(V)):
    print(V[i])
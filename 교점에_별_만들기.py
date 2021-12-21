X = [[2,-1,4],[-2,-1,4],[0,-1,1],[5,-8,-12],[5,8,12]]
answerX = []
answerY = []
result = []
for i in range(len(X)):
    for j in range(len(X)):
        if X[i][0] * X[j][1] - X[i][1] * X[j][0] != 0:
            answerX.append((X[i][1] * X[j][2] - X[i][2] * X[j][1]) / (X[i][0] * X[j][1] - X[i][1] * X[j][0]))
            answerY.append((X[i][2] * X[j][0] - X[i][0] * X[j][2]) / (X[i][0] * X[j][1] - X[i][1] * X[j][0]))

answer = list(zip(answerX,answerY))

for i in range(len(answer)):
    if answer[i][0].is_integer() & answer[i][1].is_integer():
        result.append(answer[i])
result1 = list(set(result))
print(result1)

final = [] * int(max(answerY)-min(answerY)+1)

for i in range(int(max(answerY)-min(answerY)+1)):
    final.append(list("." * int(max(answerX)-min(answerX)+1)))

for i in range(len(result1)):
    a = abs(int(max(answerY)) - int(result1[i][1]))
    b = abs(int(min(answerX)) - int(result1[i][0]))
    final[a][b] = "*"

ans = []
for i in final:
    ans.append(''.join(i))

print(ans)

### 다른사람풀이.. 내꺼는 안되는게 있는 이유가 뭘까... 조금 더 생각해보자..

def solution(line):
    INF = float('inf')
    mark,L = [],len(line)
    minx,maxx,miny,maxy=INF,-INF,INF,-INF
    for i in range(L):
        for j in range(i,L):
            if i==j : continue
            A,B,E,C,D,F = *line[i],*line[j]
            mo = A*D-B*C
            if mo==0: continue
            x,y=(B*F-E*D)/mo,(E*C-A*F)/mo
            if x-int(x) or y-int(y) : continue
            x,y=int(x),int(y)
            minx,maxx,miny,maxy = min(minx,x),max(maxx,x),min(miny,y),max(maxy,y)
            mark.append((x,y))
    res=[['.' for _ in range(maxx-minx+1)] for _ in range(maxy-miny+1)]
    for x,y in mark : res[maxy-y][x-minx] = '*'
    return [''.join(s) for s in res]
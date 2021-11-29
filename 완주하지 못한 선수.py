from collections import Counter

def solution(a,b):
    a.sort()
    b.sort()
    answer = Counter(a)-Counter(b)
    return list(answer)[0]

a = ["leo","kiki","eden","ddo","kiki"]
b = ["eden","kiki","ddo","leo"]

print(solution(a,b))

# 다른사람 풀이 :: 딕셔너리를 활용..

def solution(a, b)
    answer = " "
    temp = ()
    dic = {}
    for A in a:
        dic[hash(A)] = A
        temp += int(hash(A))
    for B in b:
        temp -= hash(B)
    answer = dic[temp]
    return answer
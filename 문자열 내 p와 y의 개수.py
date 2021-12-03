def solution(s):
    v = 0
    w = 0
    for i in range(len(s)):
        if s[i] == "P" or s[i] == "p":
            v += 1
        elif s[i] == "Y" or s[i] == "y":
            w += 1
        else:
            pass
    return v == w

##다른사람 풀이
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )


print(solution("pPoooyY"))
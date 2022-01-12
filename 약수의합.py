##Test case
n = 12
result = 28

##나의 첫 풀이
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    return answer
print(solution(n))

#성능 업그레이드
def solution(n):
    answer = 0
    for i in range(1,n//2+1):
        if n % i == 0:
            answer += i
    return answer + n
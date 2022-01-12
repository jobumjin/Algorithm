def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer = answer + "수"
        else:
            answer = answer + "박"
    return answer

#다른사람
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)
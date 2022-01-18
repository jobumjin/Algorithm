def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x*(1+i))
    return answer

print(solution(2,5))

##다른사람풀이

def number_generator(x, n):
    return [i * x + x for i in range(n)]

print(number_generator(2, 5))
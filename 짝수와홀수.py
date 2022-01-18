def solution(num):
    answer = ''
    if num % 2 != 0:
        answer = "Odd"
    else:
        answer = "Even"
    return answer

print(solution(3))
print(solution(4))

##다른사람풀이
def evenOrOdd(num):
    return "Even" if num%2 == 0 else "Odd"
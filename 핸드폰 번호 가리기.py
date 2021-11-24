def solution(phone_number):
    answer = ''
    answer += "*"*(len(phone_number)-4)
    answer += phone_number[-4:]
    return answer

a = "01033334444"
print(solution(a))
def solution(n):
    return sum(list(map(int,str(n))))

print(solution(123))

##다른사람풀이
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10)

print("결과 : {}".format(sum_digit(123)));

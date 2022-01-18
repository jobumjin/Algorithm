def solution(s):
    answer = ""
    if len(s) % 2 == 1:
        answer = s[len(s) // 2]
    else:
        answer = s[len(s) // 2 - 1] + s[len(s) // 2]
    return answer


s1 = "abcde"
s2 = "qwer"
print(solution(s1))
print(solution(s2))


### 다른사람 풀이
def string_middle(str):
    return str[(len(str) - 1) // 2:len(str) // 2 + 1]


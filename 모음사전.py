import itertools

def solution(word):
    arr = ["A","E","I","O","U"]

    data1 = list(itertools.product(arr,repeat = 5))
    data2 = list(itertools.product(arr,repeat = 4))
    data3 = list(itertools.product(arr,repeat = 3))
    data4 = list(itertools.product(arr,repeat = 2))
    data5 = list(itertools.product(arr,repeat = 1))
    data = data1 + data2 + data3 + data4 + data5

    str = []
    for i in data:
        str.append("".join(i))

    answer = sorted(str).index(word)+1
    return answer

print(solution("AAAAE"))
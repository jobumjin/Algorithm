#test_sample
n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]
#나의 풀이
arr3 = []
for i in range(n):
    arr3.append(arr1[i]|arr2[i])
    arr3[i] = format(arr3[i],"b")
    arr3[i] = arr3[i].replace("1","#")
    arr3[i] = arr3[i].replace("0"," ")
    arr3[i] = arr3[i].rjust(n)
print(arr3)

#다른사람 풀이 1 이게..한줄이 된다고..?
solution = lambda n, arr1, arr2: ([''.join(map(lambda x: '#' if x=='1' else ' ', "{0:b}".format(row).zfill(n))) for row in (a|b for a, b in zip(arr1, arr2))])

#다른사람 풀이 2 정규식
import re

def solution(n, arr1, arr2):
    answer = ["#"]*n
    for i in range(0, n):
        answer[i] = str(bin(arr1[i]|arr2[i]))[2:]
        answer[i] = re.sub('1', '#', '0'*(n-len(answer[i]))+answer[i])
        answer[i] = re.sub('0', ' ', answer[i])
    return answer
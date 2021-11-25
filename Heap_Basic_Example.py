import sys
import heapq
read = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heqpq.heappush(h,value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(read())
arr = []

for i in range(n):
    arr.append(int(read()))

res = heapsort(arr)

for i in range(n):
    print(res[i])
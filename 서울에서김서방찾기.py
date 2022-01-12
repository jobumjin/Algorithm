def solution(seoul):
    answer = ""
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = '김서방은 {0}에 있다'.format(i)
            break
    return answer

#다른사람풀이

def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

#아직도 너무 많이 부족하다. 쉬운문제를 풀면서도 한참을 고민하는 모습이.. 발전해서 좋은 코딩을 할 수 있길 소망한다.
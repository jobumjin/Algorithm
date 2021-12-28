m = int(input())

a = [False,False] + [True]*(10**m-1)
primes=[]

for i in range(2,10**m//2):
    # if a[i]:
    #     primes.append(i)
    for j in range(2*i, 10**m, i):
        a[j] = False

def judge(num):
    while len(num):
        num=int(num)
        if not a[num]:
            return False
        num=str(num)
        num=num[:-1]
    return True


def sol(num):
    for i in range(num,num*10):
        if judge(str(i)):
            print(i)

    return

sol(10**(m-1))
########
import sys
N=int(sys.stdin.readline())

def isSosu(num):
    if num==0 or num==1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

def DFS(num):
    if len(str(num))==N:
        print(num)
    else:
        for i in range(10):
            tmp_num=num*10+i
            if isSosu(tmp_num):
                DFS(tmp_num)

DFS(2)
DFS(3)
DFS(5)
DFS(7)

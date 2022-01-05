#s = "beakjoon"
s = input()
m = "abcdefghijklmnopqrstuvwxyz"
for i in m:
    if i in s:
        print(s.index(i),end = " ")
    else:
        print(-1,end = " ")
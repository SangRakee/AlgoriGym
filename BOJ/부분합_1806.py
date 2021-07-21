# 2pointer 문제

import sys

N,M=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))
num.append(0)

answer=N
left=0
right=0
sumIndex=num[0]

if sum(num)<M:
    print(0)
else:
    while left<N and right<N:
        if sumIndex<M:
            right+=1
            sumIndex+=num[right]
        elif sumIndex>=M:
            answer=min(answer,right-left+1)
            # print(sum, left, right)
            # print(answer)
            sumIndex-=num[left]
            left+=1
    print(answer)


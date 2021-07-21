# 2pointer 문제

import sys

N,M=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))
num.append(0)

answer=0
left=0
right=0
sum=num[0]

while left<N and right<N:

    if sum<M:
        right+=1
        sum+=num[right]
    elif sum>M:
        sum-=num[left]
        left+=1
    elif sum==M:
        answer+=1
        sum-=num[left]
        left+=1
    # print(sum,left,right)

print(answer)


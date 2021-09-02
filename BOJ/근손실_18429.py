# 완전탐색
# 단순 구현 문제

import sys
from itertools import permutations

N,K=map(int,sys.stdin.readline().split())
kits=list(map(int,sys.stdin.readline().split()))

arr=[i for i in range(1,N+1)]
per=list(permutations(arr,N))
# print(per)

answer=0
for i in per:
    temp=[]
    x=500
    for j in range(N):
        x=x+kits[i[j]-1]-K
        if x<500:
            break
        else:
            temp.append(x)
    if len(temp)==N:
        answer+=1
print(answer)
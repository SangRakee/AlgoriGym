# 슬라이딩 윈도우 문제

import sys

N,K,B=map(int,sys.stdin.readline().split())
arr=[0]*(N+1)
for _ in range(B):
    x=int(sys.stdin.readline())
    arr[x]=1

# print(arr)

query=[]
left=1
right=K
cnt=0
for i in range(left,right+1):
    if arr[i]==1:
        cnt+=1

result=[cnt]

# 0: 정상 1: 비정상
for i in range(1,N-K+1):
    if arr[left]==1:
        cnt-=1

    if arr[right+1]==1:
        cnt+=1

    result.append(cnt)
    left+=1
    right+=1
    # print(cnt, left, right)

print(min(result))


# 누적합 문제
# 그냥 완탐으로 하면 시간초과 발생
# 각 경우의 누적합을 구한다음에 해당 범위(i,j)에서 j의 누적합-i의 누적합 빼는 방식

import sys

arr=[]

N,M=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))

arr=[0]
temp=0
for i in range(len(num)):
    temp+=num[i]
    arr.append(temp)
# print(arr)

for _ in range(M):
    i,j=map(int,sys.stdin.readline().split())
    result=arr[j]-arr[i-1]
    print(result)

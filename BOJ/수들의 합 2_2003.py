# 2pointer 문제

import sys


n,m=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))
num.append(0) #벗어 났을때 임의로 넣는값

left=0
right=0
answer=0

sumIndex=num[0]
while True:

    if sumIndex<m: #합이 m보다 작으면 right++
        right+=1
        sumIndex+=num[right]
    elif sumIndex>m: #합이 m보다 크면 left++
        sumIndex -= num[left]
        left+=1
        # sumIndex+=num[left]
    elif sumIndex==m: #합이 m과 같을 시 answer++
        answer+=1
        sumIndex -= num[left]
        left+=1
        #그리고 왼쪽 이동
    #left,right가 배열 밖으로 벗어날때
    if right==n:
        break


print(answer)


# 구현 문제
# deque 사용안하고 그냥 리스트 사용하면 시간초과 발생

import sys
from collections import deque

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 5.폭탄을 상하좌우로 폭발시킬 함수
def bfs(time,bomb,arr1):

    temp = [["O"] * len(arr1[0]) for i in range(len(arr1))] # 폭발 후, 잔여 폭탄 위치를 담는 리스트

    # 5-1. 폭탄의 좌표가 들어있는 Queue가 빌때까지
    while bomb:
        x,y=bomb.popleft() # 폭탄좌표 추출
        temp[x][y]="."

        # 상하좌우 이동
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<len(arr1) and 0<=ny<len(arr1[0]):
                temp[nx][ny]="."

    return temp

# 1.입력1
R,C,N=map(int,sys.stdin.readline().split())

# 2.입력2
arr1=[]
for _ in range(R):
    x=list(map(str,sys.stdin.readline().replace("\n","")))
    arr1.append(x)


time=1
arr2=[["O"]*C for i in range(R)]

for _ in range(N):
    # 3.폭탄이 3초가 지날때
    if time%2==1 and time!=1:
        bomb = deque([]) # 폭탄의 좌표를 삽입할 Queue

        # 4.폭탄위치 감지
        for i in range(R):
            for j in range(C):
                if arr1[i][j] == "O":
                    bomb.append([i, j])

        # 5.폭탄을 상하좌우로 폭발시킬 함수
        arr1=[i[:] for i in bfs(time,bomb,arr1)]
        # print(arr1)
    time+=1

# 6.출력
if N%2==1:
    for i in range(R):
        print("".join(arr1[i]))
else:
    for i in range(R):
        print("".join(arr2[i]))



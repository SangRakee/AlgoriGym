# 시뮬레이션
# 1.상하좌우로 바뀌는 기준이 기존의 방식과 다름
# 2.큐를 이용하여 꼬리의 위치 파악

import sys
from collections import deque

#상우하좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def start(arr):
    # 출발지 설정
    direct=1
    time=0
    x,y=0,0
    snake=deque([(x,y)])
    arr[x][y]=2
    # 이동
    while True:
        nx=x+dx[direct]
        ny=y+dy[direct]
        time+=1
        if (0<=nx<N and 0<=ny<N) and arr[nx][ny]!=2:
            # print(nx, ny ," ",time)
            # 사과를 만날때
            if arr[nx][ny] == 1:
                snake.append((nx,ny))
                arr[nx][ny]=2
                # 그대로
            else: # 사과를 안만날때
                snake.append((nx, ny))
                arr[nx][ny]=2
                tailX,tailY=snake.popleft()
                arr[tailX][tailY]=0 # 꼬리를 줄이기
            if time in inf.keys():
                if inf[time]=="D":
                    direct=(direct+1)%4
                elif inf[time]=="L":
                    direct=(direct-1)%4
            x=nx
            y=ny

        else: # 벽에 붙이칠때
            print(time)
            return time


N=int(sys.stdin.readline())
arr=[[0]*N for i in range(N)]

K=int(sys.stdin.readline())
for _ in range(K):
    r,c=map(int,sys.stdin.readline().split())
    arr[r-1][c-1]=1

inf={}
L=int(sys.stdin.readline())
for _ in range(L):
    X,C=sys.stdin.readline().split()
    inf[int(X)]=C

start(arr)

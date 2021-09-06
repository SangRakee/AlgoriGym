# 벽 부수고 이동하기 문제
# bfs 문제

import sys
from collections import deque

#서북동남
dx=[0,-1,0,1]
dy=[-1,0,1,0]

def check(i,j):
    direction=[0,0,0,0]
    x=arr1[i][j]

    for k,v in enumerate((8,4,2,1)):
        if x-v<0:
            continue
        else:
            direction[3-k]=1
            x=x-v

    return direction

def bfs(i,j,cnt):
    weight=0
    queue=deque([(i,j)])
    vistied[i][j]=cnt

    # 큐에서 하나씩 추출
    while queue:
        # print(queue)
        x,y=queue.popleft()
        weight+=1
        direction=check(x,y)
        # 목적지 인가

        # 갈 수 있는곳 순회
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            # 갈 수 있는가
            if 0<=nx<m and 0<=ny<n:
                if direction[k]==0 and vistied[nx][ny]==0:
                    # 큐에 넣기
                    queue.append((nx,ny))
                    # 체크인
                    vistied[nx][ny]=cnt
    return weight

n,m=map(int,sys.stdin.readline().split())
arr1=[]
for _ in range(m):
    x=list(map(int,sys.stdin.readline().split()))
    arr1.append(x)

cnt_room=0
room=[]

vistied=[[0]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        # 1. 방문한 적이 없으면
        if vistied[i][j]==0:
            # 방의 갯수 +1
            cnt_room += 1
            # 방문
            room.append(bfs(i,j,cnt_room))


print(cnt_room)
print(max(room))


max_room=0
for i in range(m):
    for j in range(n):
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < m and 0 <= nj < n:
                if vistied[i][j] != vistied[ni][nj]:
                    temp = room[vistied[i][j]-1] + room[vistied[ni][nj]-1]
                    max_room = max(temp, max_room)

print(max_room)
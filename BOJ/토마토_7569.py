# BFS
# 3차원 리스트 탐색 문제

import sys
from collections import deque


#상하좌우앞뒤
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,1,-1]

def bfs():
    # 큐에서 꺼내기
    while queue:
        z,x,y=queue.popleft()

        # 갈 수 있는곳 순회
        for k in range(6):
            nz=z+dz[k]
            nx=x+dx[k]
            ny=y+dy[k]

            # 갈 수 있는가
            if 0<=nz<H and 0<=nx<N and 0<=ny<M:
                if visited[nz][nx][ny]==0 and boxes[nz][nx][ny]==0:
                    # 큐에 추가
                    queue.append([nz,nx,ny])
                    # 체크인
                    visited[nz][nx][ny]=1
                    boxes[nz][nx][ny]=boxes[z][x][y]+1


M,N,H=map(int,sys.stdin.readline().split())

boxes=[[]for i in range(H)]
for i in range(H):
    for _ in range(N):
        x=list(map(int,sys.stdin.readline().split()))
        boxes[i].append(x)

queue=deque([])
visited=[[[0]*M for i in range(N)] for i in range(H)]
for z in range(H):
    for x in range(N):
        for y in range(M):
            if boxes[z][x][y]==1:
                queue.append([z,x,y])
                visited[z][x][y]=1

# print(boxes)
bfs()

answer=0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if boxes[z][x][y]==0:
                print(-1)
                sys.exit(0)
            else:
                answer=max(answer,boxes[z][x][y])

print(answer-1)

# bfs 문제
# 벽을 부술수 있는지 판단하기 위해 visited 리스트를 3차원으로 만듬

import sys
from _collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(r,c,broken):
    visited = [[[0] * 2 for i in range(M)] for i in range(N)]
    q=deque([])
    q.append((r,c,broken))
    visited[r][c][broken]=1

    # 큐에서 하나씩 추출
    while q:
        x,y,w=q.popleft()

        # 목적지인가
        if x==N-1 and y==M-1:
            # print(visited)
            return visited[x][y][w]

        # 갈 수 있는 곳 순회
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            # 갈 수 있는가
            if 0<=nx<N and 0<=ny<M:
                if matrix[nx][ny]=="1" and w==1:
                    visited[nx][ny][0]=visited[x][y][1]+1
                    q.append((nx, ny,0))
                elif matrix[nx][ny]=="0" and visited[nx][ny][w]==0:
                    visited[nx][ny][w]=visited[x][y][w]+1
                    q.append((nx,ny,w))
    return -1



N,M=map(int,sys.stdin.readline().split())
matrix=[]
for _ in range(N):
    x=list(sys.stdin.readline().rstrip())
    matrix.append(x)

# print(matrix)
print(bfs(0,0,1))

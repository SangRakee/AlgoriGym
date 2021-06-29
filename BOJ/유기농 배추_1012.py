from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

t=int(input())

def bfs(farm,visited,row,col):
    queue=deque([])
    queue.append([row,col])
    visited[row][col]=1

    while queue:
        x,y=queue.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if farm[nx][ny]==1 and visited[nx][ny]==0:
                    queue.append([nx,ny])
                    visited[nx][ny]=1



for _ in range(t):
    m,n,k=map(int,input().split()) # m가로 n세로 k갯수
    answer=0

    farm=[[0]*m for i in range(n)]
    visited=[[0]*m for i in range(n)]


    for count in range(k):
        y,x=map(int,input().split())
        farm[x][y]=1
        # print(farm)


    for i in range(n):
        for j in range(m):
            if farm[i][j]==1 and visited[i][j]==0:
                bfs(farm,visited,i,j)
                answer+=1

    print(answer)

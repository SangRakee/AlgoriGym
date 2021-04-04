from _collections import deque

n,m=map(int,input().split())
grahp=[]

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(graph,visited,column,row,n,m):
    queue=deque([])
    queue.append([column,row])
    visited[column][row] = 1
    while queue:
        cx,ry=queue.popleft()
        for k in range(4):
            nx=cx+dx[k]
            ny=ry+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if grahp[nx][ny]==1 and visited[nx][ny] == 1e9:
                    queue.append([nx,ny])
                    visited[nx][ny] = min(visited[nx][ny], visited[cx][ry] + 1)


for i in range(n):
    x=list(map(int,input()))
    grahp.append(x)

visited=[[1e9]*m for i in range(n)]
answer=0
cnt=0
bfs(grahp,visited,0,0,n,m)

#print(visited)

print(visited[n-1][m-1])
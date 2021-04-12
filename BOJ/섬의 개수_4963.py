from collections import deque

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1,1,1,-1,-1]
dy = [-1, 1, 0, 0,-1,1,1,-1]



def bfs(graph,visited,column,row):
    visited[column][row]=1
    queue = deque([])
    queue.append([column, row])
    while queue:
        c, r = queue.popleft()
        for k in range(8):
            nx=c+dx[k]
            ny=r+dy[k]
            if 0<=nx<h and 0<=ny<w:
                if visited[nx][ny]==0 and graph[nx][ny]==1:
                    queue.append([nx,ny])
                    visited[nx][ny]=1


while True:
    w,h=map(int,input().split())
    visited=[[0]*w for i in range(h)]
    graph=[]
    cnt=0

    if w == 0 and h == 0:
        break

    for i in range(h):
        x=list(map(int,input().split()))
        graph.append(x)

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs(graph,visited,i,j)
                cnt+=1

    print(cnt)



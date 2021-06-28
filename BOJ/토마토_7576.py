from collections import deque

m,n=map(int,input().split())
farm=[]

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[0]*m for i in range(n)]
answer=0

#입력
for i in range(n):
    x=list(map(int,input().split()))
    farm.append(x)

def bfs(farm,visited,n,m,answer,queue):
    while queue:
        answer+=1
        for _ in range(len(queue)):
            x,y=queue.popleft()
            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]
                if 0<=nx<n and 0<=ny<m:   # 4 6
                    # print(nx,ny)
                    if farm[nx][ny]==0 and visited[nx][ny]==0:
                        queue.append([nx,ny])
                        farm[nx][ny]=1
                        visited[nx][ny]=1

    #익지 않은 토마토 남아있는 경우 -1 반환
    for i in range(len(farm)):
        for j in range(len(farm[i])):
            if farm[i][j] == 0:
                return -1

    #모두 익은 경우 일수 출력
    return answer - 1

queue=deque([])

for i in range(len(farm)):
    for j in range(len(farm[0])):
        if farm[i][j]==1:
            queue.append([i,j])
            visited[i][j]=1

print(bfs(farm,visited,n,m,answer,queue))
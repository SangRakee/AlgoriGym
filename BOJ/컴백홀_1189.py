#백트래킹

import sys

answer=0
#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,cnt):
    global answer
    #체크인
    visited[x][y]=1
    #목적지인가
    if x==0 and y==C-1 and cnt==K:
        answer+=1
        return
    #갈수있는곳 순회
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        #갈수 있는가
        if 0<=nx<R and 0<=ny<C:
            if visited[nx][ny]==0 and arr1[nx][ny]!="T":
                visited[nx][ny]=1
                # 간다
                bfs(nx,ny,cnt+1)
                # 체크아웃
                visited[nx][ny]=0



R,C,K=map(int,sys.stdin.readline().split())
arr1=[]
for _ in range(R):
    x=str(sys.stdin.readline())
    x=x.replace("\n","")
    arr1.append(x)

cnt=1
visited=[[0]*C for i in range(R)]
bfs(R-1,0,cnt)

print(answer)
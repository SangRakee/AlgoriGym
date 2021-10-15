# 시뮬레이션
# 삼성 기출

from collections import deque


def bfs(r,c,visited,temp):
    queue=deque([])
    queue.append([r,c])
    visited[r][c]=1

    # 큐에서 추출
    while queue:
        x,y=queue.popleft()

        # 갈 수 잇는 곳 순회
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            # 갈 수 있는가
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny]==0:
                    if L<=abs(arr[x][y]-arr[nx][ny])<=R:
                        queue.append([nx,ny])
                        visited[nx][ny]=1
                        if [nx,ny] not in temp:
                            temp.append([nx,ny])
                        if [x,y] not in temp:
                            temp.append([x,y])
    # 큐에 넣기

    # 방문 체크크


    return

def change(temp,arr):
    answer=0
    leng=0
    for x,y in temp:
        leng+=1
        answer+=arr[x][y]
    answer=answer//leng
    for x,y in temp:
        arr[x][y]=answer

    return arr

# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]


# 입력
N,L,R=map(int,input().split())
arr=[]
for i in range(N):
    x=list(map(int,input().split()))
    arr.append(x)

cnt=0
while True:
    temp=[]
    a=[]
    visited = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                bfs(i,j,visited,temp)
                # print(temp)
                if temp:
                    arr=change(temp,arr)
                    a=[i[:] for i in temp]
                    temp=[]
    if len(a)==0:
        break
    cnt+=1

print(cnt)



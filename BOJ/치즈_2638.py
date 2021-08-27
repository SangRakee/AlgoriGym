# 플러드 필 알고리즘(bfs)
# 처음 문제를 풀때, 단순 상하좌우가 0인 부분이 2면 이상일때 외부 공간으로 인식하여 문제를 풀어서 틀림
# bfs를 두번 사용하여 두단계로 나눔
# 첫번째 bfs : 외부 공간 파악, 두번째 bfs : 격자 파악
# 첫번째 bfs 같은 경우, 상하좌우에 치즈가 없는 경우를 파악

import sys
from collections import deque

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def func(r,c):
    # 방문체크
    visited[r][c]=1
    q=deque([])
    q.append([r,c])
    arr1[r][c]=2
    # 큐에서 추출
    while q:
        x,y=q.popleft()
        arr1[x][y]=2 # 외부 공간 2로 변환

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 갈 수 있는가
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny]==0 and arr1[nx][ny]!=1:
                    # 체크인
                    visited[nx][ny]=1
                    # 큐에 추가
                    q.append([nx,ny])


def bfs(queue,arr1):
    temp = [i[:] for i in arr1]
    # 큐에서 추출
    while queue:
        x,y=queue.popleft()
        cnt=0
        # 추출한 위치에서 상하좌우 판단
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<N and 0<=ny<M:
                if arr1[nx][ny]==2:
                    cnt+=1

        # 접촉면이 두군데 이면 삭제
        if cnt>=2:
            temp[x][y]=0
    return temp

N,M=map(int,sys.stdin.readline().split())
arr1=[]
for _ in range(N):
    x=list(map(int,sys.stdin.readline().split()))
    arr1.append(x)

answer=0
while True:
    visited=[[0]*M for i in range(N)]
    func(0,0) #외부 공간 파악 함수
    # print(arr1)
    queue=deque([])
    for i in range(N):
        for j in range(M):
            if arr1[i][j]==1:
                queue.append([i,j])

    if len(queue)==0:
        print(answer)
        sys.exit(0)
    temp=bfs(queue,arr1)
    arr1=[i[:] for i in temp]
    answer+=1

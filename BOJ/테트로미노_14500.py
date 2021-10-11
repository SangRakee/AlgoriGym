# bfs 문제
# 처음 시간 초과가 발생하였음
# (대처방안1) 미리 인덱스의 최댓값을 구해서 현재의 위치에서 나머지가 최대 인덱스값으로 가득찼을때보다 이전 값이 크면 return (다 구하기 전에 예상하는 것)
# (대처방안2) 각 좌표에서 방문체크 리스트를 매번 만드는 것X

import sys

def dfs(x,y,cnt,total):
    global answer

    # 체크인
    # visited[x][y]=1
    # cnt가 4일때 리턴
    if cnt==4:
        answer=max(answer,total)
        return
    # 기존 answer가 total + max_index*(3-cnt)보다 클때 리턴
    if answer>=(total+max_index*(4-cnt)):
        return

    # 갈 수 있는 곳 순회
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        # 갈 수 있는가
        if 0<=nx<N and 0<=ny<M:
            if visited[nx][ny]==0:
                # 'ㅗ'의 모양을 만들기 위한 경우의 수
                if cnt==2:
                    visited[nx][ny]=1
                    dfs(x,y,cnt+1,total+arr[nx][ny])
                    visited[nx][ny]=0
                visited[nx][ny]=1
                dfs(nx,ny,cnt+1,total+arr[nx][ny])
                visited[nx][ny]=0


#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

N,M=map(int,sys.stdin.readline().split())

arr=[]
for i in range(N):
    x=list(map(int,sys.stdin.readline().split()))
    arr.append(x)

# print(arr)

# 최대 인덱스 찾기
max_index=0
for i in arr:
    tmp=max(i)
    max_index=max(max_index,tmp)

# print(max_index)
cnt=1
answer=0
visited = [[0]*M for i in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j]=1
        dfs(i,j,cnt,arr[i][j])
        visited[i][j]=0

print(answer)
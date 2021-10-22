# BFS
# 삼성 SW 역량 테스트

# 기존 코드에서 조합을 직접 구현

import sys
from collections import deque
# from itertools import combinations

def combinations(arr,start,vis,cnt,tmp_comb):
    global comb_list

    # 목적지 인가
    if cnt==3:
        # print(tmp_comb)
        comb_list.append(tmp_comb[:])
        return

    # 갈 수 있는 곳 순회
    for i in range(start,len(arr)):
        if vis[i]==0:
            vis[i]=1
            tmp_comb.append(blank[i])
            cnt+=1
            combinations(arr,i,vis,cnt,tmp_comb)
            tmp_comb.pop()
            vis[i]=0
            cnt-=1


    return


def bfs(tmp_map,tmp_virus):

    visited = [[0] * M for i in range(N)]

    # cnt=len(tmp_virus)

    # 큐에서 꺼내기
    while tmp_virus:
        x,y=tmp_virus.popleft()

        visited[x][y]=1

        # 갈 수 있는 곳 순회
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            # 갈 수 있는가
            if 0<=nx<N and 0<=ny<M:
                if tmp_map[nx][ny]==0:
                    if visited[nx][ny]==0:
                        tmp_map[nx][ny]=2
                        tmp_virus.append([nx,ny])



#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 입력
N,M=map(int,sys.stdin.readline().split())

maps=[]
for _ in range(N):
    x=list(map(int,sys.stdin.readline().split()))
    maps.append(x)

# print(maps)

# 바이러스, 빈칸 위치 찾기
virus=[]
blank=[]
for i in range(N):
    for j in range(M):
        if maps[i][j]==2:
            virus.append([i,j])
        elif maps[i][j]==0:
            blank.append([i,j])

# 빈칸 위치 조합
comb_list=[]
tmp_comb=[]
vis=[0]*len(blank)
combinations(blank,0,vis,0,tmp_comb)
# print(comb_list)


answer=0

for comb in comb_list:
    # print(comb)
    a,b,c=comb
    # print(a,b,c)
    tmp_virus=deque(virus[:])
    tmp_map=[i[:] for i in maps]
    tmp_map[a[0]][a[1]]=1
    tmp_map[b[0]][b[1]]=1
    tmp_map[c[0]][c[1]]=1
    bfs(tmp_map,tmp_virus)
    # print(tmp_map)

    cnt=0
    for i in range(N):
        for j in range(M):
            if tmp_map[i][j]==0:
                cnt+=1
    answer=max(answer,cnt)

print(answer)
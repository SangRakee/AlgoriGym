# 시뮬레이션
# 삼성 SW 역량테스트 기출
# 1.해당 인덱스 찾기(BFS) 2.배열 90도 회전, 3.배열 인덱스값 밑으로 내리기(중력)
# 1.해당 인덱스 찾기(BFS) 경우 조건 맞추는데 고생함
# 3.반대인 밑에서 부터 확인해서 구현하는 방식

import sys
from collections import deque

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def rotate90(arr):
    rotate_arr=[[0]*N for i in range(N)]

    for i in range(N):
        for j in range(N):
            rotate_arr[i][j]=arr[j][N-1-i]

    arr=[i[:] for i in rotate_arr]

    return arr


def gravity(arr):

    for i in range(N - 2, -1, -1):  # 밑에서 부터 체크
        for j in range(N):
            if arr[i][j] >= 0:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0 <= r + 1 < N and arr[r + 1][j] == -9:  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        arr[r + 1][j] = arr[r][j]
                        arr[r][j] = -9
                        r += 1
                    else:
                        break

    return arr

def bfs(x,y,color):
    rainbow=0
    rainbow_list=[]
    group=[]
    queue=deque([[x,y]])
    visited[x][y]=1

    # 큐에서 꺼내옴
    while queue:
        x,y=queue.popleft()

        # 같은 색이거나 무지개 색일때
        if arr[x][y]==color:
            group.append([x,y])
        if arr[x][y]==0:
            rainbow_list.append([x,y])
            rainbow+=1

        # 갈수 있는 곳 순회
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            # 갈 수 있는가
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny]==0:
                    if arr[nx][ny]==color or arr[nx][ny]==0:
                        queue.append([nx,ny])   # 큐에 넣기
                        visited[nx][ny]=1       # 체크인인
    group.sort()
    group.extend(rainbow_list)
    return group,rainbow


N,M=map(int,sys.stdin.readline().split())

arr=[]
for i in range(N):
    x=list(map(int,sys.stdin.readline().split()))
    arr.append(x)


result=0

while True:
    # 1.가장큰 블록 찾기
    max_group_list=[]
    for i in range(N):
        for j in range(N):
            if arr[i][j]>0:
                visited=[[0]*N for i in range(N)]
                group,rainbow=bfs(i,j,arr[i][j])
                # if len(max_group)<len(group):
                if not max_group_list:
                    max_group_list=[len(group),rainbow,group]
                else:
                    if max_group_list[0]<len(group):
                        max_group_list=[len(group),rainbow,group]
                    elif max_group_list[0]==len(group) and max_group_list[1]<rainbow:
                        max_group_list = [len(group), rainbow, group]
                    elif max_group_list[0]==len(group) and max_group_list[1]==rainbow and max_group_list[2][0]<group[0]:
                        max_group_list = [len(group), rainbow, group]


    # print(max_group_list[2][0])
    # max_group_list.sort(reverse=True)
    if not max_group_list:
        break

    max_group=max_group_list[2]
    # print(max_group_list[0])
    # print()
    # for i in arr:
    #     print(*i)
    # print(max_group)
    if len(max_group)<2:
        # print(max_group)
        break

    # 2.블록 그룹 제거 - 제거된 칸(-9)로 표시
    score=(len(max_group))**2
    result+=score
    for i,j in max_group:
        arr[i][j]=-9

    # 3.중력
    arr=gravity(arr)
    # print(arr)


    # 4.반시계반향 회전
    arr=rotate90(arr)
    # print(arr)

    # 5.중력
    arr=gravity(arr)
    # print(arr)
    # print(result)

print(result)





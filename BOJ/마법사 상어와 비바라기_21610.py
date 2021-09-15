# 구현 문제
# 배열에서 벗어날 시 반대편으로 추가하는 구현을 못해서 오래걸림

import sys

dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]

#대각선
cx=[1,1,-1,-1]
cy=[-1,1,-1,1]

N,M=map(int,sys.stdin.readline().split())

space=[]
for _ in range(N):
    x=list(map(int,sys.stdin.readline().split()))
    space.append(x)

direct=[]
for _ in range(M):
    d,s=map(int,sys.stdin.readline().split())
    direct.append([d,s])

cloud=[[N-2,0],[N-2,1],[N-1,0],[N-1,1]]
# print(cloud)
for d,s in direct:
    # 1. 구름 이동
    for i in range(len(cloud)):
        x,y=cloud[i]
        x=(x+dx[d-1]*s)%N
        y=(y+dy[d-1]*s)%N

        cloud[i]=x,y

    # 구름의 위치를 확인해주기 위한 N*N 행렬
    is_cloud = [[False] * N for _ in range(N)]

    # 2. 구름에 있는 위치 1씩 증가
    for i,j in cloud:
        space[i][j]+=1
        is_cloud[i][j]=True

    # 3. 이동된 구름에서 대각선 파악
    for x,y in cloud:
        cnt=0
        for k in range(4):
            nx=x+cx[k]
            ny=y+cy[k]
            if 0<=nx<N and 0<=ny<N:
                if space[nx][ny]>=1:
                    cnt+=1
        space[x][y]+=cnt

    # 4. 새로운 구름 생성
    new_cloud=[]
    for i in range(N):
        for j in range(N):
            if space[i][j]>=2:
                if not is_cloud[i][j]:
                    new_cloud.append([i, j])
                    space[i][j] -= 2

    cloud=new_cloud[:]

    # print(cloud)
    # print(space)

# 5.총 강수량 계산
answer=0
for i in range(N):
    for j in range(N):
        answer+=space[i][j]

print(answer)
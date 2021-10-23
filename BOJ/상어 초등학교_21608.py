# 시뮬레이션
# 삼성 SW 역량테스트 기출

import heapq

def check(x,y,like):
    global adjacent
    cnt_like=0
    cnt_blank=0

    # 인접한 칸에 좋아하는 학생 수 및 비어있는 칸 파악
    # 상하좌우 판단
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]

        # 갈수 있는 곳인지
        if 0<=nx<N and 0<=ny<N:
            # 좋아하는 학생인 경우
            if arr[nx][ny] in like:
                cnt_like+=1

            # 빈칸인 경우
            elif arr[nx][ny]==0:
                cnt_blank+=1

    # 좋아하는 학생수를 키로 하는 딕셔너리에 좌표 벨류 추가
    if cnt_like in adjacent:
        adjacent[cnt_like].append([cnt_blank, x, y])
    else:
        adjacent[cnt_like] = [[cnt_blank, x, y]]


    return


# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 입력
N=int(input())
arr=[[0]*N for i in range(N)] # 자리를 나타낼 리스트

dic={}
for i in range(N*N):
    a,b,c,d,e=map(int,input().split())
    dic[a]=[b,c,d,e]

# print(dic)

# 순서대로 하나씩 실행
for key in dic.keys():
    nun=key
    like=dic[key]

    adjacent={}
    # 모든 좌표마다 판단
    for i in range(N):
        for j in range(N):
            # 해당 좌표 빈 자리일때
            if arr[i][j] == 0:
            # 인접한 칸에 좋아하는 학생 수 및 비어있는 칸 파악
            # 좋아하는 학생수를 키로 하는 딕셔너리에 좌표 벨류 추가
                check(i,j,like)

    candidate=[]
    # 반복문으로 딕셔너리의 key값을 4~0까지 찾기
    for i in range(4,-1,-1):
        # 좋아하는 학생수가 있을 경우
        if i in adjacent:

            for cnt_blank,x,y in adjacent[i]:
                # [비어 있는 칸,좌표]순으로 리스트에 추가(우선순위 큐)
                heapq.heappush(candidate,[-cnt_blank,x,y])
            break

    # 우선 순위큐에서 하나 추출해서 추가
    cnt_blank,x,y=heapq.heappop(candidate)
    arr[x][y]=key


# print(arr)

# 학생들의 만족도 조사

answer=0
for x in range(N):
    for y in range(N):
        like=dic[arr[x][y]]

        cnt_sit_like=0
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny] in like:
                    cnt_sit_like+=1

        if cnt_sit_like==4:
            answer+=1000
        elif cnt_sit_like==3:
            answer+=100
        elif cnt_sit_like==2:
            answer+=10
        elif cnt_sit_like==1:
            answer+=1


print(answer)
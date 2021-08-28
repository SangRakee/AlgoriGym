# 시뮬레이션
# 주사위 이동시 각 면의 방향 및 지도의 좌표를 생각해야하는 문제

import sys
from _collections import deque

#동서북남
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def move(a,):
    global x,y

    section=deque([])

    # 동
    if a==1:
        # 좌표이동
        nx=x+dx[0]
        ny=y+dy[0]
        # 다음 좌표가 지도 바깥으로 안 벗어날때
        if 0<=nx<N and 0<=ny<M:

            # 주사위 값 변경
            section.append(dice[3][1])
            for k in range(3):
                section.append(dice[1][k])

            temp = section.popleft()
            section.append(temp)

            dice[3][1] = section.popleft()
            for k in range(3):
                dice[1][k] = section.popleft()


            # 1.이동할려는 좌표 정수가 0일때
            if arr1[nx][ny]==0:
                # 1-1.주사위 바닥의 숫자를 바닥에 복사
                arr1[nx][ny]=dice[1][1]
            # 2.정수0이 아닐때
            else:
                # 2-1.주사위 바닥에 정수를 복사
                dice[1][1]=arr1[nx][ny]
                arr1[nx][ny]=0
            x, y = nx, ny
        # 바깥으로 벗어날때
        else:
            # print("벗어남")
            return

    # 서
    elif a==2:
        # 좌표이동
        nx=x+dx[1]
        ny=y+dy[1]
        # 다음 좌표가 지도 바깥으로 안 벗어날때
        if 0<=nx<N and 0<=ny<M:

            # 주사위 값 변경
            section.append(dice[3][1])
            for k in range(3):
                section.append(dice[1][k])
            dice[3][1] = section.pop()
            for k in range(3):
                dice[1][k] = section.popleft()


            # 1.이동할려는 좌표 정수가 0일때
            if arr1[nx][ny]==0:
                # 1-1.주사위 바닥의 숫자를 바닥에 복사
                arr1[nx][ny]=dice[1][1]
            # 2.정수0이 아닐때
            else:
                # 2-1.주사위 바닥에 정수를 복사
                dice[1][1]=arr1[nx][ny]
                arr1[nx][ny]=0
            x, y = nx, ny
        # 바깥으로 벗어날때
        else:
            # print("벗어남")
            return

    # 남
    elif a==4:
        # 좌표이동
        nx=x+dx[3]
        ny=y+dy[3]
        # 다음 좌표가 지도 바깥으로 안 벗어날때
        if 0<=nx<N and 0<=ny<M:

            # 주사위 값 변경
            for k in range(4):
                section.append(dice[k][1])
            temp = section.popleft()
            section.append(temp)

            for k in range(4):
                dice[k][1] = section.popleft()
            # print(dice)


            # 1.이동할려는 좌표 정수가 0일때
            if arr1[nx][ny]==0:
                # 1-1.주사위 바닥의 숫자를 바닥에 복사
                arr1[nx][ny]=dice[1][1]
            # 2.정수0이 아닐때
            else:
                # 2-1.주사위 바닥에 정수를 복사
                dice[1][1]=arr1[nx][ny]
                arr1[nx][ny]=0
            x, y = nx, ny
        # 바깥으로 벗어날때
        else:
            # print("벗어남")
            return
    # 북
    elif a==3:
        # 좌표이동
        nx=x+dx[2]
        ny=y+dy[2]
        # 다음 좌표가 지도 바깥으로 안 벗어날때
        if 0<=nx<N and 0<=ny<M:

            # 주사위 값 변경
            for k in range(4):
                section.append(dice[k][1])
            temp = section.pop()
            section.appendleft(temp)

            for k in range(4):
                dice[k][1] = section.popleft()
            # print(dice)



            # 1.이동할려는 좌표 정수가 0일때
            if arr1[nx][ny]==0:
                # 1-1.주사위 바닥의 숫자를 바닥에 복사
                arr1[nx][ny]=dice[1][1]
            # 2.정수0이 아닐때
            else:
                # 2-1.주사위 바닥에 정수를 복사
                dice[1][1]=arr1[nx][ny]
                arr1[nx][ny]=0
            x,y=nx,ny
        # 바깥으로 벗어날때
        else:
            # print("벗어남")
            return

    return print(dice[3][1])

N,M,x,y,K=map(int,sys.stdin.readline().split())
arr1=[]
for _ in range(N):
    a=list(map(int,sys.stdin.readline().split()))
    arr1.append(a)
orders=list(map(int,sys.stdin.readline().split()))

dice=[[0]*3 for i in range(4)]
# dice=[[0,2,0],[4,1,3],[0,5,0],[0,6,0]]
# print(arr1)

#처음 설정

for order in orders:
    move(order)
    # print(order,dice)

# print(dice)
# 구현 문제
# 선생님의 시점으로 상하좌우로 이동하여 학생을 안만날시 True로 판단하는 알고리즘

import sys
from itertools import combinations
from collections import deque

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def check(teacher,arr2):

    while teacher:
        x,y=teacher.popleft()

        # 추출된 좌표를 상하좌우로 이동
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            # 이동시 arr 범위에 벗아나지 않게
            while 0<=nx<len(arr2) and 0<=ny<len(arr2[0]):
                # 학생들 만날 시
                if arr2[nx][ny]=="S":
                    return False
                elif arr2[nx][ny]=="O":
                    break
                else:
                    nx+=dx[k]
                    ny+=dy[k]

    return True



N=int(sys.stdin.readline())
arr1=[]
black=[]

#입력
for i in range(N):
    x=list(sys.stdin.readline().split())
    arr1.append(x)
    # 빈공간 좌표 파악
    for j in range(N):
        if x[j]=="X":
            black.append([i, j])


# 조합 추출
obstacle=combinations(black,3)

# 조합된 경우의 수 판단
for ob in obstacle:

    teacher = deque([])
    for i in range(N):
        for j in range(N):
            if arr1[i][j] == "T":
                teacher.append([i, j])

    # 장애물을 추가한 arr 생성
    arr2=[i[:] for i in arr1]
    # 장애물 추가
    for i in range(3):
        arr2[ob[i][0]][ob[i][1]]="O"

    if check(teacher,arr2)==False:
        continue
    else:
        print("YES")
        exit(0)


print("NO")
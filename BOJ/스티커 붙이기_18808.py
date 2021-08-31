# 시뮬레이션 문제
# 도형돌리기, 공간 확인하기등 여러 구현 능력을 기를 수 있는 문제

import sys

def rotate90(sticker,row,col):
    change=[[0]*row for i in range(col)]
    for i in range(row):
        for j in range(col):
            change[j][row-1-i]=sticker[i][j]
    return change


def check(sticker,i,j):
    R,C=len(sticker),len(sticker[0]) # 3,3
    # print(sticker, i,j)
    for row in range(R):
        for col in range(C):
            if sticker[row][col]==1:
                if laptop[i+row][j+col]==1:
                    return False
    return True

def attach(sticker,i,j):
    R,C=len(sticker),len(sticker[0])  # 3,3
    for row in range(i,i+R):
        for col in range(j,j+C):
            if sticker[row-i][col-j] == 1:
                laptop[row][col]=1
    # print(laptop)
    return laptop

N,M,K=map(int,sys.stdin.readline().split())
laptop=[[0]*M for i in range(N)]

stickers=[]
for i in range(K):
    R,C=map(int,sys.stdin.readline().split())
    s=[]
    for j in range(R):
        x=list(map(int,sys.stdin.readline().split()))
        s.append(x)
    stickers.append(s)

# print(stickers)

for sticker in stickers:
    R,C=len(sticker),len(sticker[0])
    # print(R,C)

    # 90도씩 360도 회전
    for k in range(4):
        # 1.가로,세로 길이가 맞는지
        if R>N or C>M:
            # 1-1. 아닐시 90도 회전
            sticker=rotate90(sticker,R,C)
            tmp=R
            R=C
            C=tmp

        flag=False
        # 2.붙일 수 있는지 확인
        for i in range(N+1-R):
            for j in range(M+1-C):
                if check(sticker,i,j)==True:
                    flag=True
                    # 2-1. 붙임
                    attach(sticker,i,j)
                    break
            if flag==True:
                break

        # 3 붙일 수 없을시
        if flag==False:
            # 3-1. 아닐시 90도 회전
            sticker=rotate90(sticker,R,C)
            tmp=R
            R=C
            C=tmp
        else:
            break

# 출력
answer=0
for i in range(N):
    for j in range(M):
        if laptop[i][j]==1:
            answer+=1

print(answer)
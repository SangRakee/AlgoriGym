# 구현 문제
# 2차원 리스트 값을 반시계 반향으로 옮기는 문제

import sys

#우하좌상
dx=[0,1,0,-1]
dy=[1,0,-1,0]

N,M,R=map(int,sys.stdin.readline().split())

matrix=[]

for i in range(N):
    x=list(map(int,input().split()))
    matrix.append(x)


for _ in range(R):
    for i in range(min(N, M) // 2):
        x, y = i, i
        firstVal = matrix[x][y]
        for k in range(4):
            while True:  # i<=nx<N-i and i<=ny<M-i
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < i or nx >= N - i or ny >= M - i or ny < i:
                    break
                else:
                    matrix[x][y] = matrix[nx][ny]
                    x, y = nx, ny
        matrix[x + 1][y] = firstVal


for i in range(N):
    print(*matrix[i])


# for _ in range(R):
#     for i in range(M//2):
#         x, y = i, i
#         firstVal = matrix[x][y]
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             while i<=nx<N-i and i<=ny<M-i:
#                 matrix[x][y] = matrix[nx][ny]
#                 x, y = nx, ny
#                 nx = x + dx[k]
#                 ny = y + dy[k]
#         matrix[x + 1][y] = firstVal
#
# for i in range(N):
#     print(*matrix[i])

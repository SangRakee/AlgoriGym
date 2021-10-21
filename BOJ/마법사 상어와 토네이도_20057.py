# 시뮬레이션
# 삼성 SW 역량테스트 기출
# 1.달팽이 모양으로 좌표 이동 -> 딕셔너리를 만들어서 해당 좌표를 저장해두면 나중에 사용할때 편리함
# 2.해당 좌표에서 각 거리만큼의 index를 계산 -> 이런 좌표 문제 같은 경우 (반)시계 방향마다 다를 수 있으니까 유의할 것

def magic(nx, ny, x, y, k):
    global answer

    # 2. 방향별 모래 비율 위치
    left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
            (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
    right = [(x, -y, z) for x, y, z in left]
    down = [(-y, x, z) for x, y, z in left]
    up = [(y, x, z) for x, y, z in left]

    nx = x + dx[k]
    ny = y + dy[k]

    if not (0 <= nx < n and 0 <= ny < n and board[nx][ny]):
        return

    sand = board[nx][ny]
    a_x = nx + dx[k]
    a_y = ny + dy[k]

    alpha = board[nx][ny]

    if k == 0:
        for m in range(len(left)):
            mx = nx + left[m][0]
            my = ny + left[m][1]
            mr = left[m][2]

            receive = int(sand * mr)
            if 0 <= mx < n and 0 <= my < n:
                board[mx][my] += receive

            else:
                answer += receive
            alpha -= receive
    elif k == 1:
        for m in range(len(down)):
            mx = nx + down[m][0]
            my = ny + down[m][1]
            mr = down[m][2]

            receive = int(sand * mr)
            if 0 <= mx < n and 0 <= my < n:
                board[mx][my] += receive

            else:
                answer += receive
            alpha -= receive
    elif k == 2:
        for m in range(len(right)):
            mx = nx + right[m][0]
            my = ny + right[m][1]
            mr = right[m][2]

            receive = int(sand * mr)
            if 0 <= mx < n and 0 <= my < n:
                board[mx][my] += receive

            else:
                answer += receive
            alpha -= receive
    elif k == 3:
        for m in range(len(up)):
            mx = nx + up[m][0]
            my = ny + up[m][1]
            mr = up[m][2]

            receive = int(sand * mr)
            if 0 <= mx < n and 0 <= my < n:
                board[mx][my] += receive

            else:
                answer += receive
            alpha -= receive

    if 0 <= a_x < n and 0 <= a_y < n:
        board[a_x][a_y] += alpha
    else:
        answer += alpha
    board[nx][ny] = 0


# 좌하우상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
move = [(0, -1), (1, 0), (0, 1), (-1, 0)]

n = int(input())

x = n // 2
y = n // 2

board = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

cnt = 1
k = 0
flag = True
# 달팽이 모양으로 이동
dic = {}
num = 1
answer = 0
while flag == True:

    for i in range(2):
        for j in range(cnt):
            nx = x + dx[k]
            ny = y + dy[k]

            # 이동마다 흩날리는 모래 계산
            magic(nx, ny, x, y, k)
            x = nx
            y = ny
            # print(x, y)
            dic[num] = [x, y, k]
            num += 1
            if x == 0 and y == 0:
                flag = False
                break
        if flag == False:
            break
        k = (k + 1) % 4
    cnt += 1

print(answer)
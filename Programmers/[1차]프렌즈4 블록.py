# 구현 문제
# 정사각형 감지는 디피로 구현

from collections import deque

dx = [0, -1, 0, -1]
dy = [0, 0, -1, -1]


def gravity(board, m, n):
    for i in range(m - 2, -1, -1):
        for j in range(n):
            if board[i][j] != "X":
                r = i
                while True:
                    if 0 <= r + 1 < m and board[r + 1][j] == "X":
                        board[r + 1][j] = board[r][j]
                        board[r][j] = "X"
                        r += 1
                    else:
                        break

    return board


def check(board, dp, n, m):
    for i in range(1, m):
        for j in range(1, n):
            if board[i][j] == board[i - 1][j] == board[i][j - 1] == board[i - 1][j - 1] and board[i][j] != "X":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            else:
                dp[i][j] = 1

    return dp


def solution(m, n, board):
    answer = 0

    for i in range(m):
        board[i] = list(board[i])

    while True:

        dp = [[0] * n for i in range(m)]

        for i in range(n):
            dp[0][i] = 1

        for i in range(m):
            dp[i][0] = 1

        # 블록체크
        check(board, dp, n, m)
        # print(dp)

        # 블록 삭제
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if dp[i][j] >= 2:
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if [nx, ny] not in queue:
                            queue.append([nx, ny])
                            answer += 1

        # 삭제할 블록이 없으면 종료
        if not queue:
            return answer

        while queue:
            x, y = queue.popleft()
            # print(board[x][y])
            board[x][y] = "X"
        # print(board)

        # 블록 당기기
        gravity(board, m, n)

        # print(board)

    return answer
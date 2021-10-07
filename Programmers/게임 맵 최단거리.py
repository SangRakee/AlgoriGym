# bfs

from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(r, c, maps):
    queue = deque([])
    queue.append([r, c])
    visited = [[0] * len(maps[0]) for i in range(len(maps))]
    visited[r][c] = 1

    # 큐에서 꺼내옴
    while queue:
        x, y = queue.popleft()

        # 목적지 인가
        if x == (len(maps)-1) and y == (len(maps[0])-1):
            return visited[len(maps)-1][len(maps[0])-1]

        # 갈 수 있는곳 순회
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 갈 수 있는가
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny]==1:
                    if visited[nx][ny] == 0:
                        queue.append([nx, ny])  # 큐에 넣기
                        visited[nx][ny] =  visited[x][y]+1  # 체크인

    return -1


def solution(maps):
    answer = 0

    answer=bfs(0, 0, maps)

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
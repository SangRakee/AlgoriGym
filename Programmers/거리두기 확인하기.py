# 구현문제

# 테스트 케이스 places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

from collections import deque
from itertools import combinations

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(departure, arrival, place, visited):
    r = departure[0]
    c = departure[1]
    queue = deque([[r, c]])
    visited[r][c] = 0

    # 큐에서 추출
    while queue:
        x, y = queue.popleft()
        # print(x, y, arrival)

        # 목적지 인가
        if x == arrival[0] and y == arrival[1]:
            distance = visited[x][y]
            # print(distance)
            return distance

        # 갈 수 있는 곳 순회
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 갈 수 있는가
            if 0 <= nx < 5 and 0 <= ny < 5:
                if place[nx][ny] != 'X':
                    if visited[nx][ny] == -1:
                        queue.append([nx, ny])  # 큐에 추가
                        visited[nx][ny] = visited[x][y]+1  # 체크인

    return 3


def solution(places):
    answer = []

    for place in places:
        # 1.응시자 위치 저장
        people = []
        flag=False
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    people.append([i, j])

        # 2.응시자가 1명 이하인 경우
        if len(people) < 2:
            answer.append(1)
            continue

        # 3.응시자가 두명이상인 경우
        elif len(people) >= 2:

            # 4.응시자별로 조합 리스트 생성
            comb = list(combinations(people, 2))
            # print(comb)
            # 5.조합 리스트 거리 계산
            for a, b in comb:
                # a01 b01
                distance = (abs(a[0] - b[0]) + abs(a[1] - b[1]))
                # print(a,b,distance)

                if distance > 3:
                    continue

                # 6.2이하인 것은 bfs로 거리 계산
                elif distance <= 2:
                    visited = [[-1] * 5 for i in range(5)]
                    # print("시작점", a, b)
                    distance = bfs(a, b, place, visited)

                    # 7.거리두기 실패시
                    if distance <= 2:
                        answer.append(0)
                        flag=True
                        break
            if flag==True:
                continue

        answer.append(1)

    return answer

print(solution(places))
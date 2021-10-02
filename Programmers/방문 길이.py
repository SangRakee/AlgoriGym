# 구현문제
# 좌표 이동

from collections import deque

def solution(dirs):
    answer = 0
    direction = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}

    x, y = 5, 5

    q = deque([])

    for d in dirs:
        nx = x + direction[d][0]
        ny = y + direction[d][1]

        a = [[x,y,nx,ny]]
        b = [[nx,ny,x,y]]

        if 0 <= nx <= 10 and 0 <= ny <= 10:
            if (a not in q):
                q.append(a)
                q.append(b)
                answer += 1
            x, y = nx, ny

    return answer

print(solution("ULURRDLLU"))
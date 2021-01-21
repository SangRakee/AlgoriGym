n=3
computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0]*n

    while 0 in visited:
        quere=deque([visited.index(0)])
        while quere:
            node = quere.popleft()
            visited[node] = 1
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    quere.append(i)
        answer += 1
    return answer

print(solution(n,computers))
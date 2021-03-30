n=3
computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]

def dfs(computers, visited, v):
    visited[v] = 1
    for i in range(1, len(computers[v])+1):
        if visited[i]==0 and computers[v][i-1]==1:
            dfs(computers, visited,i)


def solution(n, computers):
    answer = 0
    computers.insert(0,0)
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1

    return answer

print(solution(n,computers))
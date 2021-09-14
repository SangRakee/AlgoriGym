# 최단경로 문제
# 노드가 300이하여서 플로이드 워셜로 풀 수 있는 문제

# 테스트 케이스
# n=6
# s=4
# a=6
# b=2
# fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

INF = int(1e9)

def solution(n, s, a, b, fares):
    answer = INF

    graph = [[INF] * (n + 1) for i in range(n + 1)]

    for f in fares:
        graph[f[0]][f[1]] = f[2]
        graph[f[1]][f[0]] = f[2]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

    return answer
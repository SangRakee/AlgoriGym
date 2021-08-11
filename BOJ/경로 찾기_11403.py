# 경로 확인 문제
# 플로이드-워셜 알고리즘
# 저 같은 경우 플로이드-워셜 알고리즘을 통해 모든 경로의 최소 경우의 수를 구했는데,
# 문제에서는 경우의 수를 구하는 것이 아닌 경로가 존재여부만 확인하는거다 보니 비효율적인 코드

import sys

N=int(sys.stdin.readline())

graph=[]
for _ in range(N):
    x=list(map(int,sys.stdin.readline().split()))
    for a,b in enumerate(x):
        if b == 0:
            x[a]=int(1e9)
    graph.append(x)

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(N):
    for j in range(N):
        if graph[i][j]==int(1e9):
            graph[i][j]=0
        else:
            graph[i][j]=1

for i in range(N):
    print(*graph[i])

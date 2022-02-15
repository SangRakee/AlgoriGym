# 플로이드-워셜
# 기본 문제

import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

graph=[[int(1e9)]*(n+1) for i in range(n+1)]

# 초기 비용 세팅
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    if graph[a][b]>c: # 노선이 여러개 일 수 있어서 그 중 최소인 것을 기록
        graph[a][b]=c

# 플로이드-워셜 점화식
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == int(1e9):
            graph[i][j]=0



for i in range(1,n+1):
    print(*graph[i][1:])
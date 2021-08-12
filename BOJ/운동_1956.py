# 플로이드 워셜 문제
# 갔다 오는 경우의 수에서 최단 구하기
# i -> i 최단 구하기 : i -> ... -> i를 구해서 가장 작은 값 뽑는 형태로 구함
# 다른 사람 풀이는 처음에 자기 자신 경로를 0으로 초기화 하지 않고 마지막에 (i,i)인 값을 구함

import sys
INF=int(1e9)

V,E=map(int,sys.stdin.readline().split())

graph=[[INF]*(V+1) for i in range(V+1)]
for _ in range(E):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a][b]=c

for i in range(1,V+1):
    for j in range(1,V+1):
        if i==j:
            graph[i][j]=0

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])


for i in range(1,V+1):
    print(*graph[i][1:])

answer=INF
for i in range(1,V+1):
    for j in range(1,V+1):
        if i!=j:
            if graph[i][j]!=INF and graph[j][i]!=INF:
                answer=min(answer,graph[i][j]+graph[j][i])


if answer != INF:
    print(answer)
else:
    print(-1)


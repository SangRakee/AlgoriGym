# 플로이드-워셜 문제
# 비교했을 모든 경우의 수에서 비교 할 수 없는 노드의 수 구하기
# i->j, j->i로 갈 수 없는 경우 찾기

import sys
INF=int(1e9)

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

graph=[[INF]*(N+1) for i in range(N+1)]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a][b]=1

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            graph[i][j]=0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][j]==1 or (graph[i][k]==1 and graph[k][j]==1):
                graph[i][j]=1

for i in range(1,N+1):
    cnt=0
    for j in range(1,N+1):
        if graph[i][j]==1 or graph[j][i]==1:
            cnt+=1
    print(N-1-cnt) #자기 자신 제외
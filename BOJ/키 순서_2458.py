# 플로이드-워셜
# 처음에 위상 정렬로 인지하였음
# 플로이드-워셜인 힌트 : 상대적인 순위가 아닌 전체적인 순위를 알아야하기 때문, 인풋값이 매우 작음
# 비용 계산한 것에 상대와 내가 1e9가 없으면 비교가 가능한 것이기 때문에 전체 순위를 알 수 있음

import sys

N,M=map(int,sys.stdin.readline().split())

graph=[[int(1e9)]*(N+1) for i in range(N+1)]

for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a][b]=1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

# 전체 순위를 알 수 있는지 판단
answer=0
for i in range(1,N+1):
    cnt=0
    for j in range(1,N+1):
        if graph[i][j]!=int(1e9) or graph[j][i]!=int(1e9):
            cnt+=1
    if cnt==N-1:
        answer+=1

print(answer)
# 플로이드-워셜
# 기본적인 최단 거리가 아닌 모든 경로를 방문했을때 최단 거리여서, 백트래킹으로 모든 경우의 수를 구해줘야하는 방식

import sys
sys.setrecursionlimit(10**6)

#백트래킹
def dfs(start,cnt,cost):
    # 체크인
    visited[start]=1
    # print(cnt)
    # 목적지인가
    if cnt==N:
        # print(cost)
        result.append(cost)
        return
    # 갈 수 있는 곳 순회
    for i in range(len(distance[start])):
        # 갈 수 있는 가
        if visited[i]==0:
            #간다
            dfs(i,cnt+1,cost+distance[start][i])
            # 체크아웃
            visited[i]=0

N,K=map(int,sys.stdin.readline().split())
distance=[]
for _ in range(N):
    x=list(map(int,sys.stdin.readline().split()))
    distance.append(x)

# 플로이드-워셜 점화식
for k in range(N):
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

result=[]
visited=[0]*N
dfs(K,1,0)
print(min(result))



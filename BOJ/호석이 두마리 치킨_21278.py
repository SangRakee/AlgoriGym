# 플로이드-워셜

import sys
import heapq
from itertools import combinations
INF=int(1e9)


N,M=map(int,sys.stdin.readline().split())
distance=[[INF]*(N+1) for i in range(N+1)]
building=[i for i in range(1,N+1)]

for _ in range(M):
    A,B=map(int,sys.stdin.readline().split())
    distance[A][B]=1
    distance[B][A]=1

for i in range(1,N+1):
    distance[i][i]=0


for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

arr=list(combinations(building,2))

answer=[]
q=[]
for i in arr:
    a,b=i
    result=0
    for j in range(1,len(distance)):
        result+=min(distance[j][a],distance[j][b])
    heapq.heappush(q,(result,a,b))

cost,a,b=heapq.heappop(q)
print(a,b,2*cost)
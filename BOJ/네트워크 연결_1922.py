# 최소 신장 트리(MST)
# 크루스칼 알고리즘(기본적으로 서로소 집합 알고리즘을 알고 있어야 함)

import sys
import heapq

# 파인드 함수
def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]

# 유니온 함수
def union(a,b):
    pa=find(a)
    pb=find(b)
    parent[pb]=pa
    # if pa < pb:
    #     parent[pb] = pa
    # else:
    #     parent[pa] = pb

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

edges=[]
parent=[0]
result=0

for _ in range(M):
    a,b,c=map(int,sys.stdin.readline().split())
    heapq.heappush(edges,(c,a,b))

for i in range(1,N+1):
    parent.append(i)

# print(edges)
while edges:
    # 1.최소 비용의 간선 추출
    cost,a,b=heapq.heappop(edges)
    # 2.두 정점이 이미 연결O
    if find(a)==find(b):
        continue
    # 2-1. 연결X
    else:
        result+=cost
        union(a, b)
    # print(cost,a,b)

print(result)
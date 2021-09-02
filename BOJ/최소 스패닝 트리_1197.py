# 최소 스패닝 트리
# 단순 크루스칼 알고리즘 문제

import sys
import heapq

def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]

def union(a,b):
    pa=find(a)
    pb=find(b)
    parent[pb]=pa


V,E=map(int,sys.stdin.readline().split())

edges=[]
for _ in range(E):
    A,B,C=map(int,sys.stdin.readline().split())
    heapq.heappush(edges,(C,A,B))

parent=[]
for i in range(V+1):
    parent.append(i)

answer=0
while edges:
    cost,a,b=heapq.heappop(edges)

    if find(a)==find(b):
        continue
    else:
        union(a,b)
        answer+=cost

print(answer)
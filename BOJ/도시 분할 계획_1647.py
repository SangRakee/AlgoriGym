# 최소 신장 트리(MST)
# 기본적인 MST 문제 + 조금 생각
# 최종적으로 두개의 마을로 분할해야하기 때문에 최종 MST 구축하기전(가장 비용이 많이드는 간선 제외)까지 구현 문제

import sys
import heapq

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    pa=find(a)
    pb=find(b)
    parent[pb]=pa


N,M=map(int,sys.stdin.readline().split())

parent=[0]
edges=[]
result=0

for _ in range(M):
    a,b,c=map(int,sys.stdin.readline().split())
    heapq.heappush(edges,(c,a,b))

for i in range(1,N+1):
    parent.append(i)

# 1.비용이 작은 순으로 추출
while edges:
    cost,a,b=heapq.heappop(edges)
    # 2.연결된 노드인지 판단
    if find(a)==find(b):
        continue
    else:# 2-1. 비연결 노드일시
        union(a,b)
        result+=cost
        last=cost
    # print(cost,a,b)


print(result-last)

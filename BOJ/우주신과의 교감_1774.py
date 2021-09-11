# MST 문제
# 기본적인 크루스칼 알고리즘 + 소수 둘째자리 까지 표시하는 함수

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

N,M=map(int,sys.stdin.readline().split())

parent=[]
for i in range(N):
    parent.append(i)

edges=[]
for _ in range(N):
    x,y=map(int,sys.stdin.readline().split())
    edges.append((x,y))

for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    union(a-1,b-1)

heap=[]
graph=[[]for i in range(N)]
for i in range(N):
    for j in range(N):
        if i!=j:
            distance=(((abs(edges[i][0]-edges[j][0]))**2+(abs(edges[i][1]-edges[j][1]))**2)**(1/2))
            heapq.heappush(heap,(distance,i,j))

# print(heap)

answer=0
while heap:
    cost,a,b=heapq.heappop(heap)

    if find(a)==find(b):
        continue
    else:
        union(a,b)
        answer+=cost

print('%.2f'%answer)
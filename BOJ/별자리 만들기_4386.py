# 최소 스패닝 트리(MST) 문제
# 크루스칼 알고리즘 이용
# 노드의 x,y 좌표만 주어지는 문제
# 노드간의 비용을 직접 구해야함(두 좌표간의 거리 구하기 공식)

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

N=int(sys.stdin.readline())

parent=[0]
star=[]
result=0

for i in range(1,N+1):
    parent.append(i)

for i in range(N):
    x,y=map(float,sys.stdin.readline().split())
    star.append([x,y])

dict=[]
for i in range(N):
    for j in range(i+1,N):
        a=star[i]
        b=star[j]
        cost=round(((a[0]-b[0])**2+(a[1]-b[1])**2)**(0.5),2)
        heapq.heappush(dict,(cost,i+1,j+1))

while dict:
    cost,a,b=heapq.heappop(dict)

    if find(a)==find(b):
        continue
    else:
        result+=cost
        union(a,b)

print(result)
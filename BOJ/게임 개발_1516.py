# 위상정렬

import sys
from collections import deque

N=int(sys.stdin.readline())

answer = [0] * (N+1)
cost = [0] * (N+1)
graph=[[]for i in range(N+1)]
indegree=[0]*(N+1)

for i in range(1,N+1):
    x=list(map(int,sys.stdin.readline().split()))
    indegree[i]+=len(x[1:-1])
    cost[i]=x[0]
    if x[1]!=-1:
        for j in x[1:-1]:
            graph[j].append(i)

# print(indegree)
# print(cost)
# print(graph)


queue=deque([])
for i in range(1,N+1):
    if indegree[i]==0:
        queue.append(i)
        answer[i]=cost[i]
# print(answer)
while queue:
    node=queue.popleft()

    for v in graph[node]:
        indegree[v]-=1
        answer[v]=max(answer[v],answer[node]+cost[v])
        if indegree[v]==0:
            queue.append(v)


# print(answer)
for i in range(1, len(answer)):
    print(answer[i])

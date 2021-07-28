# 위상정렬(DAG) 문제
# 위상정렬의 기초적인 형식

import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

indegree=[0]*(N+1)
grahp=[[] for i in range(N+1)]


for _ in range(M):
    # 1.진입차수 넣기
    A,B=map(int,sys.stdin.readline().split())
    grahp[A].append(B)
    indegree[B]+=1

# 위상 정렬 함수
def topologySort():
    result=[]
    queue=deque([])

    # 2.초기 진입 차수 0인 노드 Queue 적재
    for n in range(1,len(indegree)):
        if indegree[n]==0:
            queue.append(n)

    # 3. Queue에서 뽑아서 연결된 간선 제거
    while queue:
        now=queue.popleft()
        result.append(now)
        # 3-1. Queue에서 뽑은 node와 연결된 노드들의 진입차수 1빼기
        for i in grahp[now]:
            indegree[i]-=1
            if indegree[i]==0:
                queue.append(i)
    for i in result:
        print(i,end=" ")

topologySort()

# 위상정렬 문제
# 기본적인 커리큘럼이 있는 위상 정렬과 다르게 가능한 오름차순 문제순으로 풀어야 한다
# 첫번째 방법 : queue에 들어오는 문제들을 매번 정렬하여 오름차순으로 만든다음에 첫번재 인덱스 값을 popleft하였는데, 시간초과 발생
# 매번 정렬하는 것이 시간초과가 발생하는 것이라 생각하여 우선순위 큐인 heap을 사용하여, 이 문제점을 해결하였음

import sys
import heapq

N,M=map(int,sys.stdin.readline().split())

result=[]

indegree=[0]*(N+1) #진입차수 리스트
grahp=[[] for i in range(N+1)] # 노드별 진출 노드 그래프

# indegree 및 grahp 설정
for i in range(M):
    A,B=map(int,sys.stdin.readline().split())
    grahp[A].append(B)
    indegree[B]+=1

#진입차수가 0인 노드 heap 에 추가
problem=[]
for i in range(1,N+1):
    if indegree[i]==0:
        heapq.heappush(problem,i)

while problem:

    # heap에서 꺼내옴
    now=heapq.heappop(problem)
    result.append(now)

    # 갈 수 있는 곳 순회
    for v in grahp[now]:
        # 갈 수 있는 곳 indegree-1
        indegree[v]-=1
        # 갈 수 있는가(indegree==0)
        if indegree[v]==0:
            # heap에 넣기
            heapq.heappush(problem,v)

print(*result)
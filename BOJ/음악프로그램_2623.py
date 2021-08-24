# 위상정렬
# 입력값 형태가 두개의 변수형태가 아니가 한번에 여러 단계를 입력받는 형식

import sys
from collections import deque

def topologysort():
    result=[]
    queue=deque([])

    # 전입 차수 0인거 큐에 추가
    for n in range(1,N+1):
        if indegree[n]==0:
            queue.append(n)
    # 큐에서 하나씩 뽑기
    while queue:
        now=queue.popleft()
        result.append(now)

        # 갈 수 있는 곳 순회
        for i in graph[now]:
            # 전입차수 -1
            indegree[i]-=1
            # 전입차수 0인거 다시 큐에 넣기
            if indegree[i]==0:
                queue.append(i)

    return result


N,M=map(int,sys.stdin.readline().split())
PD=[]
for _ in range(M):
    arr=list(map(int,sys.stdin.readline().split()))
    PD.append(arr[1:])

# 초기 차수 설정
indegree=[0]*(N+1)
graph=[[] for i in range(N+1)]
for i in range(M):
    for j in range(len(PD[i])-1):
        graph[PD[i][j]].append(PD[i][j+1])
        indegree[PD[i][j+1]]+=1

answer=topologysort()

# 출력
if len(answer)==N:
    for i in answer:
        print(i)
else:
    print(0)
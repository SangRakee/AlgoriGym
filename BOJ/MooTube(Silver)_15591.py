# bfs 문제
# 처음에 문제를 풀때, bfs 인지 모르고 3중 포문으로 구했다가 시간초과 발생

import sys
from _collections import deque

def bfs(k,v):
    answer=0
    # 큐에 해당 출발점의 연결지 넣기
    queue=deque([[v,k]])
    # 방문 체크
    visited=[0]*(N+1)
    visited[v]=1
    # 큐에서 하나씩 뽑기기
    while queue:
        node,cost=queue.popleft()
        # 갈 수 있는 곳 순회
        for i in cows[node]:
            # 갈 수 있는가
            if i[1]>=k and visited[i[0]]==0:
                # 큐에 넣기
                queue.append(i)
                answer+=1
            # 체크인
            visited[i[0]]=1
    print(answer)


N,Q=map(int,sys.stdin.readline().split())

cows={}
for _ in range(N-1):
    p,q,r=map(int,sys.stdin.readline().split())
    if p not in cows:
        cows[p]=[[q,r]]
    else:
        cows[p].append([q,r])
    if q not in cows:
        cows[q]=[[p,r]]
    else:
        cows[q].append([p,r])

question=[]
for _ in range(Q):
    k,v=map(int,sys.stdin.readline().split())
    question.append([k,v])
    bfs(k,v)



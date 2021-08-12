# 다익스트라 알고리즘
# 처음에는 경로까지 구하는 알고리즘을 했으나 비효율적 메모리가 비효율적이여서, 경로가 아닌 방법으로 구함

import sys
import heapq
INF=int(1e9)
t=int(sys.stdin.readline())

for _ in range(t):
    n,d,c=map(int,sys.stdin.readline().split())

    graph=[[]for i in range(n+1)]
    distance=[INF]*(n+1)

    for __ in range(d):
        a,b,s=map(int,sys.stdin.readline().split())
        graph[b].append((a,s))


    # 초기 출발지 설정
    distance[c]=0
    heap=[]
    heapq.heappush(heap,(0,c))

    # 우선순위 큐에서 추출
    while heap:
        cost,now=heapq.heappop(heap)

        # 방문한 곳인가
        if distance[now]<cost:
            continue

        # 다른 인접한 노드 순회
        for i in graph[now]:
            dist,next=i[1]+cost,i[0]
            # 순회 한 노드랑 비용 계산
            if distance[next]>dist:
                distance[next]=dist
                heapq.heappush(heap,(dist,next))


    cnt=0 # 몇 번 이동하는지
    val=0 # 마지막 경로의 cost를 담는 변수
    for i in range(1,n+1):
        if distance[i]!=INF:
            cnt+=1
            val=max(val,distance[i])
    print(distance)
    print(cnt,val)

# 다익스트라(최단경로)
# 기본적인 최단경로 문제

import sys
import heapq
INF=int(1e9)

def dijkstra(start):
    # 초기 출발지 설정
    distance[start]=0
    edge=[]
    heapq.heappush(edge,(0,start))

    # 우선순위 큐에서 추출
    while edge:
        cost,node=heapq.heappop(edge)

        # 방문한 적이 있는지 체크
        if cost>distance[node]:
            continue

        # 주변 노드 체크
        for i in graph[node]:
            dist,next=cost+i[1],i[0]

            # 주변 노드와 거리 체크
            if dist<distance[next]:
                heapq.heappush(edge,(dist,next))
                distance[next]=dist


V,E=map(int,sys.stdin.readline().split())
start=int(sys.stdin.readline())

graph=[[]for i in range(V+1)]
distance=[INF]*(V+1)
for _ in range(E):
    u,v,w=map(int,sys.stdin.readline().split())
    graph[u].append((v,w))

dijkstra(start)
for i in distance[1:]:
    if i==INF:
        print("INF")
    else:
        print(i)


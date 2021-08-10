# 최단경로 문제
# 다익스트라 알고르즘
# 갔다왔다의 최대 거리를 구하는 거여서 갔을때랑 왔을때 거리를 각각 구해서 더 하는 방식

import sys
import heapq

N,M,X=map(int,sys.stdin.readline().split())

graph=[[] for i in range(N+1)]
for _ in range(M):
    x,y,c=map(int,sys.stdin.readline().split())
    graph[x].append((y,c))

def dijkstra(start):
    # 초기 출발지 설정
    distance = [int(1e9)] * (N + 1)
    node=[]
    heapq.heappush(node,(0,start))
    distance[start]=0
    while node:
        # 우선순위 큐에서 꺼내옴
        dist,now=heapq.heappop(node)

        # 방문한 곳인지
        if distance[now]<dist:
            continue

        # 갈 수 있는 곳 순회
        for i in graph[now]:
            next,cost=i[0],i[1]+dist

            # 비용 계산
            if distance[next]>cost:
                distance[next]=cost
                heapq.heappush(node,(cost,next))
    return distance

# 올때 갈때 거리 계산
answer=0
for i in range(1,N+1):
    go=dijkstra(i)
    back=dijkstra(X)
    answer= max(answer, go[X] + back[i])

print(answer)

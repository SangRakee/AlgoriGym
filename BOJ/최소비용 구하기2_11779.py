# 최단경로 문제
# 다익스트라 알고리즘 사용
# 기본적인 다익스트라 알고리즘 뿐만 아니라 최단 비용의 경로까지 구해야 하는 문제

import sys
import heapq

def dijkstra(start):
    city=[]

    # 초기 출발지 설정
    distance=[int(1e9)]*(n+1)
    distance[start]=0
    node=[]
    heapq.heappush(node,(0,start))
    # 우선순위 큐에서 하나씩 추출
    while node:
        dist,now=heapq.heappop(node)

        # 방문한 곳인가
        if distance[now]<dist:
            continue
        path[now].append(now)  # 현재 노드에 연결된 노드 추가

        # 노드 순회
        for i in buses[now]:
            next,cost=i[0],i[1]+dist

            # 현재 노드를 거쳐 다른 노드로 이동시에 거리가 더 짧을때
            if distance[next]>cost:
                distance[next]=cost
                heapq.heappush(node,(cost,next))
                path[next]=path[now][:]   # 현재 경로에서 갈 수 있는 리스트 추가

    return distance


n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

buses=[[] for i in range(n+1)]
path=[[] for i in range(n+1)] # 경로를 담는 리스트
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    buses[a].append((b,c))

x,y=map(int,sys.stdin.readline().split())


print(dijkstra(x)[y])
print(len(path[y]))
print(*path[y])



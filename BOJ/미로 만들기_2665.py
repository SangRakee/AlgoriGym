# 다익스트라 문제
# 하나의 출발지에서 하나의 목적지만 구하면 되는 문제
# 그래서 distance 리스트를 선언할 필요 없이 우선순위 큐에서 쌓인 cost 비용만 더하면 된다
# distance 리스트가 없다보니 visited 리스트를 만들어 방문처리를 해줌

import sys
import heapq

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

n=int(sys.stdin.readline())

room=[]
for i in range(n):
    x=list(map(str,sys.stdin.readline()))
    room.append(x)

# 초기 출발지 설정
heap=[]
visited=[[0]*n for i in range(n)]
heapq.heappush(heap,(0,0,0))
visited[0][0]=1

# 우선순위 큐에 추출
while heap:
    cost,x,y=heapq.heappop(heap)

    # 목적지 일때 종료
    if x==n-1 and y==n-1:
        print(cost)
        exit(0)

    # 상하좌우로 이동
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]

        # 범위 밖으로 안 벗어났는지
        if 0<=nx<n and 0<=ny<n:
            # 방문한 적이 있는지
            if visited[nx][ny]==0:
                # 우선순위 큐에 넣기
                # 검은방일때
                if room[nx][ny]=="0":
                    heapq.heappush(heap,(cost+1,nx,ny))
                else: # 흰방일때
                    heapq.heappush(heap,(cost,nx,ny))
                # 체크인
                visited[nx][ny]=1

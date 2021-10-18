# 시뮬레이션
# 삼성 기출

from _collections import deque
import heapq


def bfs(r,c,eat,level,time):
    queue=deque([])
    queue.append([r,c])
    visited=[[-1]*N for i in range(N)]
    visited[r][c]=0
    temp=0
    eat_list=[]

    # 큐에서 하나씩 추출
    while queue:
        x,y=queue.popleft()

        # 갈 수 있는곳 순회
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            # 벗어나는가
            if 0<=nx<N and 0<=ny<N:

                # 방문 했는 곳인가
                if visited[nx][ny]==-1:

                    # 물고기가 있을 시
                    if arr[nx][ny]!=0:

                        # 물고기가 더 클시 이동 불가
                        if arr[nx][ny]>level:
                            continue

                        # 물고기와 같은 경우 이동만
                        elif arr[nx][ny]==level:
                            queue.append([nx,ny])
                            visited[nx][ny]=visited[x][y]+1

                        # 물고기가 더 작을 시 먹고 이동
                        elif arr[nx][ny]<level:
                            queue.append([nx,ny])
                            visited[nx][ny]=visited[x][y]+1

                            heapq.heappush(eat_list,[visited[nx][ny],nx,ny])

                    # 물고기가 없을 시
                    else:
                        queue.append([nx, ny])
                        visited[nx][ny] = visited[x][y] + 1

    if eat_list:
        dic,nx,ny=heapq.heappop(eat_list)
        eat_list = []
        eat+=1
        if eat==level:
            level+=1
            eat=0

        s_r,s_c=nx,ny
        temp=visited[nx][ny]
        visited=[[-1]*N for i in range(N)]
        visited[s_r][s_c]=temp
        queue=deque([[s_r,s_c]])
        arr[s_r][s_c]=0
        arr[r][c]=0

        return nx,ny,eat,level,temp
    else:
        return None

        # break


    print(temp)
    exit(0)






# 상좌우하
dx=[-1,0,0,1]
dy=[0,-1,1,0]


N=int(input())

arr=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    arr.append(tmp)
    for j in range(len(tmp)):
        if tmp[j]==9:
            s_x=i
            s_y=j
            arr[s_x][s_y]=0

level=2
eat=0
time=0
answer=0

# while문 - 아기상어가 잡아먹을 고기가 없을 떄 까지
while True:
        # 2.상어 이동
    next_value=bfs(s_x,s_y,eat,level,time)

    if next_value is None:
        break
    s_x, s_y, eat, level, time=next_value
    answer+=time


print(answer)
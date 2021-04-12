#처음풀었던 방식(1) : arr list에 순환한 노드들을 넣어서 중복 제거한 다음에 arr의 갯수 구하는 방식
#다른사람 풀이(2) : 방문 하지 않은 노드만 BFS해서 BFS할때마다 횟수 구하는 방식
#1번째보다 2번째 방식이 더 좋은 것 같음ㅎㅎ
from _collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())

graph=[[]for i in range(n+1)]
circle=[]
arr=[]

for i in range(m):
    x,y=map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)

def dfs(graph,start,visited,arr):
    queue=deque([start])
    visited[start]=1
    while queue:
        v=queue.popleft()
        arr.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=1

#1번째 방식
for i in range(1,n+1):
    arr=[]
    visited = [0] * (n + 1)
    dfs(graph,i,visited,arr)
    arr.sort()
    if arr not in circle:
        circle.append(arr)

#2번째 방식
# count=0
# for i in range(1,n+1):
#     if not visited[i]:
#         dfs(graph,i,visited)
#         count+=1


print(len(circle))
#print(count) 2번째 방식 출력값




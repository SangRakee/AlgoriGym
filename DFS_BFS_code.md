# DFS/BFS

### DFS

```python
graph=[]
visited=[False] * 노드갯수

def dfs(graph,v,visited):
    visited[v]=True  #현대 노드 방문 처리
    print(v, end=' ')
    for i in graph[v]: #현재 노드와 연결된 다른 노드를 재귀적으로 방문 
        if not visited[i]:
            dfs(graph,i,visited)
```



### BFS

```python
from colletion import deque   #Queue 생성 라이브러리

graph=[]
visited=[False] * 노드갯수

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]= True
    while queue:
        v=queue.popleft()
        print(v,end= '')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
```




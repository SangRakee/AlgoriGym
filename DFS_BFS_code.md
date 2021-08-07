# DFS/BFS

### DFS

```python
graph=[]
visited=[False] * 노드갯수

def dfs(v):
    visited[v]=True  #현대 노드 방문 처리
    print(v, end=' ')
    for i in graph[v]: #현재 노드와 연결된 다른 노드를 재귀적으로 방문 
        if not visited[i]:
            dfs(graph,i,visited)
```

1. 체크인

2. 목적지인가?
3. 갈 수 있는곳을 순회
4. 갈 수 있는가?
5. 간다
6. 체크아웃





### BFS

```python
from collections import deque   #Queue 생성 라이브러리

graph=[]
visited=[False] * 노드갯수

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]= True
    
    while queue:
        v=queue.popleft()		  # 1. 큐에서 꺼내옴
        print(v,end= '')
        for i in graph[v]:        # 3.갈 수 있는 곳 순회
            if not visited[i]:    # 4.갈 수 있는가
                queue.append(i)   # 5.큐에넣기
                visited[i]=True   # 6.체크인
```



1. 큐에서 꺼내옴
2. 목적지인가?
3. 갈 수 있는 곳 순회
4. 갈 수 있는가
5. 큐에 넣기
6. 체크인
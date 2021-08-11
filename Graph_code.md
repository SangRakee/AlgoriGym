# 그래프

- 무향, 유향, 인접

- 차수

- 싸이클

- 트리 : 순환이 없음, 경로가 1개 존재

  1. 관련 문제(서로소 집합 문제)

     - 유니온/파인드

     1)	parent[i] 초기화

     ```python
     for i in range(1,n+1):
         parent.append(i)
     ```

     2)	find 함수

     ```python
     def find(a):
         # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
         if parent[a] != a:
             parent[a] = find(parent[a])
         return parent[a]
     ```

     3) 	union 함수

     ```python
     def union(a,b):
         # a랑 b를 하나로 합집합 하겠다
         pa=find(a)
         pb=find(b)
         parent[pb]=pa
         
         # a랑 b가 우선순위가 정해질때 코드
         #if pa < pb:
         #    parent[pb] = pa
         #else:
         #    parent[pa] = pb
     ```

     

  

  2. 관련 문제(위상 정렬, DAG, O(V+E) ) - BFS 응용

     - 위상 : 비순환 / 방향

       1)	진입차수를 input으로 받는다

       ```python
       indegree=[0]*N+1
       ```

       2)	진입차수 0인 애들 초기 Queue 적재

       ```python
       for i in range(1,N+1):
           if indegree[i]==0:
               queue.append(i)
       ```

       3)	Queue에서 1개씩 뽑으면서 "연결된 간선 끊어주기"

       ```python
       result=[] #알고리즘 수행 결과를 담을 리스트
       while queue:
           now=queue.popleft()
           result.append(now)
       ```
       
       3-1)  Queue에서 뽑은 노드와 연결된 노드들의 진입차수 1빼기
       
        ```python
        for i in grahp[now]:
            indegree[i]-=1
            if indegree[i]==0:
                queue.append(i)
        ```
       
       



### 트리

- 순환이 없다. 경로가 1개 존재
- Root가 존재할 수 있다.

- 자신-부모 관계는 있다(LCA,단절점 등 Depth 구할때)

- 신장트리 : 모든 정점이 연결된 트리



- 최소신장트리(MST)    - 크루스칼, 프림

  - 최소값으로 모든 장점을 연결해라

    ex)  모든 도시의 수도관 연결. 최소 비용으로

    ​		네크워크 연결. 모든 컴퓨터를 인터넷 연결. 최소 비용으로.

  1)	답이 여러개일 수 있다.

  2) 	간선 개수는 N-1이다.

  ​	if (cnt == N-a) break;

- 크루스칼 알고리즘 (시간 복잡도 : O(ElogE) ) 

  1)	모든 간선을 cost 오름차순 정렬 ( 작은 값부터 뽑을 수 있게)

  ​	PrioriryQueue 사용 추천(자동 정렬이기 때문)

  ```python
  import heapq
  edge=[]
  heapq.heappush(edge,(cost,a,b))
  ```

  2)	최소 cost부터 간선 뽑기

  ```python
  while edge:
      cost,a,b=heapq.heapop(edge)
  ```

  2-1)	두 정점이 이미 연결 O

  ```python
  	if find(a)==find(b):
          continue
  ```

  2-2)	두 정점이 연결 X

  ```python
  	else:
  		union(a,b)
  		result+=cost
  ```

  - 기본적으로 서로소(find/union) 함수를 알고 있어야 하는 문제




- 최단 경로 알고리즘


  - 다양한 경우


    - 한 지점에서 다른 한 지점까지 최단 경로
    - 한 지점에서 다른 모든 지점가지의 최단 경로(다익스트라, 벨만-포드)
    - 모든 지점에서 다른 모든 지점까지의 최단 경로(플로이드-워셜)

  - 다익스트라, 벨만-포드, 플로이드-워셜 알고리즘

  - 다익스트라 알고리즘(우선 순위 큐 적용시: O(ElogV) )

    - 출발지 고정

    - 음의 간선x

    - 우선순위큐

      1)	기본 세팅

      ```python
      import heapq
      INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
      graph = [[] for i in range(N+1)] # 노드별 간선정보(진출차수)가 담긴 그래프 리스트
      distance = [INF] * (N + 1) # 최단 거리 테이블을 모두 무한으로 초기화
      
      # 경로를 담는 리스트 (문제에서 경로를 물어볼 시)
      # path = [[] for i in range(N+1)] 
      ```
      
      2)	초기 출발지 고정
      
      ```python
      def dijkstra(start):
          edges = [] #우선순위 큐
          # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 우선순위 큐 삽입
          heapq.heappush(edges, (0, start))
          distance[start] = 0
      ```
      
      3)	우선 순위 큐로 최단 거리 노드 추출
      
      ```python
      	while edges:
      		# 최단 거리가 가장 짧은 노드 정보 추출
              dist, now = heapq.heappop(edge)
      ```
      
      3-1) 	현재 노드가 이미 처리된 적 있는 노드 판단
      
      ```python
            	if distance[now]<dist:
                  continue
              # 현재 노드에 연결된 노드 추가
              # path[now].append(now)
      ```
      
      3-2)	현재 노드와 연결된 다른 인접한 노드들 확인

      ```python
              for i in grahp[now]:
                  cost = dist + i[1]    # i[0]: 목적지, i[1]: 비용
      ```
      
      3-3)	현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      
      ```python
      			if cost < distance[i[0]]:
                      distance[i[0]] = cost
                      heapq.heappush(edges, (cost, i[0]))
                      # 최단 거리 수정으로 인해 최단 경로 수정 
                      # path[i[0]]=path[now][:]
      ```
      
      

  

  - 벨만-포드

    - 출발지 고정

    - 음수 간선 가능(음수 사이클x)

    - O(E*V)

      ```
      ```

      ```
      ```

      ```
      ```

      ```
      ```

      ```
      
      ```

  -  플로이드-워셜

    - 모든 경로의 최단거리 파악
    
    - 음수 간선 가능
    
    - 음수 싸이클 있으면 불가
    
    - O(N^3) -- 300미만
    
      1)	기본 세팅
    
      ```python
      graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
      ```
    
      2)	초기 비용 세팅
    
      ```python
      # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
      for a in range(1, n + 1):
          for b in range(1, n + 1):
              if a == b:
                  graph[a][b] = 0
                  
      # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
      for _ in range(m):
          a, b, cost = map(int, input().split())
          graph[a][b] = cost
      ```
    
      3)	점화식
    
      ```python
      # 점화식에 따라 플로이드 워셜 알고리즘을 수행
      for k in range(1, n + 1): 			# 경유지
          for a in range(1, n + 1):   	# 출발지
              for b in range(1, n + 1):	# 도착지
                  graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
      ```
    
      
    
      

  | 다익스트라 | 벨만-포드 | 플로이드-워셜 |
  | ---------- | --------- | ------------- |
  |            |           |               |
  |            |           |               |
  |            |           |               |
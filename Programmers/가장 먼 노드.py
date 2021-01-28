# 테스트케이스
# n=6
# vertex=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


from _collections import deque

def bfs(graph,start,visited):
    cnt=0
    count=0
    queue=deque([[start,count]])
    while queue:
        value=queue.popleft()
        print("방문노드: ",start)
        start = value[0]
        count = value[1]
        if visited[start] == -1:
            visited[start] = count
            count += 1
            for i in graph[start]:
                queue.append([i, count])

def solution(n, vertex):
    answer = 0
    visited=[-1]*(n+1)
    graph=[[]for i in range(n+1)]

    for i in range(len(vertex)):
        graph[vertex[i][0]].append(vertex[i][1])
        graph[vertex[i][1]].append(vertex[i][0])
    print(graph)
    bfs(graph,1,visited)
    for value in visited:
        if value == max(visited):
            answer += 1



    return answer

print(solution(n,vertex))

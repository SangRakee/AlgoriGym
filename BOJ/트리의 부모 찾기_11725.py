import sys
sys.setrecursionlimit(100000) #런타임 에러 방지
n=int(sys.stdin.readline())
arr=[]
visited=[0]*(100001)
tree=[0]*(n+1)
graph=[[]for i in range(n+1)]

for i in range(n-1):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph,start,visited,tree):
    visited[start]=1
    for i in graph[start]:
        if not visited[i]:
            print(i,start)
            tree[i]=start
            dfs(graph,i,visited,tree)

dfs(graph,1,visited,tree)

print(tree)
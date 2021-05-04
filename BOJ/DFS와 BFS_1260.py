n,m,v=map(int,input().split())
arr=[[0]*(n+1)for i in range(n+1)]
dfs_visit=[0 for i in range(n+1)]
bfs_visit=[0 for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    arr[a][b]=1
    arr[b][a]=1

def dfs(v):
    if dfs_visit[v]:
        return
    dfs_visit[v]=1
    print(v,end=' ')
    for i in range(1,n+1):
        if dfs_visit[i]==0 and arr[v][i]==1:
            dfs(i)

def bfs(v):
    queue=[v]
    bfs_visit[v]=1
    while queue:
        v=queue[0]
        print(v,end=' ')
        del queue[0]
        for i in range(1,n+1):
            if bfs_visit[i]==0 and arr[v][i]==1:
                queue.append(i)
                bfs_visit[i]=1

dfs(v)
print()
bfs(v)
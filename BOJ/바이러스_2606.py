n=int(input())
num_net=int(input())
net=[]
vir=[]


for i in range(num_net):
    x,y=map(int,input().split())
    net.append([x,y])

graph=[[0]*(n+1) for i in range(n+1)]

for i in net:
    graph[i[0]][i[1]]=1
    graph[i[1]][i[0]]=1

def dfs(graph,start,visited,vir):
    visited[start]=1
    vir.append(start)
    for i in range(1,len(graph[start])):
        if not visited[i] and graph[start][i]:
            dfs(graph,i,visited,vir)


visited=[0]*(n+1)
dfs(graph,1,visited,vir)
vir.remove(1)
print(len(vir))

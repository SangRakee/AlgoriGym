#백트래킹
#기본 순열

def dfs(v,arr,visited,answer,temp,m):
    if len(temp)==m:
        # print(temp)
        for i in temp:
            print(i,end=" ")
        print("")
        return
    for i in range(len(arr)):
        if visited[i]==0:
            visited[i]=1
            temp.append(arr[i])
            dfs(i+1,arr,visited,answer,temp,m)
            visited[i]=0
            temp.pop()



n,m=map(int,input().split())

arr=[]
for i in range(n):
    arr.append(i+1)


visited=[0]*len(arr)
answer=[]
temp=[]
dfs(0,arr,visited,answer,temp,m)
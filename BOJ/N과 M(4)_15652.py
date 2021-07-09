#백트래킹
#동일한 값을 뽑을 수 있는 조합(기존 조합과 비교했을 때, 12,15번째 줄에서 방문을 체크할 필요가 없고 15번째 재귀를 동일한 곳에서 시작)

def dfs(v,arr,visited,answer,temp,m):
    if len(temp)==m:
        for i in temp:
            print(i,end=" ")
        print("")
        return
    for i in range(v,len(arr)):
        if visited[i]==0 and len(temp)<m:
            # visited[i]=0
            temp.append(arr[i])
            dfs(i,arr,visited,answer,temp,m)
            # visited[i]=1
            temp.pop()



n,m=map(int,input().split())

arr=[]
for i in range(n):
    arr.append(i+1)


visited=[0]*len(arr)
answer=[]
temp=[]
dfs(0,arr,visited,answer,temp,m)
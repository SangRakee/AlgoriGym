#백트래킹
#기본 순열문제

def per(v,arr,visited,answer,temp,m):
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
            per(i+1,arr,visited,answer,temp,m)
            visited[i]=0
            temp.pop()


n,m=map(int,input().split())

arr=list(map(int,input().split()))

# print(arr)
visited=[0]*len(arr)
answer=[]
temp=[]
arr.sort()
per(0,arr,visited,answer,temp,m)
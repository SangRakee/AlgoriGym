#백트래킹, 브루트포스 문제

import sys
result=[]
def com(v,arr,visited,temp):
    if len(temp)==7:
        if sum(temp)==100:
            temp.sort()
            for i in range(len(temp)):
                print(temp[i])
            return
    for i in range(v,len(arr)):
        if visited[i]==0:
            visited[i]=1
            temp.append(arr[i])
            com(i+1,arr,visited,temp)
            visited[i]=0
            temp.pop()

arr=[]
temp=[]
visited=[0]*9

for i in range(9):
    x=int(sys.stdin.readline())
    arr.append(x)

com(0,arr,visited,temp)
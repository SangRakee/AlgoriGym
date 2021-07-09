#백트래킹 문제

k=int(input())
arr1=list(map(str,input().split()))
num=[0,1,2,3,4,5,6,7,8,9]
result=[]

def dfs(v,x,visited,num,temp,arr1,result):
    # visited[v]=1
    if len(temp)>=(k+1):
        print(temp)
        x="".join(map(str,temp))
        result.append(x)
        return temp

    for i in range(len(num)):
        if visited[i]==0:
            if len(temp)==0:
                visited[i]=1
                temp.append(num[i])
                dfs(i, x, visited, num, temp, arr1,result)
                temp.pop()
                visited[i] = 0
            else:
                if arr1[x]==">":
                    if temp[-1]>num[i]:
                        temp.append(num[i])
                        visited[i]=1
                        dfs(i,x+1,visited,num,temp,arr1,result)
                        temp.pop()
                        visited[i] = 0

                elif arr1[x]=="<":
                    if temp[-1]<num[i]:
                        temp.append(num[i])
                        visited[i]=1
                        dfs(i,x+1,visited,num,temp,arr1,result)
                        temp.pop()
                        visited[i] = 0


#반복문으로 전체 다 해볼필요 없이 dfs(0)으로도 해결 가능
# for i in num:
visited=[0]*len(num)
temp=[]
x=0
dfs(0,x,visited,num,temp,arr1,result)
#
#
# print(result)
print(max(result))
print(min(result))
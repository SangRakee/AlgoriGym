n=int(input())
arr=[]

weight=[[0]*100 for i in range(100)]


for i in range(n):
    x=list(map(int,input().split()))
    arr.append(x)

for i in range(len(arr)):
    for j in range(10):
        for z in range(10):
            weight[arr[i][0]+j][arr[i][1]+z]=1
cnt=0
for i in range(100):
    for j in range(100):
        if weight[i][j]==1:
            cnt+=1

print(cnt)
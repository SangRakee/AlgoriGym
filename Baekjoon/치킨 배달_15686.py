from itertools import combinations

n,m =map(int,input().split())
area=[]
chicken=[]
home=[]
min_dist=[]

for i in range(n):
    x=list(map(int,input().split()))
    area.append(x)

for i in range(n):
    for j in range(n):
        if area[i][j]==1:
            x=[i+1,j+1]
            home.append(x)
        elif area[i][j]==2:
            x=[i+1,j+1]
            chicken.append(x)



for i in range(len(chicken)):
    count=[]
    for j in range(len(home)):
        dist=abs(chicken[i][0]-home[j][0])+abs(chicken[i][1]-home[j][1])
        count.append(dist)

    min_dist.append(count)

answer=[]
for i in combinations(min_dist,m):
    x=0
    sum=0
    for j in range(len(i[0])):
       arr=[]
       for z in range(m):
            arr.append(i[z][j])
       sum+=min(arr)
    answer.append(sum)
print(min(answer))
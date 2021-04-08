n=int(input())
load=list(map(int,input().split()))
city=list(map(int,input().split()))

money=0
dic=0
mincity=city[0]

for i in range(n-1):
    if mincity>=city[i+1]:
        dic+=load[i]
        money+=dic*mincity
        mincity = city[i+1]
        dic=0
    else:
        dic+=load[i]
money += dic*mincity

print(money)





def dist_calc(idx, pos):
    if idx ==1:
        return pos
    elif idx==2:
        return C + R + C - pos
    elif idx==3:
        return C + R + C + R -pos
    else:
        return C+pos

C,R =map(int,input().split())
circumference=(C+R)*2

N=int(input())
dist=[]
for i in range(N+1):
    idx,pos=map(int,input().split())
    dist.append(dist_calc(idx,pos))

my_dist=dist[-1]

anwwer=0

for i in range(N):
    clockwise=abs(my_dist-dist[i])
    anwwer+=min(clockwise,circumference-clockwise)

print(anwwer)

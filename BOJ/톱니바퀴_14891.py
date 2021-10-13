# 구현
# 삼성 기출

import sys

def solve(n,d):
    visited[n]=1
    bef_n=n-1
    aft_n=n+1

    now=arr[n]
    n6=now[6]
    n2=now[2]

    if d == -1:
        a = now.pop(0)
        now.append(a)
        arr[n] = now
    else:
        a = now.pop()
        now.insert(0, a)
        arr[n] = now

    # 벗어나지 않는 바퀴 일때
    if 0<=bef_n<4:
        if visited[bef_n]==0:

            bef=arr[bef_n]

            if bef[2]!=n6:
                if d==-1:
                    solve(bef_n,1)
                else:
                    solve(bef_n,-1)
    #     else:
    #         return
    # else:
    #     return


    if 0<=aft_n<4:
        if visited[aft_n]==0:
            aft=arr[aft_n]

            if aft[6]!=n2:
                if d==-1:
                    solve(aft_n,1)
                else:

                    solve(aft_n,-1)
            else:
                return
        else:
            return




arr=[]
for i in range(4):
    x=list(map(int,input()))
    arr.append(x)


K=int(input())

direction=[]
for _ in range(K):
    a,b=map(int,input().split())
    direction.append([a,b])
#
# print(arr)
# print(direction)


for d in direction:
    num,dir=d
    visited=[0,0,0,0]
    solve(num-1,dir)

    # print(arr)

answer=0
for i in range(len(arr)):
    if arr[i][0]==1:
        answer+=(2**i)

print(answer)
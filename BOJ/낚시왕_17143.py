# 시뮬레이션
# 삼성 sw 역량테스트 기출
# 속력만큼 움직이는 것을 구하는 과정에서 속력마다 반복문을 동작시키면 시간초과 발생
# 해결방법. 2*(n-2) 진행하면 원래 위치로 되돌아 오기 때문에 속력%2*(n-2) 범위로만 반복한다

import heapq

def change(d):

    if d==0:
        d=1
    elif d==1:
        d=0
    elif d==2:
        d=3
    elif d==3:
        d=2


    return d

# 상하우좌
dx=[-1,1,0,0]
dy=[0,0,1,-1]

# 입력
R,C,M=map(int,input().split())

p_y=-1

arr=[[-1]*(C) for i in range(R)]
sharks={}
for i in range(M):
    r,c,s,d,z=map(int,input().split())
    arr[r-1][c-1]=i
    sharks[i]=[r-1,c-1,s,d-1,z]

answer=0
for i in range(C):
    # print(sharks)
    if M==0:
        answer=0
        break

    # 1.사람 한칸 옆으로
    p_y+=1

    dead_s=[]
    # 2.땅이랑 가장 가까운 상어 제거
    for key in sharks.keys():
        x, y, s, d, z = sharks[key]
        if y==p_y:
            heapq.heappush(dead_s,[x,key])

    # 2-1.잡을 상어가 여러 마리인 경우
    # print(p_y,dead_s, end=" ")
    if dead_s:
        x,num=heapq.heappop(dead_s)
        answer+=sharks[num][4]
        # print(answer)
        del sharks[num]

    # print(sharks)
    # 3.상어 이동
    for key in sharks.keys():
        x,y,s,d,z=sharks[key]

        if d==0 or d==1:
            for _ in range(s%(2*R-2)):
                nx=x+dx[d]
                ny = y + dy[d]
                if not (0 <= nx < R and 0 <= ny < C):
                    d = change(d)
                    nx = x + dx[d]
                    ny = y + dy[d]
                x = nx
                y = ny

        else:
            for _ in range(s%(2*C-2)):
                nx=x+dx[d]
                ny = y + dy[d]
                if not (0 <= nx < R and 0 <= ny < C):
                    d = change(d)
                    nx = x + dx[d]
                    ny = y + dy[d]
                x = nx
                y = ny


        sharks[key]=[x,y,s,d,z]

    dic={}
    # 4.부딪히는 상어가 있는지
    for key in sharks.keys():
        x, y, s, d, z = sharks[key]
        if (x,y) in dic:
            dic[x,y].append([z,key])
        else:
            dic[x,y]=[[z,key]]


    for v in dic.values():
        if len(v)>=2:
            max_s=sorted(v,reverse=True)[0][1]
            for j in range(len(v)):
                if v[j][1]!=max_s:
                    del sharks[v[j][1]]
        # del sharks[max_s]
    # print(sharks)

print(answer)
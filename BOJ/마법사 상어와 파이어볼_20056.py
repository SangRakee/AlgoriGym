# 틀린코드
# 시뮬레이션 
# 삼성 SW 역량테스트 기출

# 틀린부분
# 기존 이중리스트를 만들어서 각 x,y좌표에 해당 인덱스를 넣는 코드인데 매번 좌표를 확인할때 N*N의 시간복잡도를 줄이기 위해 딕셔너리를 이용했지만,
# 딕셔너리 특성상 여러 리스트를 넣는 value에서 데이터 처리가 어려움이 있고 keyError가 발생하였음

from _collections import deque

def check(list):

    num=list[0]%2

    for i in list[1:]:
        if num!=(i%2):
            return False

    return True



# 상 우 하 좌
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

# 입력
N,M,K=map(int,input().split())

dic={}

fireballs=deque()
for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    fireballs.append([r-1,c-1])
    dic[r-1,c-1]=[[m,s,d]]

# print(arr)

# 반복문 - K번
for _ in range(K):

    tmp_arr=[]

    for i in range(len(fireballs)):
        r,c=fireballs.popleft()
        # print(dic[r,c])
        # print(dic)
        if dic:
            for m,s,d in dic[r,c]:
                # 이동거리 계산
                nr=(r+dx[d]*s)%N
                nc=(c+dy[d]*s)%N

                fireballs.append([nr,nc])
                tmp_arr.append([nr,nc,m,s,d])
            del dic[r,c]

    for x,y,m,s,d in tmp_arr:
        if (x,y) in dic:
            dic[x,y].append([m,s,d])
        else:
            dic[x,y]=[[m,s,d]]
    # print(tmp_arr)
    for (x,y) in dic:
        if len(dic[x,y])>=2:
            nm, ns, odd, even, flag = 0, 0, 0, 0, 0
            list_d=[]
            for a in dic[x,y]:
                m,s,d=a
                nm+=m
                ns+=s
                list_d.append(d)
            flag=check(list_d)
            nm=nm//5
            ns=ns//len(dic[x,y])
            dic[x,y]=[]
            if nm!=0:
                for i in range(4):
                    if flag==True:
                        nd=2*i
                    else:
                        nd=2*i+1
                    if (x, y) in dic:
                        dic[x, y].append([nm, ns, nd])
                    else:
                        dic[x, y] = [[nm, ns, nd]]

# print(dic)
answer=0
for value in dic.values():
    for m,s,d in value:
        answer+=m
print(answer)


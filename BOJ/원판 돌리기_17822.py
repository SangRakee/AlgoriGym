# 시뮬레이션
# 삼성 sw 역량 테스트 기출

# 고민했던 점1
# 인접한 수를 확인할때 차례로 변환하다가 변환된 X랑 인접한 수를 비교할때 문제점 발견(코드상에서는 비교할때 이전에 변환된 값이랑 비교하게 되는 문제점)
# arr와 같은 임시 리스트(tmp)를 만들어서 변환 된 값은 tmp에 저장하고 비교하는 값은 arr로 비교해서 해결

from _collections import deque

# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]


N,M,T=map(int,input().split())

arr=[[]]
for i in range(N):
    tmp=list(map(int,input().split()))
    arr.append(tmp)


direction=[]
for _ in range(T):
    x,d,k=map(int,input().split())
    direction.append([x,d,k])


for dir in direction:
    x,d,k=dir

    # 1.회전

    # 반복문 - x부터 len(arr)까지 x칸으로
    for i in range(x,len(arr),x):

        # tmp - 해당 행 리스트
        queue=deque(arr[i])

        # d==0일때 시계 방향
        if d==0:
            # 반복문 - k번
            for j in range(k):
                # 마지막 인덱스를 가장 처음으로 추가
                queue.appendleft(queue.pop())

        # d==1일때 반시계 방향
        else:
            # 반복문 - k번
            for j in range(k):
                # 가장 처음 인덱스를 가장 마지막으로 추가
                queue.append(queue.popleft())
        arr[i]=list(queue)

    # print("회전 :",arr)


    # 2.인접한 수 계산

    lock=False

    tmp=[i[:] for i in arr]

    # 이중포문 - 좌표 이동
    for x in range(1,N+1):
        for y in range(M):
            flag=False
            if arr[x][y]!="X":
                # 상하좌우로 인접한 인덱스 찾기
                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]

                    # 인접한 인덱스가 범위를 벗어나는 경우
                    if (1<=nx<N+1 and 0<=ny<M):
                        if arr[x][y] == arr[nx][ny]:
                            flag = True
                            lock=True
                            tmp[nx][ny] = "X"
                    elif not (1<=nx<N+1):
                        continue

                    elif not (0<=ny<M):
                        if ny<0:
                            ny=M-1
                        elif ny>=M:
                            ny=0

                        if arr[x][y]==arr[nx][ny]:
                            flag=True
                            lock=True
                            tmp[nx][ny]="X"

                if flag==True:
                    lock=True
                    tmp[x][y]="X"
    arr=[i[:] for i in tmp]
    # print("인접한 :", arr)
    # 인접한 인덱스가 없는 경우
    if lock==False:
        # print("!!")
        # 남은수 평균 구하기
        sum_index=0
        cnt=0
        # 이중 포문 - 좌표 이동
        for i in range(1,N+1):
            for j in range(M):
                if arr[i][j]!="X":
                    sum_index+=arr[i][j]
                    cnt+=1
        if sum_index!=0:
            avg_index=sum_index/cnt
        else:
            avg_index=0

        for i in range(1,N+1):
            for j in range(M):
                if arr[i][j] != "X":
                    if arr[i][j]>avg_index:
                        arr[i][j]-=1
                    elif arr[i][j]<avg_index:
                        arr[i][j]+=1

    #     print("평균 :", arr)
    # print()


answer=0
for i in range(1,N+1):
    for j in range(M):
        if arr[i][j]!="X":
            answer+=arr[i][j]

print(answer)
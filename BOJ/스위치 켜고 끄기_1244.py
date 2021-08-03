# 구현 문제

import sys

N=int(sys.stdin.readline())
switch=list(map(int,sys.stdin.readline().split()))
# switch.insert(0,0)

M=int(sys.stdin.readline())



for _ in range(M):
    sex,num=map(int,sys.stdin.readline().split())
    # print("처음",switch)
    # 1. 남자일때
    if sex==1:
        # 1-1. 몇배수 인지
        count=(len(switch))//(num)
        # 1-2. 배수만큼 스위치 상태 변경
        for i in range(1,count+1):
            switch[num*i-1]=(switch[num*i-1]+1)%2
    # 2. 여자일때
    elif sex==2:
        # 2-1. 범위에서 안벗어나는 선에서 좌우 한칸씩 이동
        index=0
        while True:
            if num-index-1<0 or num+index-1>=len(switch):
                break
            if index==0:
                switch[num-1]=(switch[num-1]+1)%2
            else:
                if switch[num-index-1]==switch[(num+index-1)]:
                    switch[num-index-1]=(switch[num-index-1]+1)%2
                    switch[num+index-1]=(switch[num+index-1]+1)%2
                else:
                    break
            # print(index, switch)
            index+=1



# 3. 출력
for i in range(0,len(switch),20):
    print(*switch[i:i+20])



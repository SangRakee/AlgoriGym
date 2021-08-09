# 구현 문제
# Queue를 사용해서 다리에 트럭이 지나가는 과정을 구현
# 마지막에는 truck Queue에서 모든 트럭이 나오는 순간 while문이 끝나기 때문에 다리에서 아직 못 벗어난 트럭을 빼주기 위해 time 변수에 다리 길이만큼 더 해줌

import sys
from collections import deque

n,w,l=map(int,sys.stdin.readline().split())
truck=deque(list(map(int,sys.stdin.readline().split())))

time=0
brige=deque([0]*(w))

while truck:
    brige.popleft()

    # 현재 다리 무게에 다음 트럭 추가
    if sum(brige)+truck[0]<=l:
        brige.append(truck.popleft())
        time += 1
    # 아니면 대기
    else:
        brige.append(0)
        time += 1


    # print(brige,time)

print(time+w)


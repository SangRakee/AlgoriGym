# 힙 문제
# push할때 이차원 배열로 넣고 첫번째 인덱스에 절댓값을 넣고 두번째 인덱스에는 원래값을 넣어서 우선순위가 절대값한 값으로 들어가게 한다.
# pop할때는 두번째 인덱스인 원래값을 뽑는다.

import heapq
import sys

n=int(sys.stdin.readline())

heap=[]

for i in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,[abs(x),x])
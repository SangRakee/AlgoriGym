# 힙 문제
# 최대 힙에서 들어가고 나갈때 부등호만 변경 해주면 해결 

import heapq
import sys

n=int(sys.stdin.readline())

heap=[]

for i in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,x)
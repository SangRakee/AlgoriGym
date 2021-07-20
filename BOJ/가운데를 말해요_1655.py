# heap 문제
# 처음에 매번 정렬(힙정렬)해서 구했던 알고리즘은 시간초과 뜸

import sys
import heapq

n=int(sys.stdin.readline())

left_heap=[]
right_heap=[]

for _ in range(n):
    num=int(sys.stdin.readline())

    # 1. 두개의 heap을 번갈아가면서 넣을 조건문
    if len(left_heap)==len(right_heap):
        heapq.heappush(left_heap,(-num,num))
    else:
        heapq.heappush(right_heap,(num,num))

    # 2. 각 heap의 최상위 노드를 비교하는 것
    if right_heap and left_heap[0][1] > right_heap[0][1]: # left_heap의 최상위 노드가 right_heap의 최상위 노드보다 클때
        left_max=heapq.heappop(left_heap)[1]
        right_min=heapq.heappop(right_heap)[1]
        heapq.heappush(right_heap,(left_max,left_max))
        heapq.heappush(left_heap,(-right_min,right_min))

    print(left_heap[0][1])


# 우선순위 큐, Heap 문제
# 보석과 가방을 정렬한 다음에 포인트로 탐지하면서 하나씩 최대힙에 넣은 후 가방에 맞는 최대 값을 넣는 방식

import sys
import heapq

N,K=map(int,sys.stdin.readline().split())
jewelries=[]
bags=[]
money=0

heap=[]

for i in range(N):
    M,V=map(int,sys.stdin.readline().split())
    jewelries.append([M,V])

jewelries.sort()

for i in range(K):
    C=int(sys.stdin.readline())
    bags.append(C)

bags.sort()

# print(jewelries,bags)

point=0
for bag in bags:
    while True:
        if point==len(jewelries):
            break

        if bag <jewelries[point][0]:
            break

        if bag>=jewelries[point][0]:
           heapq.heappush(heap,(-jewelries[point][1],jewelries[point][0]))
           point+=1
    # print(bag,heap)
    if heap:
        money+=(-heapq.heappop(heap)[0])

print(money)

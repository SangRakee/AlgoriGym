# 최대 최소 구하는 문제
# 우선순위 큐를 이용하여 시간초과 해결

import heapq

def solution(A, B):
    answer = 0

    maxheap = []
    minheap = []

    for i in range(len(A)):
        heapq.heappush(maxheap, A[i])
        heapq.heappush(minheap, -B[i])

    leng = len(maxheap)
    for i in range(leng):
        max_value = -heapq.heappop(maxheap)
        min_value = heapq.heappop(minheap)
        answer += (max_value * min_value)

    return answer
# 힙 문제
# 1. 입력 시 sys 라이브러리 사용 안할시 시간 초과 발생
# 2. 두 번째 코드 처럼 try except IndexError문을 사용하여 배열이 빈 상태에서도 실행하는 것이 있지만 첫 번째 코드가 시간적으로 더 빠름

import heapq
import sys

n=int(sys.stdin.readline())

heap=[]

for i in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,-x)

# for i in range(n):
#     x=int(sys.stdin.readline())
#     try:
#         if x==0:
#             print(-heapq.heappop(heap))
#         else:
#             heapq.heappush(heap,-x)
#     except IndexError:
#         print(0)
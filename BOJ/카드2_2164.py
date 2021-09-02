# 큐

import sys
from _collections import deque

N=int(sys.stdin.readline())

arr=[i for i in range(1,N+1)]
q=deque(arr)

while len(q)!=1:
    q.popleft()
    q.append(q.popleft())

print(q[0])
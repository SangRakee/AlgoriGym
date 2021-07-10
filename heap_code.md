## 힙 정렬

```python
import sys
import heapq

input = sys.stdin.readline

#최소힙1
def minHeapsort1(arr):
    h=[]
    result=[]
    for i in arr:
        heapq.heappush(h,i)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

#최소힙2
def minHeapsort2(arr):
    heapq.heapify(arr)
    result=[]
    for i in range(len(arr)):
        result.append(heapq.heapop(h))
    return result

#최대힙1
def maxHeapsort1(arr):
    h=[]
    result=[]
    for i in arr:
        heapq.heappush(h,-i)
    print(h)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

#최대힙2
def maxHeapsort2(arr):
    heapq.heapify(arr)
    result=[]
    for i in range(len(arr)):
        result.append(heapq.heapop(h))
    return result[::-1]
    
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
res = minHeapsort1(arr)

print(res)
```

